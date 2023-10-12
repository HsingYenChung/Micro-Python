from ble_uart import BleUart      
from machine import Pin              
from gpb import delay,LED

ble = BleUart( 0 , 115200 )                   
delay(200) 
ble.cmd_mode_entry() 
ble.cmd_AT()                          
ble.set_device_name('Mark')               
print(ble.read_device_name()) 
led = Pin ( 2, Pin.OUT) 
while True:
	delay(100)
	cmd = str(ble.read(30), 'utf-8').strip('\0') # 將讀取回來值文字後面塞的\0刪除    
	if cmd != '':   
		print(cmd) 
		if cmd == 'on': 
			led.on() 
			ble.write('LED ON') 
		elif cmd == 'off': 
			led.off() 
		ble.write('LED OFF') 
delay(100)
