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

def draw_image(pic):

        row_chunk = 10
        num_rows = len(pic)
        row_groups= math.ceil(num_rows/row_chunk)
        gc.collect()
        for group_offset in range(0,row_groups-1):
                gc.collect()
                for x, row in enumerate(pic[0:row_chunk]):
                        for y, col in enumerate(row):
                                if col == '1':
                                        framebuf1.pixel(x+group_offset*row_chunk,y,1)

                gc.collect()
                lcd.data(buffer)
                pic = pic[row_chunk+1:]
                gc.collect()

