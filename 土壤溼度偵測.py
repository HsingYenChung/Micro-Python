from machine import ADC 
from gpb import delay 
soil = ADC(1)

for i in range(100):
	print ("thirst!"+str(soil.read()))
	delay(2000)
# while True: 
# 	if soil.read() < 500: 
# 		print ("thirst!"+str(soil.read())) 
# 		delay(1000) 
