import tkinter as tk
from tkinter import messagebox
from threading import Thread
from tooltip import Tooltip


class GoToPointFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Go To Point")
        self.parent = parent
        self.grid(row=0, column=1, sticky=tk.W)
        self.initWidgets()

    def initWidgets(self):
        self.straight_move_image = tk.PhotoImage(file="GUI/resources/move_straight.gif")
        self.straightMoveBtn = tk.Button(self, image=self.straight_move_image, command=self.async_moveLinear)
        self.straightMoveBtn.image = self.straight_move_image
        self.straightMoveBtn.grid(row=0, column=0, pady=10, padx=10, columnspan=4, rowspan=4,
                                  sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.straightMoveBtn, text='move to point in straight line')

        self.parent.buttons_set.add(self.straightMoveBtn)

        self.curved_move_image = tk.PhotoImage(file="GUI/resources/move_curved.gif")
        self.curvedMoveBtn = tk.Button(self, image=self.curved_move_image, command=self.async_move)
        self.curvedMoveBtn.image = self.curved_move_image
        self.curvedMoveBtn.grid(row=0, column=5, pady=10, padx=10, columnspan=4, rowspan=4,
                                sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.curvedMoveBtn, text='move to point freely')
        self.parent.buttons_set.add(self.curvedMoveBtn)

    def moveLinear(self, num):
        self.parent.robot.move_linear(num)

    def async_moveLinear(self):
        num_str = self.parent.point_selection_frame.currentPointBox.get()
        num = self.parent.point_management_frame.get_point_as_int(num_str)
        if not num:
            return
        if not (num in self.parent.recorded_points):
            messagebox.showinfo("Error", "no such point in memory")
            return False
        t = Thread(target=self.moveLinear, args=(num,))
        t.start()

    def move(self, num):
        robot = self.parent.robot
        robot.go_to_point(num)

    def async_move(self):
        num_str = self.parent.point_selection_frame.currentPointBox.get()
        num = self.parent.point_management_frame.get_point_as_int(num_str)
        if not num:
            return
        if not (num in self.parent.recorded_points):
            messagebox.showinfo("Error", "no such point in memory")
            return False
        t = Thread(target=self.move, args=(num,))
        t.start()
