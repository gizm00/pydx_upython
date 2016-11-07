


### The Internet of Cats - a micropython project
I wanted to learn a bit of [micropython](http://micropython.org) and a friend had an [ESP8266 micro controller](https://www.sparkfun.com/products/13678) and a [Nokia 5110 LCD display](https://www.sparkfun.com/products/10168) I could play with. And everyone loves cats, so thus the Internet of Cats was born!

#### What the heck is an internet of cats?
The Internet of cats is an access point for 1-bit cat pictures. A (very very simple) HTTP server runs on the ESP8266, listening for requests of 'cat=somecat'  If 'somecat' is found on the device, its bitmap will be rendered on the display, like so:

<img src = 'photos/pusheen_request.png'>

#### What! Thats amazing. How to I make one?
 I'm glad you asked! Feel free to follow along with my simple [step-by-step](http://www.homestarrunner.com/sbemail58.html) instructions.

But first! Thanks to the following folks for sharing their code and how-tos. This project would not have been possible without them.

<li>[Instructions for connecting the ESP-01 to the Nokia 5110 rom Kendrick Tabi](https://www.kendricktabi.com/2015/08/esp8266-and-nokia-5110-lcd.html)
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

For the ESP-12, the following setup is required to flash the device. Namely, you need to ground GPIO0 and GPIO5. Make sure CH_PD is high.
<img src='photos/esp12_firmware_flash.png'>
This photo is from [agcross.com](http://www.agcross.com/2015/09/the-esp8266-wifi-chip-part-3-flashing-custom-firmware)


