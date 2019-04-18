# DB1-Python
Python API library for interacting with the nullbits DB1/DB1 Pro. Program and control your DB1 using python!

# Dependencies
See [cython-hidapi](https://github.com/trezor/cython-hidapi) for setup.
DB1-Python is written in and requires python3.

# Installation (MacOS)
`brew install python`

`python3 --version`

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r example_reqs.txt`

`python3 basicTest.py`

# Examples
See basicTest.py for an all-in-one example of current implemented functionality, and APITest.py for a more advanced REST api-based example.

Inline example:
```python
from db1 import Db1
from db1 import RgbMode

DB1 = Db1()

# Set RGB mode to rainbow swirl
DB1.set_rgb_mode(RgbMode.RainbowSwirl6)

# Increase the brightness 10%
DB1.increase_brightness()

# Decrease the brightness 10%
DB1.decrease_brightness()

# Set HSV to light blue (doesn't save to EEPROM)
DB1.set_hsv_no_eeprom(180, 100, 100)

# Set HSV to light blue (saves to EEPROM)
DB1.set_hsv_eeprom(180, 100, 100)
```
Use a [color picker](https://alloyui.com/examples/color-picker/hsv) to get HSV values!

# Note on EEPROM
Writing to the internal EEPROM more than necessary isn't recommended. If you are using this library to do something that changes the LED colors frequently (changing based on weather, for example), it's suggested that you do so using set_hsv_no_eeprom() so avoid write-cycling the EEPROM unnecessarily. 

# TODO
* Dynamic keymapping support
* Macro support
* Discord Mute/Deafen LED support
