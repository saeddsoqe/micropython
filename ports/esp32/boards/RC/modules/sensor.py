# Dev by Sonthaya Nongnuch
# Edited and Modified by Saeed Desouky
from machine import Pin, I2C, ADC

LM73_ADDR = const(0x4D)
MAX_VALUE = const(800)
MIN_VALUE = const(200)

def light():
    adc = ADC(Pin(34))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    value = int(100 - ((adc.read() - MIN_VALUE) / (MAX_VALUE - MIN_VALUE) * 100))
    value = 100 if value > 100 else value
    value = 0 if value < 0 else value
    return value

def temperature():
    i2c1 = I2C(1, scl=Pin(5), sda=Pin(4), freq=100000)
    data = i2c1.readfrom_mem(LM73_ADDR, 0x00, 2)
    temp = (((data[0] & 0x7F) << 8)| data[1]) >> 5
    temp = temp * 0.25
    temp = temp * (-1 if (data[0] & 0x80) != 0 else 1)
    return temp
