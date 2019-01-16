#!/usr/bin/env python
import rospy #needed for all ROS Node
from std_msgs.msg import String #allows reuse of std_msgs/String message type for publishing.

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
		#declares that your node is publishing to the chatter topic using the message type 
		#String. String here is actually the class std_msgs.msg.String. 
		
    rospy.init_node('talker', anonymous=True)
		#tells rospy the name of your node. This is important since until rospy has this 
		#information, it cannot communicate with the Master. Here, the node name is, talker.
		
    rate = rospy.Rate(10) #10Hz - loop at the rate. With 10Hz, we should expect to go through the loop 10 times per second
    while not rospy.is_shutdown(): #check is_shutdown() to see if your program should exit (e.g. if there is a Ctrl-C etc).
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
	#rospy.ROSInterruptException exception, thrown by rospy.sleep() and rospy.Rate.sleep() when Ctrl-C is pressed 
	#or your Node is otherwise shutdown. This happens so code does not execute after the sleep().