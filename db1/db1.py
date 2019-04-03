import hid
import time
import math
from enum import Enum

class MessageId(Enum):
    ProtocolVersion = 1
    JumpToBootloader = 2

    SetRgbMode = 3
    SetRgbHsv = 4
    SetRgbHsvNoEeprom = 5

    IncreaseBrightness = 6
    DecreaseBrightness = 7

    GetDynamicKeymap = 8
    SetDynamicKeymap = 9

    GetMuteLedIsEnabled = 10
    SetMuteLedIsEnabled = 11

    SetMacro = 12
    GetMacro = 13

class RgbMode(Enum):
    Invalid = 0
    
    Static = 1

    Breathing1 = 2
    Breathing2 = 3
    Breathing3 = 4
    Breathing4 = 5

    RainbowMood1 = 6
    RainbowMood2 = 7
    RainbowMood3 = 8

    RainbowSwirl1 = 9
    RainbowSwirl2 = 10
    RainbowSwirl3 = 11
    RainbowSwirl4 = 12
    RainbowSwirl5 = 13
    RainbowSwirl6 = 14

    Snake1 = 15
    Snake2 = 16
    Snake3 = 17
    Snake4 = 18
    Snake5 = 19
    Snake6 = 20

    Knight1 = 21
    Knight2 = 22
    Knight3 = 23

    Xmas = 24

    StaticRainbow1 = 25
    StaticRainbow2 = 26
    StaticRainbow3 = 27
    StaticRainbow4 = 28
    StaticRainbow5 = 29
    StaticRainbow6 = 30
    StaticRainbow7 = 31
    StaticRainbow8 = 32
    StaticRainbow9 = 33
    StaticRainbow10 = 34

class Db1():

    def __init__(self):
        pass

    def open(self):
        try:
            h = hid.device()

            vendor_id = 0xFEED
            product_id = 0x6060

            device_list = hid.enumerate(vendor_id, product_id)

            for device in device_list:
                if device['usage_page'] == 65376:
                    h.open_path(device['path'])
                    break

            # enable non-blocking mode
            h.set_nonblocking(1)

            return h

        except IOError as ex:
            print(ex)
            print("You probably don't have the hard coded device. Update the hid.device line")
            print("in this script with one from the enumeration list output above and try again.")

        print("Done")

    def close(self, device):
        device.close()

    def write_read(self, data_to_write):
        # open the device
        device = self.open()

        # must put 0 at the beginning
        data_to_write = [0] + data_to_write

        if (len(data_to_write) < 33):
            data_to_write += [0] * (33 - len(data_to_write))

        # write the data
        device.write(data_to_write)

        # wait
        time.sleep(0.05)
        
        # read the data
        d = device.read(32)

        # close the device
        self.close(device)

        return d

    def set_rgb_mode(self, mode):
        self.write_read([MessageId.SetRgbMode.value, mode.value])

    # max hue : 360
    # max sat : 100
    # max brightness: 100
    def set_hsv_no_eeprom(self, hue, sat, brightness):
        sat = round(sat * 2.55)
        brightness = round(brightness * 2.55)
        sat_string = str(sat).encode('ascii')
        brightness_string = str(brightness).encode('ascii')
        self.write_read([MessageId.SetRgbHsvNoEeprom.value, hue >> 8, hue & 0xff, int(sat_string), int(brightness_string)])

    def set_hsv_eeprom(self, hue, sat, brightness):
        sat = round(sat * 2.55)
        brightness = round(brightness * 2.55)
        sat_string = str(sat).encode('ascii')
        brightness_string = str(brightness).encode('ascii')
        self.write_read([MessageId.SetRgbHsv.value, hue >> 8, hue & 0xff, int(sat_string), int(brightness_string)])

    def increase_brightness(self):
        self.write_read([MessageId.IncreaseBrightness.value])

    def decrease_brightness(self):
        self.write_read([MessageId.DecreaseBrightness.value])