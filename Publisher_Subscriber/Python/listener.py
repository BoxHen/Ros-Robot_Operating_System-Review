#!/usr/bin/env python
import rospy
from std_msgs.msg import String #allows reuse of std_msgs/String message type for publishing.

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
	#The anonymous keyword argument is  used for nodes where you normally expect many of them to be running 
	#and don't care about their names (e.g. tools, GUIs). It adds a random number to the end of your node's 
	#name, to make it unique. Unique names are more important for nodes like drivers, where it is an error 
	#if more than one is running. If two nodes with the same name are detected on a ROS graph, the older node is shutdown.
	
    rospy.Subscriber("chatter", String, callback)
	
    rospy.spin()
	#keeps your node from exiting until the node has been shutdown. Unlike roscpp, rospy.spin() does not affect the subscriber 
	#callback functions, as those have their own threads.
	

if __name__ == '__main__':
    listener()