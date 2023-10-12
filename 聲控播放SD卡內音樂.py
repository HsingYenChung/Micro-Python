import audio_decode,audio_encode,voice_recognition
from machine import Pin
from gpb import LED,delay

audio_decode.init()
audio_encode.init()

voice_recognition.load_database( 'tinkaVR.bin' ) 
delay(500)

voice_recognition.start(10)

while True:                   
    cmd_id =voice_recognition.get_id()
    if cmd_id == 9:        #播放音樂             
        print("start!")
        audio_decode.start('BLACKPINK.mp3')
        
    elif cmd_id == 10:   #增加音量
        audio_decode.volume_up(2)
        print("volume up!")
        
    elif cmd_id == 11:  #降低音量
        audio_decode.volume_down(2)
        print("volume down!")

    elif cmd_id == 12:    #停止音樂          
        audio_decode.stop()
        print("stop!")

        #audio_decode.pause()
        #audio_decode.resume()

