import tkinter as tk
from tkinter import ttk


class Joints:
    BASE, SHOULDER, ELBOW, PITCH, ROLL, GRIPPER = range(6)


class XYZ:
    X_AXIS, Y_AXIS, Z_AXIS = range(3)


class Direction:
    INC, DEC = range(2)


class RobotMoveByAxisFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Move By Axis")
        self.parent = parent
        self.place(x=310, y=215)
        self.initWidgets()

    def initWidgets(self):
        self.x_label = tk.Label(self, text="X")
        self.x_label.grid(row=0, column=0, sticky=tk.E + tk.W, padx=5)

        self.x_inc = ttk.Button(self, text="+", width=1)
        self.x_inc.bind('<ButtonPress-1>',
                        lambda event, axis=XYZ.X_AXIS, direction=Direction.INC: self.parent.xyz_start(event, 'x', direction))
        self.x_inc.bind('<ButtonRelease-1>', lambda event, axis=XYZ.X_AXIS: self.parent.robot.stop_movement(event, 'x'))
        self.x_inc.grid(row=1, column=0)
        self.parent.parent.buttons_set.add(self.x_inc)

        self.x_dec = ttk.Button(self, text="-", width=1)
        self.x_dec.bind('<ButtonPress-1>',
                   lambda event, axis=XYZ.X_AXIS, direction=Direction.DEC: self.parent.xyz_start(event, 'x', direction))
        self.x_dec.bind('<ButtonRelease-1>', lambda event, axis=XYZ.X_AXIS: self.parent.robot.stop_movement(event, 'x'))
        self.x_dec.grid(row=2, column=0)
        self.parent.parent.buttons_set.add(self.x_dec)

        self.y_label = tk.Label(self, text="Y")
        self.y_label.grid(row=0, column=1, sticky=tk.E + tk.W, padx=5)

        self.y_inc = ttk.Button(self, text="+", width=1)
        self.y_inc.bind('<ButtonPress-1>',
                   lambda event, axis=XYZ.Y_AXIS, direction=Direction.INC: self.parent.xyz_start(event, 'y', direction))
        self.y_inc.bind('<ButtonRelease-1>', lambda event, axis=XYZ.Y_AXIS: self.parent.robot.stop_movement(event, 'y'))
        self.y_inc.grid(row=1, column=1)
        self.parent.parent.buttons_set.add(self.y_inc)

        self.y_dec = ttk.Button(self, text="-", width=1)
        self.y_dec.bind('<ButtonPress-1>',
                   lambda event, axis=XYZ.Y_AXIS, direction=Direction.DEC: self.parent.xyz_start(event, 'y', direction))
        self.y_dec.bind('<ButtonRelease-1>', lambda event, axis=XYZ.Y_AXIS: self.parent.robot.stop_movement(event, 'y'))
        self.y_dec.grid(row=2, column=1)
        self.parent.parent.buttons_set.add(self.y_dec)

        self.z_label = tk.Label(self, text="Z")
        self.z_label.grid(row=0, column=2, sticky=tk.E + tk.W, padx=5)

        self.z_inc = ttk.Button(self, text="+", width=1)
        self.z_inc.bind('<ButtonPress-1>',
                   lambda event, axis=XYZ.Z_AXIS, direction=Direction.INC: self.parent.xyz_start(event, 'z', direction))
        self.z_inc.bind('<ButtonRelease-1>', lambda event, axis=XYZ.Z_AXIS: self.parent.robot.stop_movement(event, 'z'))
        self.z_inc.grid(row=1, column=2)
        self.parent.parent.buttons_set.add(self.z_inc)

        self.z_dec = ttk.Button(self, text="-", width=1)
        self.z_dec.bind('<ButtonPress-1>',
                   lambda event, axis=XYZ.Z_AXIS, direction=Direction.DEC: self.parent.xyz_start(event, 'z', direction))
        self.z_dec.bind('<ButtonRelease-1>', lambda event, axis=XYZ.Z_AXIS: self.parent.robot.stop_movement(event, 'z'))
        self.z_dec.grid(row=2, column=2)
        self.parent.parent.buttons_set.add(self.z_dec)

        self.p_label = tk.Label(self, text="P")
        self.p_label.grid(row=0, column=3, sticky=tk.E + tk.W, padx=5)

        self.p_inc = ttk.Button(self, text="+", width=1)
        self.p_inc.bind('<ButtonPress-1>',
                   lambda event, joint=Joints.PITCH, direction=Direction.INC: self.parent.move_joints_step(event, joint, direction))
        self.p_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.PITCH: self.parent.robot.stop_movement(event, joint))
        self.p_inc.grid(row=1, column=3)
        self.parent.parent.buttons_set.add(self.p_inc)

        self.p_dec = ttk.Button(self, text="-", width=1)
        self.p_dec.bind('<ButtonPress-1>',
                   lambda event, joint=Joints.PITCH, direction=Direction.DEC: self.parent.move_joints_step(event, joint, direction))
        self.p_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.PITCH: self.parent.robot.stop_movement(event, joint))
        self.p_dec.grid(row=2, column=3)
        self.parent.parent.buttons_set.add(self.p_dec)

        self.r_label = tk.Label(self, text="R")
        self.r_label.grid(row=0, column=4, sticky=tk.E + tk.W, padx=5)

        self.r_inc = ttk.Button(self, text="+", width=1)
        self.r_inc.bind('<ButtonPress-1>',
                   lambda event, joint=Joints.ROLL, direction=Direction.INC: self.parent.move_joints_step(event, joint, direction))
        self.r_inc.bind('<ButtonRelease-1>', lambda event, joint=Joints.ROLL: self.parent.robot.stop_movement(event, joint))
        self.r_inc.grid(row=1, column=4)
        self.parent.parent.buttons_set.add(self.r_inc)

        self.r_dec = ttk.Button(self, text="-", width=1)
        self.r_dec.bind('<ButtonPress-1>',
                   lambda event, joint=Joints.ROLL, direction=Direction.DEC: self.parent.move_joints_step(event, joint, direction))
        self.r_dec.bind('<ButtonRelease-1>', lambda event, joint=Joints.ROLL: self.parent.robot.stop_movement(event, joint))
        self.r_dec.grid(row=2, column=4)
        self.parent.parent.buttons_set.add(self.r_dec)

