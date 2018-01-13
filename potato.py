import snowboydecoder

def detected_callback():
    print "hotword detected"

detector = snowboydecoder.HotwordDetector("Hey_Potato.pmdl", sensitivity = 0.6, audio_gain = 1)

detector.start(detected_callback)
