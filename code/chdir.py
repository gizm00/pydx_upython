# for moving files around on the ESP8266

def chfiledir(file_in, file_out):
	with open(file_in) as fin:
		data = fin.read()
		fout = open(file_out, 'w')
		fout.write(data)
		fout.close()
