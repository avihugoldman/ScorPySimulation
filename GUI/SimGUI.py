import tkinter as tk
from threading import Thread
from tkinter import messagebox

import SimRobot
from menuBarGui import MenuBar
from robotPositionFrameGui import RobotPositionFrame
from pointSelectionFrameGui import PointSelectionFrame
from coordinatesFrameGui import CoordinatesFrame
from pointManagementFrame import PointManagementFrame
from goToPointFrame import GoToPointFrame
from robotMovementFrameGui import RobotMovementFrame
from robotStatusFrame import RobotStatusFrame
from stopRobotFrame import StopRobotFrame


class RobotGui(tk.Frame):
    def __init__(self, parent, scorpy_robot):
        # tk.Frame.__init__(self, parent)
        super(RobotGui, self).__init__(parent)
        self.parent = parent
        try:
            # print(int(SimRobot.robot.getBasicTimeStep()))
            self.running = True
        except Exception as e:
            self.running = False
            print(f"Webots not running {e}")
        self.init_variables()
        self.grid()
        self.robot = scorpy_robot
        t = Thread(target=self.main_widgets(), args=(self,))
        t.start()
        # self.main_widgets()

    def main_widgets(self):
        self.menuBar = MenuBar(self)
        self.point_selection_frame = PointSelectionFrame(self)
        self.point_management_frame = PointManagementFrame(self)
        self.robot_position_frame = RobotPositionFrame(self)
        self.coordinates_frame = CoordinatesFrame(self)
        self.go_to_position_frame = GoToPointFrame(self)
        self.robot_movement_frame = RobotMovementFrame(self)
        self.robot_status_frame = RobotStatusFrame(self)
        self.stop_robot_frame = StopRobotFrame(self)

    def init_variables(self):
        self.current_file_name = None
        self.recorded_points = set()
        self.buttons_set = set()
        self.is_point_absolute = tk.IntVar()
        self.is_point_absolute.set(1)
        self.is_control_on = tk.IntVar()
        self.is_control_on.set(0)
        self.error_status = tk.IntVar()
        self.error_status.set(0)
        self.is_homed = tk.IntVar()
        self.is_homed.set(0)
        self.teach_by_robot_positon = tk.IntVar()
        self.teach_by_robot_positon.set(1)
        self.current_point = tk.StringVar()
        self.relative_point = tk.StringVar()
        self.x_var = tk.DoubleVar()
        self.y_var = tk.DoubleVar()
        self.z_var = tk.DoubleVar()
        self.pitch_var = tk.DoubleVar()
        self.roll_var = tk.DoubleVar()
        self.type_var = tk.StringVar()

    def toggle_recording_frame(self):
        if self.teach_by_robot_positon.get() == 1:
            self.coordinates_frame.grid_forget()
            self.robot_position_frame.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10)
        if self.teach_by_robot_positon.get() == 0:
            self.robot_position_frame.grid_forget()
            self.coordinates_frame.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10)
            self.x_var.set(0.0)
            self.y_var.set(0.0)
            self.z_var.set(0.0)
            self.pitch_var.set(0.0)
            self.roll_var.set(0.0)
            self.type_var.set('')

    def disable_buttons(self, state):
        if state:
            toggle = "disabled"
        else:
            toggle = "normal"
        for widget in self.buttons_set:
            widget.configure(state=toggle)

    def on_closing(self):
        if messagebox.askokcancel("Are you sure you want to quit?",
                                  "Make sure you save any changes to points before you quit\n Click Ok to quit or Cancel to go back"):
            self.parent.destroy()
            exit(0)

    def get_control_status(self):
        if False:
            return 1
        else:
            return 0

    def check_robot_status(self):
        self.is_control_on.set(self.get_control_status())
        if self.robot.is_home:
            self.robot_status_frame.homeBtn.configure(image=self.robot_status_frame.home_on_image)
        else:
            self.robot_status_frame.homeBtn.configure(image=self.robot_status_frame.home_off_image)
        if self.is_control_on.get() == 1:
            self.robot_status_frame.controlBtn.configure(image=self.robot_status_frame.control_on_image)
        else:
            self.robot_status_frame.controlBtn.configure(image=self.robot_status_frame.control_off_image)

    def update_robot_coordinates(self):
        if self.teach_by_robot_positon.get() == 1:
            if self.is_point_absolute.get() == 1:
                coords_list = [0.1, 0.1, 0.1, 0.1, 0.1]
                self.x_var.set(coords_list[0])
                self.y_var.set(coords_list[1])
                self.z_var.set(coords_list[2])
                self.pitch_var.set(coords_list[3])
                self.roll_var.set(coords_list[4])
                self.type_var.set('absolute')
            elif self.is_point_absolute.get() == 0:
                if self.relative_point.get():
                    coords_list = [0.1, 0.1, 0.1, 0.1, 0.1]
                    anchor_point_vector = [0.1, 0.1, 0.1, 0.1, 0.1]
                    self.x_var.set(coords_list[0] - anchor_point_vector[0])
                    self.y_var.set(coords_list[1] - anchor_point_vector[1])
                    self.z_var.set(coords_list[2] - anchor_point_vector[2])
                    self.pitch_var.set(coords_list[3] - anchor_point_vector[3])
                    self.roll_var.set(coords_list[4] - anchor_point_vector[4])
                    self.type_var.set('relative to ' + self.relative_point.get())
                else:
                    self.x_var.set(0.0)
                    self.y_var.set(0.0)
                    self.z_var.set(0.0)
                    self.pitch_var.set(0.0)
                    self.roll_var.set(0.0)
                    self.type_var.set('relative to ?')
        else:
            if self.is_point_absolute.get() == 1:
                self.type_var.set('absolute')
            elif self.is_point_absolute.get() == 0:
                if self.relative_point.get():
                    self.type_var.set('relative to ' + self.relative_point.get())
                else:
                    self.type_var.set('relative to ?')

    def routine_check(self):
        self.check_robot_status()
        self.update_robot_coordinates()
        self.after(100, self.routine_check)


def start_gui(scorpy_robot):
    root = tk.Tk()
    app = RobotGui(root, scorpy_robot)
    if app.running:
        root.title("ScorPySimulation")
        root.geometry("700x600")
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        root.after(100, app.routine_check)
        app.mainloop()


scorpy_robot = SimRobot.SimRobot()

start_gui(scorpy_robot)

