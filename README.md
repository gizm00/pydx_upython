### The Internet of Cats - a micropython project
I wanted to learn a bit of [micropython](http://micropython.org) and a friend had an [ESP8266 micro controller](https://www.adafruit.com/product/2282) and a [Nokia 5110 LCD display](https://www.adafruit.com/product/338) I could play with. And everyone loves cats, so thus the Internet of Cats was born!

#### What the heck is an internet of cats?
The Internet of cats is an access point for 1-bit cat pictures. A (very very simple) HTTP server runs on the ESP8266, listening for requests of 'cat=somecat'  If 'somecat' is found on the device, its bitmap will be rendered on the display, like so:

<img src = 'photos/pusheen_request.png'>

#### What! Thats amazing. How to I make one?
 I'm glad you asked! Feel free to follow along with my simple [step-by-step](http://www.homestarrunner.com/sbemail58.html) instructions.

But first! Thanks to the following folks for sharing their code, this project would not have been possible without it.

<li>[upcd8544.py by Markus Birth via Mike Causer](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Conways-Game-of-Life]upcd8544.py)
<li>[convert_png.py by Gary Bake](https://github.com/garybake/upython_wemos_shields/blob/master/oled/convert_png.py)
<li>http_server.py is based on [this example](https://github.com/micropython/micropython/tree/master/examples/network) from the MicroPython repo



