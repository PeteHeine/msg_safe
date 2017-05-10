# msg_safe
Ros messages for the SAFE project. 
Package includes scripts and launch files for converting between SafeObstacleArray and MarkerArray (A ROS msg type used for visualization in rviz). 

#### Obj.msg
Containing x, y, z and quality

	float64 x    	# x component 
	float64 y    	# y component 
	float64 z    	# z component 
	float32 quality	# quality of the estimation

#### SafeObject.msg
Full description of detected object 
	
	Header header
	int32 id       			# ID of the obstacle
	int32 type     			# dynamic/static, positive/negative, human/animal, heat signature, etc.
	float32 det_confidence_level 	# confidence level of the detection
	Obj obj_position
	Obj obj_lin_vel
	Obj obj_size

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

	from msg_safe.msg import Obj,SafeObject,SafeObjectArray

## Todo and considerations
- Update the safe-protocol or update ConvertFunctions.py to actually match the safe protocol... In visaulization_msgs/Marker the position refers to the center of a visualization-shape (the center of a rectangle, cylinder etc). In the safe-protocol the rectangle is specified by (some) lower corner. PC: I definitly prefer visaulization_msgs/Marker it is less ambigious and I like that the object is specified by its center point.
- Using standard msgs from ros and extend with some quality measure
	- Instead of Obj position. Use geometry_msgs/pose.msg with position of type Point and orientation of type Quanternion
- Test
