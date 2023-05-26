import sensor, image, time, lcd
from maix import KPU, utils
import machine

utils.gc_heap_size(4*256*1024)
machine.reset()
labels = ['car', 'bicycle', 'pedestrian', 'greening']

from modules import ybserial
from machine import Timer
ser = ybserial()


lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.skip_frames(time=100)
clock = time.clock()

kpu = KPU()
kpu.load_kmodel("/sd/KPU/model-50342.kmodel")


def get_result_filt(index, score):
    result_str = ''
    if True:
    #if index_mnist == 1:
    #    if score > 0.999:
    #        result_str = "num: %d" % index_mnist
    #elif index_mnist == 5:
    #    if score > 0.9995:
    #        result_str = "num: %d" % index_mnist
    #else:
        result_str = "num: %d(%s) and score: %d" % (index, labels[index], score)
    return result_str

last_number = 0
count_number = 0
count_clear = 0
MAX_COUNT = 3


car_count = 0
car_state = 0
motion_index = 0
speed_line = -0.2
speed_angular = -1.6
back_count = 22
turn_count = 22
run_end = 0
ACTION_NUM = 8

def on_timer(timer):
    global car_count
    if car_count > 0:
        car_count = car_count - 1


timer = Timer(Timer.TIMER0, Timer.CHANNEL0,
            mode=Timer.MODE_PERIODIC, period=50,
            unit=Timer.UNIT_MS, callback=on_timer, arg=None)

def camera_show():
    global car_count
    while (car_count > 0):
        img = sensor.snapshot()
        lcd.display(img)


while True:
    img = sensor.snapshot()
    #img_mnist1=img.to_grayscale(1)
    img_mnist2=img.resize(224, 224)
    img_mnist2.invert()
    img_mnist2.strech_char(1)
    img_mnist2.pix_to_ai()

    out = kpu.run_with_output(img_mnist2, getlist=True)
    max_mnist = max(out)
    index_mnist = out.index(max_mnist)
    score = KPU.sigmoid(max_mnist)
    display_str = get_result_filt(index_mnist, score)
    if len(display_str) > 0:
        img.draw_string(4,3,display_str,color=(0,0,0),scale=2)
        print(display_str)
    lcd.display(img)

kpu.deinit()
