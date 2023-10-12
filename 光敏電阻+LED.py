from machine import ADC
#光強阻抗小，光弱阻抗大
#3.3V
from gpb import delay, LED

light=ADC(0)
led=LED(1)

while True:
	if light.read() >= 3000:
		led.on()
		print(light.read())
		
	else:
		led.off()
		delay(50)
	print(light.read()) 
	delay(100)
	
