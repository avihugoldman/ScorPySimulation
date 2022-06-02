
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
import threading
import time

from Point import Point
from controller import Robot, Motor

# TIME_STEP = 64

MAX_SPEED = 6.28

BASE_SPEED = 0

MOVEMENT_VELOCITY = 0.1

# create the Robot instance.
robot = Robot()


# get the time step of the current world.
TIME_STEP = int(robot.getBasicTimeStep())
joint_map = {0: "Base2Body_Rot", 1: "Body2Arm_Rot", 2: "Lower2Upper_Rot", 3: "grip_pitch", 4: "rot_grip"}
sensor_map = {0: "Base2Body_Sen", 1: "Body2Arm_Sen", 2: "Lower2Upper_Sen", 3: "grip_pitch_Sen", 4: "rot_grip_Sen"}
xyz_map = {0: "x", 1: "y", 2: "z"}

class SimRobot(Robot):
    
    def __init__(self):
        super(Robot, self).__init__()
        self._motion_status = False
        self._is_home = True
        self._enable_movement = True
        self._points: dict[int: Point] = {}
        self.cam = robot.getDevice('web_cam')
        self.cam.enable(TIME_STEP)
        
        self.gps = robot.getDevice("Scrobot_GPS")
        self.gps.enable(TIME_STEP)
        
        self.base_body_mt = robot.getDevice('Base2Body_Rot')
        self.base_body_sen = robot.getDevice('Base2Body_Sen')
        self.base_body_sen.enable(TIME_STEP)
        
        self.shoulder_mt = robot.getDevice('Body2Arm_Rot')
        self.shoulder_sen = robot.getDevice('Body2Arm_Sen')
        self.shoulder_sen.enable(TIME_STEP)

        self.elbow_mt = robot.getDevice('Lower2Upper_Rot')
        self.elbow_sen = robot.getDevice('Lower2Upper_Sen')
        self.elbow_sen.enable(TIME_STEP)

        self.grip_mt = robot.getDevice('grip_pitch')
        self.grip_sen = robot.getDevice('grip_pitch_Sen')
        self.grip_sen.enable(TIME_STEP)
        
        self.roll_grip_mt = robot.getDevice('rot_grip')
        self.roll_grip_sen = robot.getDevice('rot_grip_Sen')
        self.roll_grip_sen.enable(TIME_STEP)
        
        self.grip_right_arm_mt = robot.getDevice('Right_arm')
        self.grip_right_arm_sen = robot.getDevice('Right_arm_Sen')
        self.grip_right_arm_sen.enable(TIME_STEP)
        
        self.grip_left_arm_mt = robot.getDevice('Left_arm')
        self.grip_left_arm_sen = robot.getDevice('Left_arm_Sen')
        self.grip_left_arm_sen.enable(TIME_STEP)

        self._sensor_list = [self.base_body_sen, self.shoulder_sen, self.elbow_sen, self.grip_sen, self.roll_grip_sen, self.grip_right_arm_sen,  self.grip_left_arm_sen]
        
    @property
    def motion_status(self) -> bool:
        return self._motion_status
    
    @motion_status.setter
    def motion_status(self, status: bool):
        self._motion_status = status

    @property
    def is_home(self) -> bool:
        for sensor in self._sensor_list:
            # print(f"sensor value is :{sensor.getValue()}")
            if abs(sensor.getValue()) > 0.000001:
                self._motion_status = False
                return False
        self._motion_status = True
        return True

    @is_home.setter
    def is_home(self, status: bool):
        self._motion_status = status

    def rotatioanal_base(self):
        self.base_body_mt.setPosition(float("inf"))
        i=0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i+=1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
            
            pos = self.base_body_sen.getValue()
            print(pos)
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i<=50:
                self.base_body_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
            if i > 50:
                self.base_body_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def rotatioanal_base_reverse(self):
    
        # You should insert a getDevice-like function in order to get the
        # instance of a device of the robot. Something like:
        #  motor = robot.getDevice('motorname')
        #  ds = robot.getDevice('dsname')
        #  ds.enable(timestep)
        
        self.base_body_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.base_body_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY)
            if i > 50:
                self.base_body_mt.setVelocity(BASE_SPEED)
                break
            pass

    def shoulder(self):
        self.shoulder_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
        
            # Process sensor data here.
        
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.shoulder_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
            if i > 50:
                self.shoulder_mt.setVelocity(BASE_SPEED)
                break
            pass

    def shoulder_reverse(self):
        self.shoulder_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
        
            # Process sensor data here.
        
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.shoulder_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY)
            if i > 50:
                self.shoulder_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def elbow(self):
        self.elbow_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.elbow_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
            if i > 50:
                self.elbow_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def elbow_reverse(self):
        self.elbow_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.elbow_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY)
            if i > 50:
                self.elbow_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def gripper_pitch(self):
        self.grip_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.grip_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY)
            if i > 50:
                self.grip_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def gripper_pitch_reverse(self):
        self.grip_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.grip_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
            if i > 50:
                self.grip_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def gripper_roll(self):
        self.roll_grip_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.roll_grip_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY)
            if i > 50:
                self.roll_grip_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def gripper_roll_reverse(self):
        self.roll_grip_mt.setPosition(float("inf"))
        i = 0
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(TIME_STEP) != -1:
            i += 1
            print(i)
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            #  val = ds.getValue()
    
            # Process sensor data here.
    
            # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
            if i <= 50:
                self.roll_grip_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
            if i > 50:
                self.roll_grip_mt.setVelocity(BASE_SPEED)
                break
            pass
    
    def gripper_open(self):
        self.grip_right_arm_mt.setPosition(float("inf"))
        self.grip_left_arm_mt.setPosition(float("inf"))
        left_sensor = self.grip_left_arm_sen
        right_sensor = self.grip_right_arm_sen
        opening_print_flag = False
        
        while robot.step(TIME_STEP) != -1:
            if abs(left_sensor.getValue()) > 0.000001 and abs(right_sensor.getValue()) > 0.000001:
                if not opening_print_flag:
                    print("Opening gripper!")
                    opening_print_flag = True
                self.grip_right_arm_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY * 3)
                self.grip_left_arm_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY * 3)
            else:
                self.grip_right_arm_mt.setVelocity(BASE_SPEED)
                self.grip_left_arm_mt.setVelocity(BASE_SPEED)
                print("Gripper opened!")
                self._is_home = False
                break
    
    def gripper_close(self):
        self.grip_right_arm_mt.setVelocity(0)
        self.grip_right_arm_mt.setPosition(float("inf"))
        self.grip_left_arm_mt.setVelocity(0)
        self.grip_left_arm_mt.setPosition(float("inf"))
        left_sensor = self.grip_left_arm_sen
        right_sensor = self.grip_right_arm_sen
        closing_print_flag = False
        
        while robot.step(TIME_STEP) != -1:
            if abs(left_sensor.getValue() - 0.5056) > 0.01 and abs(right_sensor.getValue() + 0.5056) > 0.01:
                if not closing_print_flag:
                    print("Closing gripper!")
                    closing_print_flag = True
                self.grip_left_arm_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY * 3)
                self.grip_right_arm_mt.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY * 3)
            else:
                self.grip_left_arm_mt.setVelocity(BASE_SPEED)
                self.grip_right_arm_mt.setVelocity(BASE_SPEED)
                print("Gripper closed!")
                break

    def home(self):
        self.base_body_mt.setPosition(float('0'))
        self.shoulder_mt.setPosition(float('0'))
        self.elbow_mt.setPosition(float('0'))
        self.grip_mt.setPosition(float('0'))
        self.roll_grip_mt.setPosition(float('0'))
        self.grip_right_arm_mt.setPosition(float('0'))
        self.grip_left_arm_mt.setPosition(float('0'))
        home_print_flag = False

        while robot.step(TIME_STEP) != -1:
            if not self.is_home:
                if not home_print_flag:
                    print(f"Going Home")
                    home_print_flag = True
                self.base_body_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
                self.shoulder_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
                self.elbow_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
                self.grip_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
                self.roll_grip_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
                self.grip_right_arm_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
                self.grip_left_arm_mt.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
            else:
                self.base_body_mt.setVelocity(BASE_SPEED)
                self.shoulder_mt.setVelocity(BASE_SPEED)
                self.elbow_mt.setVelocity(BASE_SPEED)
                self.grip_mt.setVelocity(BASE_SPEED)
                self.roll_grip_mt.setVelocity(BASE_SPEED)
                self.grip_right_arm_mt.setVelocity(BASE_SPEED)
                self.grip_left_arm_mt.setVelocity(BASE_SPEED)
                break
        print(f"Finished going Home")
        self._is_home = True
        
    def move_joints(self, joint, direction):
        self._enable_movement = True
        motor = robot.getDevice(joint_map[joint])
        sensor = robot.getDevice(sensor_map[joint])
        motor.setPosition(float('inf'))
        print(f"Moving joint {joint_map[joint]}")
        
        while self._enable_movement and robot.step(TIME_STEP) != -1:
            self._is_home = False
            if direction == 1:
                motor.setVelocity(BASE_SPEED - MOVEMENT_VELOCITY)
            else:
                motor.setVelocity(BASE_SPEED + MOVEMENT_VELOCITY)
        
        motor.setVelocity(BASE_SPEED)
        print(f"Finished moving joint {joint_map[joint]}")
            
    def move_to_point(self, point: Point):
        pass
    
    def stop_movement(self, event, axis):
        self._enable_movement = False
        self.base_body_mt.setVelocity(BASE_SPEED)
        self.shoulder_mt.setVelocity(BASE_SPEED)
        self.elbow_mt.setVelocity(BASE_SPEED)
        self.grip_mt.setVelocity(BASE_SPEED)
        self.roll_grip_mt.setVelocity(BASE_SPEED)
        self.grip_right_arm_mt.setVelocity(BASE_SPEED)
        self.grip_left_arm_mt.setVelocity(BASE_SPEED)

    def stop(self, joint):
        self._enable_movement = False
        motor = robot.getDevice(joint_map[joint])
        motor.setVelocity(BASE_SPEED)

    def xyz_start(self, event, xyz, direction):
        axis = sensor_map[xyz]
        print(f"move_xyz : {axis, direction}")
        
    def move_xyz(self, xyz, direction):
        axis = sensor_map[xyz]
        print(f"move_xyz : {axis, direction}")

    def teach_absolute_xyz_position(self, point_number, x, y, z, pitch, roll):
        self._points[point_number] = Point(int(x * 1000), int(y * 1000), int(z * 1000), int(pitch * 1000), int(roll * 1000))
        return True
        
    def teach_relative_xyz_position(self, point_number, x, y, z, pitch, roll, relative_num):
        rel_point = self._points[relative_num]
        self._points[point_number] = Point(int(rel_point.x + x * 1000), int(rel_point.y + y * 1000), int(rel_point.z + z * 1000), int(rel_point.pitch + pitch * 1000), int(rel_point.roll + roll * 1000), "Relative")
        return True
        
    def clear_recorded_points(self):
        for point in self._points.keys():
            self.delete_point(point)
    
    def delete_point(self, point_number):
        try:
            del self._points[point_number]
            return True
        except Exception as e:
            print(f"Fail to delete point, error is : {e}")
            return False
        
    def move_linear(self, num):
        point = self._points[num]
        self.move_to_point(point)

    def get_position_coordinates(self, num: int):
        data = self.gps.getValues()
        print(f"robot coordinates are {data}")
        return data
        
    def get_position_type(self, num):
        return self._points[num].point_type
    
    def get_sensor_data(self, sensor: str):
        data = None
        if sensor == "grip_pitch_Sen":
            data = self.grip_sen.getValue()
        elif sensor == "rot_grip_Sen":
            data = self.roll_grip_sen.getValue()
        data = round(data, 5)
        return data
    
    def set_motion_status(self, status):
        if status:
            self._motion_status = True
        else:
            self._motion_status = False
    
    