# msg_safe
Ros messages for the SAFE project. 

- Obj.msg: Containing x, y, z and quality
- SafeObject.msg: Full description of detected object 
- SafeObjectArray.msg: Array of the SafeObject message. 
- SafeSafetyAlert.msg: 
- SafeSensorManagement.msg: 
- SafeSensorStatus.msg: 

Package includes scripts and launch files for converting between SafeObstacleArray and MarkerArray (A ROS msg type used for visualization in rviz). 

#### In python
Import messages in python scripts. 

	from msg_safe.msg import Obj,SafeObject,SafeObjectArray

#### Considerations
- Using standard msgs from ros and extend with some quality measure
	- Instead of Obj position. Use geometry_msgs/pose.msg with position of type Point and orientation of type Quanternion
