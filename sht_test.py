from machine import I2C, Pin
import sht30

i2c=I2C(0, sda=Pin(4), scl=Pin(5))
sht=sht30.SHT30(i2c=i2c, i2c_address=68)

sht.measure()
