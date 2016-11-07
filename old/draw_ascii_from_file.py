def draw_image(file_name):

	gc.collect()
	y = 0
	with open(file_name) as f:
		for line in f:
			y=0
			framebuf1.text(line,y,0)
			gc.collect()
			y = y+1

		gc.collect()
		print('sending to lcd')
    		lcd.data(buffer)
		gc.collect()
