import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.B128X128)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

width = 90
height = 120
sub_image_number_in_one_axis = 16

def get_sub_image_paramaters():
    list_for_y_axis = []
    y_value = 0
    y_interval = height//sub_image_number_in_one_axis
    for yi in range(sub_image_number_in_one_axis):
        list_for_x_axis = []
        x_value = 0
        x_interval = width//sub_image_number_in_one_axis
        for xi in range(sub_image_number_in_one_axis):
            region_of_interest = (x_value, y_value, x_interval, y_interval)
            x_value += x_interval
            list_for_x_axis.append(region_of_interest)
        y_value += y_interval
        list_for_y_axis.append(list_for_x_axis)

    return list_for_y_axis

def get_sub_image_center_points():
    list_for_y_axis = []
    y_value = 0
    y_interval = height//sub_image_number_in_one_axis
    half_y_interval = y_interval//2
    for yi in range(sub_image_number_in_one_axis):
        list_for_x_axis = []
        x_value = 0
        x_interval = width//sub_image_number_in_one_axis
        half_x_interval = x_interval//2
        for xi in range(sub_image_number_in_one_axis):
            region_of_interest = (x_value + half_x_interval, y_value + half_y_interval)
            x_value += x_interval
            list_for_x_axis.append(region_of_interest)
        y_value += y_interval
        list_for_y_axis.append(list_for_x_axis)

    return list_for_y_axis

sub_image_crop_paramater_list = get_sub_image_paramaters()
def detect_a_sub_image(an_image):
    list_for_y_axis = []
    for yi in range(sub_image_number_in_one_axis):
        list_for_x_axis = []
        for xi in range(sub_image_number_in_one_axis):
            crop_paramater = sub_image_crop_paramater_list[yi][xi]
            sub_image = an_image.copy(roi=crop_paramater)
            blobs = sub_image.find_blobs([(58, 100, -128, 127, -128, 127)])
            true_or_false = 1
            for blob in blobs:
                if blob.pixels() > 1:
                    true_or_false = 0
            list_for_x_axis.append(true_or_false)
        list_for_y_axis.append(list_for_x_axis)
    return list_for_y_axis

detected_point_list = []
sub_image_center_point_list = get_sub_image_center_points()
def print_out_points(an_image):
    list_for_y_axis = []
    for yi in range(sub_image_number_in_one_axis):
        list_for_x_axis = []
        for xi in range(sub_image_number_in_one_axis):
            point = sub_image_center_point_list[yi][xi]
            if (detected_point_list[yi][xi] == 1):
                an_image.draw_circle(point[0], point[1], 3, color=(255, 0, 0), fill=True)
            else:
                an_image.draw_circle(point[0], point[1], 3, color=(0, 255, 0), fill=True)
            #an_image.draw_cross(point[0], point[1], color=(0, 255, 0)) # center_x, center_y
        list_for_y_axis.append(list_for_x_axis)
    return an_image


while(True):
    clock.tick()
    img = sensor.snapshot().lens_corr(1.8)

    detected_point_list = detect_a_sub_image(img)
    img = print_out_points(img)

    #red_blobs = img.find_blobs([(59, 75, -15, 8, -27, -2)])
    #for blob in red_blobs:
        #img.draw_rectangle(blob[0:4], color=(0,255,0), thickness=4)
        #img.draw_cross(blob[5], blob[6]) # center_x, center_y

    #print("FPS %f" % clock.fps())
