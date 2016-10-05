from machine import Pin, SPI
import gc
import upcd8544

gc.collect()

import framebuf
import math

gc.collect()

#spi = HSPI(baudrate=80000000, polarity=0, phase=0)
spi = SPI(-1,baudrate=200000, polarity=0, phase=0, sck=Pin(0), mosi=Pin(1), miso=Pin(4))  
RST = Pin(3)
#CE = Pin(5)
DC = Pin(2)
#BL = Pin(16)
lcd = upcd8544.PCD8544(spi, RST, DC)

width = 84
height = 48
pages = height // 8
buffer = bytearray(pages * width)
framebuf1 = framebuf.FrameBuffer1(buffer, width, height)

gc.collect()
