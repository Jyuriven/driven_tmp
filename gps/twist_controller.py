import rospy
from pid import PID
from yaw_controller import YawController
class Controller(object):
    def __init__(self, vehicle_mass=220,  decel_limit=0, accel_limit=5,
                 wheel_radius=505, wheel_base=1320, steer_ratio=0.151, max_lat_accel=5, max_steer_angle=27):

        self.yaw_controller = YawController(wheel_base, steer_ratio, 0.1, max_lat_accel, max_steer_angle)
        kp = 0.3
        ki = 0.1
        kd = 0.0
        min_throttle = 0.0
        max_throttle = 0.2
        self.throttle_controller = PID(kp, ki, kd, min_throttle, max_throttle)
        self.vehicle_mass = vehicle_mass
        self.decel_limit = decel_limit
        self.accel_limit = accel_limit
        self.wheel_radius = wheel_radius
	last_time = rospy.get_time()
        last_vel = 0.0

	def control(self, current_vel, linear_vel, angular,brake):
	    vel_error = linear_vel - current_vel
	    self.last_vel = current_vel

	    current_time = rospy.get_time()
	    sample_time = current_time - self.last_time

	    throttle = self.throttle_controller.step(vel_error, sample_time)

	    print("Jetson2Ardu Control DATA : ")
	    print("Jetson2Ardu Control DATA ( THROTTLE ) : %d",throtle )
	    print("Jetson2Ardu Control DATA ( BRAKE ) : %f", brake)
	    print("Jetson2Ardu Control DATA ( STEERING ) : %f", steering )

	    return throttle, brake, steering
