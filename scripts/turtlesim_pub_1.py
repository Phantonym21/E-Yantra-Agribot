#!/usr/bin/env python

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
import rospy

varx = None
vary = None
c = 0
e = 0

def callback(data):

	global varx
	global vary
	varx = data.x
	vary = data.y

	rospy.loginfo(varx)

if __name__=='__main__':
	# global c

	rospy.init_node('Buuger',anonymous = True)

	# move = Twist()


	move1 = Twist()
	move1.linear.x = 2.0
	move1.angular.z = -1.0

	move2 = Twist()
	move2.linear.x = 2.0
	move2.angular.z = -1.0

	move3 = Twist()
	move3.linear.x = 0.0
	move3.angular.z = 0.0

	sub = rospy.Subscriber("turtle1/pose",Pose ,callback)
	pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size =1)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		# if varx == None:
		# 	c+=1
		# 	move.linear.x = 2.0
		# 	move.angular.z = -1.0
		# 	rospy.loginfo("Bau1")
		# elif varx == 5.544444561004639 and c==1:
		# 	c+=1
		# 	move.linear.x =2.0
		# 	move.angular.z = 1.0
		# 	rospy.loginfo("Bau2")
		# elif varx == 5.544444561004639 and c==2:
		# 	move.linear.x =0.0
		# 	move.angular.z = 0.0
		# 	rospy.loginfo("Bau3")	

		if varx  == 5.544444561004639 and c==0:
			e = 1
			c+=1
			rospy.loginfo("Bau1")
		elif varx == 5.544444561004639 and c==1:
			e = 2
			c+=1
			rospy.loginfo("Bau2")
		elif varx == 5.544444561004639 and c==2:
			e = 3
			rospy.loginfo("Bau3")


		if e == 1:
			pub.publish(move1)
			rospy.loginfo("Bau4")
		elif e == 2:
			pub.publish(move2)	
			rospy.loginfo("Bau5")
		else:
			pub.publish(move3)
			rospy.loginfo("Bau6")

		rate.sleep()	

		# pub.publish(move)
		# rate.sleep()	