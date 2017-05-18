#!/usr/bin/env python

import rospy

from visualization_msgs.msg import MarkerArray
from safe_sensor_msgs.msg import SafeObjectArray 
from ConvertFunctions import safeObjectArray2markerArray

rospy.init_node('msg_safe_2_marker_array_', anonymous=False)
nodeName = rospy.get_name()

topicMsgSafeIn = rospy.get_param(nodeName+'/topicMsgSafeIn', nodeName+'/msg_safe')
topicVisualizeOut = rospy.get_param(nodeName+'/topicVisualizeOut', nodeName+'/ImageBBox3d')

pub_marker_array = rospy.Publisher(topicVisualizeOut, MarkerArray , queue_size=0)

def callback_SafeObjectArray(safeObjectArray):   
    # Converts safe-message (SafeObjectArray) to visualization-marker (MarkerArray).
    pub_marker_array.publish(safeObjectArray2markerArray(safeObjectArray))
    
rospy.Subscriber(topicMsgSafeIn, SafeObjectArray, callback_SafeObjectArray,queue_size=None)  
# main
def main():
    
    rospy.spin()

if __name__ == '__main__':
    main()
