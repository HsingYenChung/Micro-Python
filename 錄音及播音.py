from machine import Pin 
import audio_decode,audio_encode 
from gpb import delay 
led = Pin( 3 ,Pin.OUT) 
audio_decode.init() 
audio_encode.init() 
def recode(): 
	audio_encode.start('record.wav') 
	led.on() #燈亮開始講話 
	delay(5000) 
	led.off() #燈暗停止錄音 
	audio_encode.stop() 
recode() 
delay(1000) 
audio_decode.start('record.wav') 