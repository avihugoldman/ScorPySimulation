import tkinter as tk
from tkinter import messagebox
from threading import Thread
import queue
from tooltip import Tooltip


class RobotStatusFrame(tk.LabelFrame):
    def __init__(self, parent):
        # tk.LabelFrame.__init__(self, parent, text="Robot Status")
        super(RobotStatusFrame, self).__init__(parent, text="Robot Status")
        self.parent = parent
        self.grid(row=8, column=1, sticky=tk.W + tk.S + tk.N)
        self.initWidgets()
        self.q = queue.Queue()

    def initWidgets(self):
        self.control_on_image = tk.PhotoImage(file="GUI/resources/control_on.gif")
        self.control_off_image = tk.PhotoImage(file="GUI/resources/control_off.gif")
        self.controlBtn = tk.Button(self, image=self.control_off_image, command=self.turn_control_on)
        self.controlBtn.grid(row=0, column=3, pady=10, padx=10, columnspan=4, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.controlBtn, text='turn control on')
        self.parent.buttons_set.add(self.controlBtn)

        self.home_on_image = tk.PhotoImage(file="GUI/resources/home_on.gif")
        self.home_off_image = tk.PhotoImage(file="GUI/resources/home_off.gif")
        self.homeBtn = tk.Button(self, image=self.home_off_image, command=self.async_home_robot)
        self.home_onBtn = tk.Button(self, image=self.home_on_image, command=self.async_home_robot)
        self.homeBtn.grid(row=0, column=8, pady=10, padx=10, columnspan=4, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.homeBtn, text='home robot')
        self.parent.buttons_set.add(self.homeBtn)

    def declare_stop_motion(self):
        if not (self.q.empty()):
            with self.q.mutex:
                self.q.queue.clear()
            self.parent.secondaryClient.set_motion_status(0)
        else:
            self.parent.after(100, self.declare_stop_motion)

    def turn_control_on(self):
        self.parent.on_closing()

    def async_home_robot(self):
        t = Thread(target=self.parent.robot.home, args=())
        print("in async_home_robot")
        self.parent.robot.set_motion_status(1)
        t.start()
        self.parent.after(100, self.declare_stop_motion)

    def home_robot(self):
        robot = self.parent.robot
        # if not robot.is_home:
        robot.home()
        self.parent.robot.set_motion_status(1)
        self.parent.after(100, self.declare_stop_motion)
        # outqueue.put('done')


