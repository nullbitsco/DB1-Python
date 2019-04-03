from db1 import Db1
from db1 import RgbMode
import time

if __name__ == "__main__":
	print("DB1 Python API Demo!")

	DB1 = Db1()
	DB1.set_rgb_mode(RgbMode.Static)
	time.sleep(3)

	# Set LED mode Breathing
	DB1.set_rgb_mode(RgbMode.Breathing4)
	time.sleep(3)

	# Set LED mode Rainbow3
	DB1.set_rgb_mode(RgbMode.RainbowMood3)
	time.sleep(3)

	# Set LED mode Snake
	DB1.set_rgb_mode(RgbMode.Snake3)
	time.sleep(3)

	# Set LED mode Knight
	DB1.set_rgb_mode(RgbMode.Knight3)
	time.sleep(3)

	# Set LED mode Xmas
	DB1.set_rgb_mode(RgbMode.Xmas)
	time.sleep(3)

	# Set LED mode Static Rainbow
	DB1.set_rgb_mode(RgbMode.StaticRainbow10)
	time.sleep(3)

	# Set LED mode Static
	DB1.set_rgb_mode(RgbMode.Static)
	time.sleep(3)

	# Set LEDs to white, full brightness
	DB1.set_hsv_no_eeprom(0, 0, 100)
	time.sleep(1)

	# Set LEDs to red, full brightness
	DB1.set_hsv_no_eeprom(0, 100, 100)
	time.sleep(1)

	# Set LEDs to green, full brightness
	DB1.set_hsv_no_eeprom(130, 100, 100)
	time.sleep(1)

	# Set LEDs to blue, full brightness
	DB1.set_hsv_eeprom(230, 100, 100)
	time.sleep(1)

	# Set LEDs to rainbow mode
	DB1.set_rgb_mode(RgbMode.RainbowSwirl6)
	time.sleep(1)

	# Change brightness, one step at a time
	for x in range(20):
		DB1.decrease_brightness()
		time.sleep(0.1)

	for x in range(20):
		DB1.increase_brightness()
		time.sleep(0.1)

	print("Done!")