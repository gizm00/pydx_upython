import usocket as socket
import gc


CONTENT = b"""\
HTTP/1.0 200 OK
Hello #%d from MicroPython!
"""

def main():
    s = socket.socket()

    # Binding to all interfaces - server will be accessible to other hosts!
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    print("Bind address info:", ai)
    addr = ai[0][-1]
    gc.collect()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<this_host>:8080/")
    gc.collect()

    counter = 0
    while True:
	gc.collect()
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_sock)
	client_stream = client_sock
	lcd_cat = ""
	print("Request:")
	req = client_stream.readline()
	print(req)
        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
            
            if str(h).find('GET /cat=pusheen'):
		print("drawing Pusheen")
                lcd_cat = 'cats/smoosheen.txt'
		break
            if str(h).find('GET /cat=sitting'):
		print("drawing sitting cat")
                lcd_cat = 'sitting_cat.txt'
                break


            print(h)
	draw_image(lcd_cat, framebuf1, buffer, lcd)
        client_stream.write(CONTENT % counter)
        client_stream.close()
	client_sock.close()
	counter += 1
	print()

def poll():
    while True:
        gc.collect()
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_sock)
        client_stream = client_sock

        print("Request:")
        req = client_stream.readline()
        print(req)
        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
            print(h)
        client_stream.write(CONTENT % counter)

        client_stream.close()
        client_sock.close()
	counter += 1
