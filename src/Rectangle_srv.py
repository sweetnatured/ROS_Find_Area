#!/usr/bin/env python

from ros_service_assignment.srv import Ra
from ros_service_assignment.srv import RaRequest
from ros_service_assignment.srv import RaResponse

import rospy

def rectangle_area_callback(req):
    print "Returning [%s * %s = %s]"%(req.a, req.b, (req.a * req.b))
    return RaResponse(req.a * req.b)

def rectangle_area_server():
    rospy.init_node('rectangle_area_server_node')
    s = rospy.Service('rectangle_area_service', Ra, rectangle_area_callback)
    print "Ready to find area."
    rospy.spin()
    
if __name__ == "__main__":
    rectangle_area_server()
