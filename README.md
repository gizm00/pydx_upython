


### The Internet of Cats - a micropython project
I wanted to learn a bit of [micropython](http://micropython.org) and a friend had an [ESP8266 micro controller](https://www.sparkfun.com/products/13678) and a [Nokia 5110 LCD display](https://www.sparkfun.com/products/10168) I could play with. And everyone loves cats, so thus the Internet of Cats was born!

#### What the heck is an internet of cats?
The Internet of cats is an access point for 1-bit cat pictures. A (very very simple) HTTP server runs on the ESP8266, listening for requests of 'cat=somecat'  If 'somecat' is found on the device, its bitmap will be rendered on the display, like so:

<img src = 'photos/pusheen_request.png'>

#### What! Thats amazing. How to I make one?
 I'm glad you asked! Feel free to follow along with my simple [step-by-step](http://www.homestarrunner.com/sbemail58.html) instructions. If you have any questions or problems please file an issue and I'll take a look.

But first! Thanks to the following folks for sharing their code and how-tos. This project would not have been possible without them.

<li>[Instructions for connecting the ESP-01 to the Nokia 5110 from Kendrick Tabi](https://www.kendricktabi.com/2015/08/esp8266-and-nokia-5110-lcd.html)
<li>[upcd8544.py by Markus Birth via Mike Causer](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Conways-Game-of-Life]upcd8544.py)
<li>[convert_png.py by Gary Bake](https://github.com/garybake/upython_wemos_shields/blob/master/oled/convert_png.py)
<li>http_server.py is based on [this example](https://github.com/micropython/micropython/tree/master/examples/network) from the MicroPython repo

#### Step 1, get the hardware

I prototyped this project using the [ESP-12](http://www.gearbest.com/transmitters-receivers-module/pp_227650.html) and later built a portable version with the [ESP-01](https://www.sparkfun.com/products/13678). The code folder in the repo has separate sub folders depending on which version of the ESP8266 you use. If I were to do it over again, I would probably use a breakout board like [this one from Adafruit](https://www.adafruit.com/product/2821). It would have saved me some debug and soldering time when adding an external supply and powering the chip. Adafruit also has some fantastic ESP8266 tutorials.

I used the [350mAh](https://www.adafruit.com/products/2750) and [500mAh](https://www.adafruit.com/products/1578) LiPo batteries from AdaFruit and they worked like a charm. 

For the display, the version of the Nokia 5110 I had was [this one from Sparkfun](https://www.sparkfun.com/products/10168) 

For connecting to the board, you will need a USB to TTY cable if you are just using the bare board like I did. <b>Important!</b> The supply for the ESP8266 is nominal 3.3V. Most off the shelf USB to TTY cables are 5V, which will reduce your project to a heap of smoldering sadness. 

You will want something like this [USB to TTL board](http://www.dx.com/p/ft232bl-module-usb-to-ttl-board-module-support-5v-3-3v-421177#.WCC5UhIrK1s) that has a 3V supply based on how you set the jumper.

#### Step 2, setup the board to flash the MicroPython firmware

You need to put the ESP8266 into boot loader mode to flash the MicroPython firmware. Heres how to do it.

For the ESP-12, the following setup is required to flash the device. Namely, you need to ground GPIO0 and GPIO5. Make sure CH_PD is high.
<img src='photos/esp12_firmware_flash.png'>
This photo is from [agcross.com](http://www.agcross.com/2015/09/the-esp8266-wifi-chip-part-3-flashing-custom-firmware)

For the ESP-01, you can [follow this pinout from Sparkfun](https://cdn.sparkfun.com/datasheets/Wireless/WiFi/ESP8266ModuleV1.pdf) for basic pin descriptions. I printed it out so I could reference it while working.  To setup the ESP-01 configure the pins as described in [this table](https://github.com/esp8266/esp8266-wiki/wiki/Uploading), specifically CH_PD and GPIO2 should be high, and GPIO0 should be low. There is no GPIO15 on the ESP-01, so ignore that.

#### Step 3, flash the firmware
Now that you've setup your device in bootmode, get the latest micropython firmware and send it to the device.

To do this you will need
<li>The [latest micropython firmware for the ESP8266](http://micropython.org/download#esp8266)
<li>The [esptool](github.com/themadinventor/esptool/) for sending the firmware to the device:
>pip install esptool

At this point you need to connect the ESP8266 to the USB port if you haven't already to communicate over the RX/TX lines

First, erase the flash
>esptool.py --port /dev/ttyUSB0 erase_flash

Unplug and replug in the 8266. If you dont you might see the following if you proceed immediately to flashing the board:

> “A fatal error occurred: Failed to connect to ESP8266”

Next, load the flash. Depending on your USB port configuration and what other peripherals you have plugged in, the ESP8266 may not be on /dev/ttyUSB0 as indicated in the esptool command line below. To check, unplug the 8266 and run 
> ls /dev/ttyUSB*

If this returns 'No such file or directory' then great, your ESP8266 is the only thing you are plugging in, so it should be easy to figure out what port it is on.

Plug in the 8266 and run the 'ls' command again, noting the difference between the USB ports mounted now. The ttyUSB* entry that is mounted after plugging in the 8266 is the one you need to use below. 

Replace 'latest-firmware.bin' with the name of the firmware you downloaded.  

>esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=8m 0 latest-firmware.bin

If this completed without complaining, congrats! You've flashed the firmware. Unplug / replug in the ESP8266 and open a terminal to test the install

####Step 4, connect to the REPL on the board
Open up a terminal and type the following, changing the USB port to the correct one for your setup:

>screen /dev/ttyUSB0 115200

You should see something like the following:

<img src='photos/repl.png'>

If not, you may need to try flashing again. Signs that I've had to reflash include errors about FAT 32 file system corruption, or fatal errors resulting in a scrolling sea of code spew. 