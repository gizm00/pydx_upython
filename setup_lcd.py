from machine import Pin, HSPI
import time
import upcd8544
import framebuf

def setup_lcd():

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

	return {'lcd':lcd, 'buffer':buffer, 'framebuf1':framebuf1}
