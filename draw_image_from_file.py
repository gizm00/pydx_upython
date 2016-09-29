import gc
def draw_image(file_name, framebuf1, buffer, lcd):

	gc.collect()
	x = 0
	y = 0
	with open(file_name) as f:
		for line in f:
			y=0
			for char in line:
				if char == '0':
					#print('x,y' + str(x) + ',' + str(y))
					framebuf1.pixel(y,x,1)
					gc.collect()
				y = y+1
			x = x+1

		gc.collect()
		print('sending to lcd')
    		lcd.data(buffer)
		gc.collect()
