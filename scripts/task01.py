#!/usr/bin/env python

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
import rospy


# varx = 5.544444561004639
# vary = 5.544444561004639
c = 0

def callback(msg):
	# global varx
	# global vary
	# pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size =1)
	# move = Twist()
	# rate = rospy.Rate(1)
	# pub.publish(move)
	global c 


	varx = msg.x
	vary = msg.y

	if varx == 5.544444561004639 and c == 2:
		rospy.loginfo("Bau")
		
	if varx == 5.544444561004639 and c == 0:
		c+=1	
		move.linear.x = 1.0
		move.angular.z = -1.0
		rospy.loginfo("Bau1")
		pub.publish(move)
		
	if varx ==5.544444561004639 and c ==1:
		move.linear.x = 1.0
		move.angular.z = 1.0
		c+=1
		rospy.loginfo("Bau2")
		pub.publish(move)
		
	pub.publish(move)
	
	rospy.loginfo(varx)
	rate.sleep()

# if __name__=='__main__':

rospy.init_node('Buuger')
sub = rospy.Subscriber("turtle1/pose",Pose ,callback)
pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size =1)
rate = rospy.Rate(10)
move = Twist()	


# rate.sleep()
rospy.spin()