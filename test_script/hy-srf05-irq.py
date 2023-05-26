
import utime
from maix import I2S, GPIO
from board import board_info
from fpioa_manager import fm
import audio

time_us = [0 for i in range(4)]

def irq_decorator(name, index):
    global time_us
    #name, index = func()
    time_us[index] = utime.ticks_us()
    diff = time_us[index] - time_us[index - 1] if index else time_us[0] - time_us[3]
    print("{}: [irq]{} callback cost {} us".format(utime.ticks_us(), name, diff))

#@irq_decorator
def echo_irq(pin):
    irq_decorator("echo_rising", 0) if pin.value() else irq_decorator("echo_falling", 1)
#@irq_decorator
def out_irq(pin):
    irq_decorator("out_rising", 3) if pin.value() else irq_decorator("out_falling", 2)

# See <https://wiki.sipeed.com/soft/maixpy/zh/api_reference/Maix/fpioa.html>
fm.unregister(fm.fpioa.GPIOHS13)
fm.unregister(fm.fpioa.GPIOHS14)
fm.unregister(fm.fpioa.GPIOHS15)
fm.register(1,fm.fpioa.GPIOHS13)
fm.register(2,fm.fpioa.GPIOHS14)
fm.register(3,fm.fpioa.GPIOHS15)
hy_trig=GPIO(GPIO.GPIOHS13, GPIO.OUT)
hy_echo=GPIO(GPIO.GPIOHS14, GPIO.IN, GPIO.PULL_DOWN)
hy_out=GPIO(GPIO.GPIOHS15, GPIO.IN, GPIO.PULL_DOWN)
hy_trig.value(0)

hy_echo.irq(echo_irq, GPIO.IRQ_BOTH, priority=6)#, GPIO.WAKEUP_NOT_SUPPORT)
hy_out.irq(out_irq, GPIO.IRQ_BOTH, priority=6)#, GPIO.WAKEUP_NOT_SUPPORT)

while True:
    utime.sleep_ms(100)
    hy_trig.value(1)
    print("{}: trig 1".format(utime.ticks_us()))
    #continue
    utime.sleep_us(15)
    hy_trig.value(0)
    print("{}: trig 0".format(utime.ticks_us()))

