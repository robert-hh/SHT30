# Readme

This is a copy of a repository of Roberto Sánchez at 
https://github.com/rsc1975/micropython-sht30.
The scripts are only changed to adapt it for using machine.I2C for
the interface, and removing some obsolete characters.

Sample usage of the driver:

    from machine import I2C, Pin
    import sht30

    i2c=I2C(0, sda=Pin(4), scl=Pin(5))
    sht=sht30.SHT30(i2c=i2c, i2c_address=68)

    sht.measure()


Note: The Apache license is that of the initial author. Personally
I prefer MIT.