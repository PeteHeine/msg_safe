#!/usr/bin/env python

import rospy

from visualization_msgs.msg import MarkerArray
from msg_safe.msg import SafeObjectArray 
from ConvertFunctions import markerArray2safeObjectArray

rospy.init_node('marker_array_2_msg_safe', anonymous=False)
nodeName = rospy.get_name()

topicVisualizeIn = rospy.get_param(nodeName+'/topicVisualizeIn', nodeName+'/ImageBBox3d')


topicMsgSafeOut = rospy.get_param(nodeName+'/topicMsgSafeOut', nodeName+'/msg_safe')

pub_msg_safe = rospy.Publisher(topicMsgSafeOut, SafeObjectArray , queue_size=0)

def callback_MarkerArray(markerArray):    
    pub_msg_safe.publish(markerArray2safeObjectArray(markerArray))
    
rospy.Subscriber(topicVisualizeIn, MarkerArray, callback_MarkerArray,queue_size=None)  
# main
def main():
    
    rospy.spin()

if __name__ == '__main__':
    main()