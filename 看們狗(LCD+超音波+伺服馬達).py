from sensor import HC_SR04
from gpb import delay, Servo
from machine import Pin, I2C
import utime
from machine_i2c_lcd import I2cLcd    #5V  
from lcd_api import LcdApi

# 初始化HC-SR04和伺服馬達
sr04 = HC_SR04(8, 9)  # 5V
servo = Servo(5)  # 5V

# 初始化I2C
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(scl=Pin('C0'), sda=Pin('C1'), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    if sr04.Ultrasound() < 100:
        delay(500)
        servo.angle(90)
        print(str(sr04.Ultrasound()) + "cm")
        lcd.move_to(0, 0)
        lcd.putstr("Open the door ")
        delay(500)
    else:
        delay(500)
        servo.angle(-90)
        print(str(sr04.Ultrasound()) + "cm")
        lcd.move_to(0, 0)
        lcd.putstr("Close the door ")
        delay(500)
