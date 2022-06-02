import threading
import tkinter as tk
from tkinter import ttk
from robotMoveByAxisFrame import RobotMoveByAxisFrame, Joints, XYZ, Direction
from threading import Thread

class RobotMovementFrame(tk.LabelFrame):
    def __init__(self, parent):
        super(RobotMovementFrame, self).__init__(parent, text="Move Robot Manually", height=350)
        self.parent = parent
        self.grid(row=2, rowspan = 30, column=0, sticky=tk.W + tk.E, padx=10)
        self.pack_propagate(False)
        self.initWidgets()
        self.robot = parent.robot
        self._enable_movement = True

    def initWidgets(self):
        buttonStyle = ttk.Style()
        buttonStyle.configure('my.TButton', font=('Helvetica', 8), width=2)
        self.background_image = tk.PhotoImage(file="GUI/resources/robot.gif")
        self.background_label = tk.Label(self, image=self.background_image, width=408, height=297)
        self.background_label.image = self.background_image
        self.background_label.place(x=30, y=10)

        self.base_inc = ttk.Button(self, text=u"\u25c4", style = 'my.TButton')
        self.base_inc.bind('<ButtonPress-1>',
                      lambda event, joint=Joints.BASE, direction=Direction.DEC: self.joint_start(event, joint, direction))
        self.base_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.BASE: self.stop(event, joint))

        self.base_inc.place(x=10, y=215)
        self.parent.buttons_set.add(self.base_inc)

        self.base_dec = ttk.Button(self, text=u"\u25ba", style = 'my.TButton')
        self.base_dec.bind('<ButtonPress-1>',
                      lambda event, joint=Joints.BASE, direction=Direction.INC: self.joint_start(event, joint, direction))
        self.base_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.BASE: self.stop(event, joint))
        self.base_dec.place(x=190, y=215)
        self.parent.buttons_set.add(self.base_dec)

        self.shoulder_inc = ttk.Button(self, text=u"\u25c4", style = 'my.TButton')
        self.shoulder_inc.bind('<ButtonPress-1>',
                          lambda event, joint=Joints.SHOULDER, direction=Direction.INC: self.joint_start(event, joint, direction))
        self.shoulder_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.SHOULDER: self.stop(event, joint))
        self.shoulder_inc.place(x=90, y=70)
        self.parent.buttons_set.add(self.shoulder_inc)

        self.shoulder_dec = ttk.Button(self, text=u"\u25bc", style = 'my.TButton')
        self.shoulder_dec.bind('<ButtonPress-1>',
                          lambda event, joint=Joints.SHOULDER, direction=Direction.DEC: self.joint_start(event, joint, direction))
        self.shoulder_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.SHOULDER: self.stop(event, joint))
        self.shoulder_dec.place(x=166, y=160)
        self.parent.buttons_set.add(self.shoulder_dec)

        self.elbow_inc = ttk.Button(self, text=u"\u25b2", style = 'my.TButton')
        self.elbow_inc.bind('<ButtonPress-1>',
                       lambda event, joint=Joints.ELBOW, direction=Direction.INC: self.joint_start(event, joint, direction))
        self.elbow_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.ELBOW: self.stop(event, joint))
        self.elbow_inc.place(x=230, y=30)
        self.parent.buttons_set.add(self.elbow_inc)

        self.elbow_dec = ttk.Button(self, text=u"\u25bc", style = 'my.TButton')
        self.elbow_dec.bind('<ButtonPress-1>',
                       lambda event, joint=Joints.ELBOW, direction=Direction.DEC: self.joint_start(event, joint, direction))
        self.elbow_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.ELBOW: self.stop(event, joint))
        self.elbow_dec.place(x=230, y=110)
        self.parent.buttons_set.add(self.elbow_dec)

        self.pitch_inc = ttk.Button(self, text=u"\u25b2", style = 'my.TButton')
        self.pitch_inc.bind('<ButtonPress-1>',
                       lambda event, joint=Joints.PITCH, direction=Direction.INC: self.joint_start(event, joint, direction))
        self.pitch_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.PITCH: self.stop(event, joint))
        self.pitch_inc.place(x=360, y=30)
        self.parent.buttons_set.add(self.pitch_inc)

        self.pitch_dec = ttk.Button(self, text=u"\u25bc", style = 'my.TButton')
        self.pitch_dec.bind('<ButtonPress-1>',
                       lambda event, joint=Joints.PITCH, direction=Direction.DEC: self.joint_start(event, joint, direction))
        self.pitch_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.PITCH: self.stop(event, joint))
        self.pitch_dec.place(x=360, y=110)
        self.parent.buttons_set.add(self.pitch_dec)

        self.roll_inc = ttk.Button(self, text=u"\u25c4", style = 'my.TButton')
        self.roll_inc.bind('<ButtonPress-1>',
                      lambda event, joint=Joints.ROLL, direction=Direction.INC: self.joint_start(event, joint, direction))
        self.roll_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.ROLL: self.stop(event, joint))
        self.roll_inc.place(x=265, y=160)
        self.parent.buttons_set.add(self.roll_inc)

        self.roll_dec = ttk.Button(self, text=u"\u25ba", style = 'my.TButton')
        self.roll_dec.bind('<ButtonPress-1>',
                      lambda event, joint=Joints.ROLL, direction=Direction.DEC: self.joint_start(event, joint, direction))
        self.roll_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.ROLL: self.stop(event, joint))
        self.roll_dec.place(x=375, y=160)
        self.parent.buttons_set.add(self.roll_dec)

        self.gripper_label = tk.Label(self,text="Gripper")
        self.gripper_label.place(x=250, y=230)

        self.gripper_open = ttk.Button(self, width=5, text="Open")
        self.gripper_open.bind('<ButtonRelease-1>',
                         lambda event: self.open_gripper(event))
        self.gripper_open.place(x=252, y=252)
        self.parent.buttons_set.add(self.gripper_open)

        self.gripper_close = ttk.Button(self, width=5, text="Close")
        self.gripper_close.bind('<ButtonRelease-1>',
                         lambda event: self.close_gripper(event))
        self.gripper_close.place(x=252, y=278)
        self.parent.buttons_set.add(self.gripper_close)

        self.moveByAxis = RobotMoveByAxisFrame(self)

    def joint_start(self, event, joint, direction):
        if str(event.widget['state']) == 'normal':
            t_1 = Thread(target=self.parent.robot.move_joints, args=(joint, direction))
            t_1.start()
    
    def move_joints_step(self, event, joint, direction):
        if str(event.widget['state']) == 'normal':
            self.parent.robot.move_joints_step(joint, direction)
    
    def xyz_start(self, event, axis, direction):
        if str(event.widget['state']) == 'normal':
            self.parent.robot.move_xyz(axis, direction)

    def open_gripper(self, event):
        if str(event.widget['state']) == 'normal':
            self.parent.robot.gripper_open()

    def close_gripper(self, event):
        if str(event.widget['state']) == 'normal':
            self.parent.robot.gripper_close()

    def stop(self, event, axis):
        self._enable_movement = False
        if str(event.widget['state']) == 'normal':
            self.parent.robot.stop(axis)
            print("stopping")
            
