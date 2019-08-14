import sensor, image, time
from pyb import UART
import binascii

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.B128X128)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

def int_to_byte(integer):
    hex_string = '{:02x}'.format(integer)
    a_byte = binascii.unhexlify(hex_string)
    return a_byte


def byte_to_int(a_byte):
    if (a_byte == None):
        return 0

    hex_string = binascii.hexlify(a_byte)
    integer = int(hex_string, 16)
    return integer

uart = UART(3, 115200, timeout=5) #P4/P5 = TX/RX

i = 0
while(True):
    clock.tick()
    #img = sensor.snapshot().lens_corr(1.8)

    uart.write(int_to_byte(i))
    a_byte = uart.read(1)
    print(byte_to_int(a_byte))

    #print(i)
    i += 1
    if i > 255:
        i = 0
