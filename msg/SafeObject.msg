Header header
int32      id       #ID of the obstacle
int32      type     # dynamic/static, positive/negative, human/animal, heat signature, etc.
float32    det_confidence_level   #confidence level of the detection
Obj[]      obj_position
Obj[]      obj_lin_vel
Obj[]      obj_size