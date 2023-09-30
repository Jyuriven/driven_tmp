from twist_controller import Controller
import rospy
import time

def main():
	rospy.init_node('rosout') 	
	master_control = Controller()
	while True:
		Throttle, Brake, Steering = master_control.control(10, 10, 25.0, 0)
		print(Throttle,Brake,Steering)
		time.sleep(1)
	'''
	Throttle, Brake, Steering = master_control.control(0, 10, 0, 0)
	print(Throttle,Brake,Steering)
	Throttle, Brake, Steering = master_control.control(10, 10, 3, 0)
	print(Throttle,Brake,Steering)
	'''
if __name__ == "__main__":
    main()
