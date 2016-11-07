import usocket as socket
import gc
from draw_image_from_file import *

CONTENT = b"""\
HTTP/1.0 200 OK
Hello #%d from MicroPython!
"""

def main(framebuf1, buffer1, lcd):
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
        lcd_whale = ""
        print("Request:")
        req = client_stream.readline()
        req = str(req)
        print(req)
        if req.find('GET /cat=sitting') > 0:
            lcd_cat = 'sitting_cat.txt'
        if req.find('GET /cat=smoosheen') > 0:
            lcd_cat = 'smoosheen.txt'
        if req.find('GET /cat=totoro') > 0:
            lcd_cat = 'totoro.txt'
        if req.find('GET /cat=hello') > 0:
            lcd_cat = 'hello_kitty.txt'
        if req.find('GET /cat=upython') > 0:
            lcd_cat = 'upython_logo.txt'
        if req.find('GET /cat=nyan') > 0:
            lcd_cat = 'nyan_cat.txt'
        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
            print(h)

        print("writing to client")
        client_stream.write(CONTENT % counter)

        client_stream.close()

        if len(lcd_cat) > 0:
            lcd_cat = 'cats/' + lcd_cat
            print("sending cat to LCD")
            print("lcd cat: " + str(lcd_cat))
            draw_image(lcd_cat, framebuf1, buffer1, lcd)
        counter += 1
        print()


#main()
