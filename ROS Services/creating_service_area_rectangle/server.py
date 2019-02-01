#!/usr/bin/env 

import ros_service_assignment.srv from RectangleAreaService
import ros_service_assignment.srv from RectangleAreaServiceRequest
import ros_service_assignment.srv from RectangleAreaServiceResponse

import rospy

def handle_rectangle_area(req):
	print "The area of the rectangle is [%s + %s = %s]" %(req.width, req.height, (req.width * req.height))
	return RectangleAreaResponse(req.width * req.height) # send back response to the client

def rectangle_area_server():
	rospy.init_node('rectangle_area_server')
	s = rospy.Service('rectangle_area_service', RectangleAreaService, handle_rectangle_area)
	print "ready to calculate area"
	rospy.spin()

if __name__ == "__main__":
	rectangle_area_server()

