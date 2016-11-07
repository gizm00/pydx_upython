from machine import Pin, HSPI
import gc
import time
import upcd8544

gc.collect()

import framebuf
import math

gc.collect()

spi = HSPI(baudrate=80000000, polarity=0, phase=0)
RST = Pin(4)
CE = Pin(5)
DC = Pin(12)
BL = Pin(16)
lcd = upcd8544.PCD8544(spi, RST, CE, DC, BL)

width = 84
height = 48
pages = height // 8
buffer = bytearray(pages * width)
framebuf1 = framebuf.FrameBuffer1(buffer, width, height)

gc.collect()

def draw_image(file_name):

        gc.collect()
        x = 0
        y = 0
        with open(file_name) as f:
                for line in f:
                        y=0
                        for char in line:
                                if char == '0':
                                        print('x,y' + str(x) + ',' + str(y))
                                        framebuf1.pixel(y,x,1)
                                        gc.collect()
                                y = y+1
                        x = x+1

                gc.collect()
                print('sending to lcd')
                lcd.data(buffer)
                gc.collect()
