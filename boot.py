# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
gc.collect()

from setup_lcd import *
from draw_image_from_file import *
gc.collect()
import webrepl
webrepl.start()
gc.collect()
