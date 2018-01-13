import snowboydecoder #hotword
import mraa 
import time 

#initialize gpio 23
gpio_1 = mraa.Gpio(23)

#set gpio 23 to output
gpio_1.dir(mraa.DIR_OUT)

def detected_callback():
    print "hotword detected"
    #sends signal to arduino to make motor move for 2 seconds
    gpio_1.write(1)
    time.sleep(2)
    gpio_1.write(0)

detector = snowboydecoder.HotwordDetector("Hey_Potato.pmdl", sensitivity = 0.6, audio_gain = 1)

detector.start(detected_callback)
