#!/usr/bin/env python

import sys
import rospy
from ros_service_assignment.srv import RectangleArea
from ros_service_assignment.srv import RectangleAreaRequest
from ros_service_assignment.srv import RectangleAreaResponse

def request_rectangle_area(x, y):
    rospy.wait_for_service('rectangle_area_service')
    try:
        add_two_ints = rospy.ServiceProxy('rectangle_area_service', RectangleArea)
        server_response = add_two_ints(x, y)
        return server_response.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
