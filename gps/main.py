from twist_controller import Controller
import rospy

def main():
    master_control = Controller()
    Throttle, Brake, Steering, start_time = master_control.control(20,15,10,0)
    print(Throttle,Brake,Steering)
    Throttle, Brake, Steering, start_time = master_control.control(0,15,10,3)
if __name__ == "__main__":
    main()
