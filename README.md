# safe_sensor_msgs
Ros messages for the SAFE project. 
Package includes scripts and launch files for converting between SafeObstacleArray and MarkerArray (A ROS msg type used for visualization in rviz). 

#### Obj.msg
Contains x, y, z and quality

	float64 x    	# x component 
	float64 y    	# y component 
	float64 z    	# z component 
	float32 quality	# quality of the estimation

#### ObjOrientation.msg
Contains orientation and quality

	geometry_msgs/Quaternion orientation 	# Specifying orientation 
	float32 quality    			# quality of the estimation

#### SafeObject.msg
Full description of detected object 
	
	Header header
	int32 id       			# ID of the obstacle
	stringtype     			# dynamic/static, positive/negative, human/animal, heat signature, etc.
	float32 det_confidence_level 	# confidence level of the detection
	Obj obj_position
	Obj obj_lin_vel
	Obj obj_size
	ObjOrientation obj_orientation

#### SafeObjectArray.msg
Array of the SafeObject message. 

	SafeObject[] safe_objects

#### SafeSafetyAlert.msg

	Header header  			# header of the message
	int32 zone_no 			# Safety Critical Alert (based on configurable safety zones, system parameters)
	float32 confidence_level 	# confidence level of the alert
	int32 alert_severity   		# severity of the alert (e.g., warning, lift, stop, etc. )

#### SafeSensorManagement.msg

	Header header  	   # header of the message
	int32 object_id    # the ID of the object 
	int32 update_freq  # the update frequency of the message

#### SafeSensorStatus.msg

	Header header  
	int32 sensor_staus  #Error state (related to sensor diagnostics)


## Import in python
Import messages in python scripts. 

	from safe_sensor_msgs.msg import Obj,SafeObject,SafeObjectArray

## Todo and considerations
- Update the safe-protocol or update ConvertFunctions.py to actually match the safe protocol... In visaulization_msgs/Marker the position refers to the center of a visualization-shape (the center of a rectangle, cylinder etc). In the safe-protocol the rectangle is specified by (some) lower corner. PC: I definitly prefer visaulization_msgs/Marker it is less ambigious and I like that the object is specified by its center point.
- Consider merging obj_position and obj_orientation into a single geometry_msgs/pose message, however this would also require two quality values. 


## Updates since revision 5 (2017-05-09)
- SafeObject has been updated to only have one object per message (E.g. Obj[] obj_position --> Obj obj_position). SafeObjectArray is created to contain multiple SafeObjetcs. Reason: The 'float32 det_confidence_level' is not a array, so it is only possible to have one confidence_level for all the detected obstacles. Another problem with early SafeObject is that obj_position[], obj_lin_vel[] and obj_size[] could potentially have a different number of instances. 
- The ObjOrientation.msg is added as a message and in the SafeObject. Reason: The velodyne sensor is able to provide orientation of obstacles... Orientation is also added to avoid lossing information when converting between markerArray and SafeObjectArray (markerArray contains orientation information). 
- In SafeObject the 'int32 type' is changed to a string (string type). In this way each sensor may publish as many class-types as desired and merging of classes can be handled at a later stage. This also makes converting between SafeObjectArray and markerArray more convenient. (markerArray.ns = SafeObjectArray.type)
