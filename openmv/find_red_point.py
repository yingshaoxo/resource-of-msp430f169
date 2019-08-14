import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot().lens_corr(1.8)
    red_blobs = img.find_blobs([(65, 95, 10, 45, -20, 12)])
    for blob in red_blobs:
        img.draw_rectangle(blob[0:4], color=(0,255,0), thickness=4)
        img.draw_cross(blob[5], blob[6]) # center_x, center_y
    print("FPS %f" % clock.fps())
