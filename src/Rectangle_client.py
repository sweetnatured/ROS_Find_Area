#!/usr/bin/env python

import sys
import rospy
from ros_service_assignment.srv import Ra
from ros_service_assignment.srv import RaRequest
from ros_service_assignment.srv import RaResponse

def request_rectangle_area(x, y):
    rospy.wait_for_service('rectangle_area_service')
    try:
        add_two_ints = rospy.ServiceProxy('rectangle_area_service', Ra)
        server_response = add_two_ints(x, y)
        return server_response.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting area %s*%s"%(x, y)
    s = request_rectangle_area(x, y)
    print "%s * %s = %s"%(x, y, s)
