#!/usr/bin/env python
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
import rospy

if __name__=='__main__':

	rospy.init_node('pub_circle', anonymous=True)
	
	
	move_above = Twist()
	move_above.linear.x = 2.0
	move_above.angular.z = 1.0
	
	move_below = Twist()
	move_below.linear.x =2.0
	move_below.angular.z =-1.0
	
	now = rospy.Time.now()
	
	pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size =2)
	rate = rospy.Rate(10)
	
	while rospy.Time.now() < now + rospy.Duration.from_sec(6.283185307179):
		pub.publish(move_below)
	while rospy.Time.now() < now + rospy.Duration.from_sec(12.56637061435):
		pub.publish(move_above)
