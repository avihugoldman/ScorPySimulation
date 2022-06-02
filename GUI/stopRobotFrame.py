import tkinter as tk
from tooltip import Tooltip


class StopRobotFrame(tk.LabelFrame):
    def __init__(self, parent):
        super(StopRobotFrame, self).__init__(parent, text="Stop Robot")
        self.parent = parent
        self.grid(row=2, column=1, sticky=tk.W + tk.S + tk.N)
        self.initWidgets()

    def initWidgets(self):
        self.stop_image = tk.PhotoImage(file="GUI/resources/stop.gif")
        self.stopRobotBtn = tk.Button(self, image=self.stop_image, command=self.stop_robot)
        self.stopRobotBtn.grid(row=0, column=3, pady=10, padx=10, columnspan=4, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.stopRobotBtn, text='stop robot movement')

    def stop_robot(self):
        print("Stopping all movement")
        self.parent.robot.stop_movement(None, None)
