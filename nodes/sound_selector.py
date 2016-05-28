#!/usr/bin/python

import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

Soundhandle = SoundClient()

def say_message(string_message):
	global Soundhandle

	object_seen = string_message.data
	sound = Soundhandle.voiceSound(object_seen)
	print "Saying '",object_seen,"'"
	sound.play()

def sound_selector():
	rospy.init_node('sound_selector', anonymous=True)
	rospy.Subscriber("/caffe_best", String, say_message)
	rospy.spin()

if __name__ == '__main__':
    print "Running sound_selector node."
    try:
        sound_selector()
    except rospy.ROSInterruptException:
        pass

