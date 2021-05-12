import machine
import utime
potentiometer = machine.ADC(26)
while True:
    value=potentiometer.read_u16() #16bit read value
    value=value/65536
    value=3.3*value
    #print(potentiometer.read_u16())
    print(value)
    utime.sleep(2)