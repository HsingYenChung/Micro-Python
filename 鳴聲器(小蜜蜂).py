from machine import PWM 
from gpb import delay 
buzzer = PWM( 7 , duty=1000 )

tones = { 
"A0" : 28, 
"AS0" : 29, 
"B0" : 31,
"A4": 440, 
"AS4": 466, 
"B4": 494, 
"C5": 523, 
"CS5": 554, 
"D5": 587, 
"DS5": 622, 
"E5": 659, 
"F5": 698, 
"FS5": 740, 
"G5": 784, 
"GS5": 831, 
"A5": 880, 
"AS5": 932, 
"B5": 988,
"C6": 1046, 
"D6": 1175,
"E6": 1319,
"F6": 1397,
"G6": 1568,
}

song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"] 
 
littleBee_song = ["G5", "E5", "E5", "P", "F5", "D5", "D5", "P", "C5", "D5", "E5", "F5", "G5", "G5", "G5", "P", 
                  "G5", "E5", "E5", "P", "F5", "D5", "D5", "P", "C5", "E5", "G5", "G5", "E5", "P", "P", "P", 
                  "D5", "D5", "D5", "D5", "D5", "E5", "F5", "P", "E5", "E5", "E5", "E5", "E5", "F5", "G5", "P", 
                  "G5", "E5", "E5", "P", "F5", "D5", "D5", "P", "C5", "E5", "G5", "G5", "C5", "P", "P", "P"] 
 
littleStar_song = ["C5", "C5", "G5", "G5", "A5", "A5","G5", "P", "F5", "F5", "E5", "E5", "D5", "D5", "C5", "P", 
                  "G5", "G5", "F5", "F5", "E5", "E5", "D5", "P","G5", "G5", "F5", "F5", "E5", "E5", "D5", "P", 
                  "C5", "C5", "G5", "G5", "A5", "A5", "G5","P", "F5", "F5", "E5", "E5", "D5", "D5", "C5", "P"] 
 
Birthday_song = ["G5", "G5", "A5", "G5", "C6","B5","P",
                 "G5","G5","A5","G5", "D6","C6", "P",
                 "G5", "G5", "G6", "E6", "C6", "B5", "A5", "P", 
                  "F6", "F6", "E6", "C6", "D6", "C6","P"] 

def playtone(frequency): 
    buzzer.duty(1000) 
    buzzer.freq(frequency) 
def bequiet(): 
    buzzer.duty(0) 
    delay(200) 
def playsong(mysong): 
    for i in range(len(mysong)): 
        if (mysong[i] == "P"): 
            bequiet() 
        else: 
            playtone(tones[mysong[i]]) 
            delay(300) 
    bequiet()
    
playsong(Birthday_song)

# print([Birthday_song[8]])
# print(tones[Birthday_song[8]])