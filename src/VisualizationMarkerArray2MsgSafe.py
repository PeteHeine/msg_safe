#!/usr/bin/env python

import rospy

from visualization_msgs.msg import Marker, MarkerArray
from msg_safe.msg import Obj,SafeObject,SafeObjectArray 
from ConvertFunctions import marker2msgSafe

rospy.init_node('marker_array_2_msg_safe', anonymous=False)
nodeName = rospy.get_name()

topicVisualizeIn = rospy.get_param(nodeName+'/topicVisualizeIn', nodeName+'/ImageBBox3d')


topicMsgSafeOut = rospy.get_param(nodeName+'/topicMsgSafeOut', nodeName+'/msg_safe')

pub_msg_safe = rospy.Publisher(topicMsgSafeOut, SafeObjectArray , queue_size=0)

def callback_MarkerArray(markerArray):
    
    safeObjects = SafeObjectArray()
    for marker in markerArray.markers:
        # For visualization a dummie markers with deleteall. This needs to be skipped. 
        if marker.action is not marker.DELETEALL:
            safeObjects.safe_objects.append(marker2msgSafe(marker))            

    
    pub_msg_safe.publish(safeObjects)
    
rospy.Subscriber(topicVisualizeIn, MarkerArray, callback_MarkerArray,queue_size=None)  
# main
def main():
    
    rospy.spin()

if __name__ == '__main__':
    main()