import tkinter as tk
from tkinter import messagebox
from tooltip import Tooltip


class PointManagementFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Record or Delete Point")
        self.parent = parent
        self.grid(row=1, column=1, sticky=tk.W + tk.S + tk.N)
        self.initWidgets()

    def initWidgets(self):
        self.rec_image = tk.PhotoImage(file="GUI/resources/rec.gif")
        self.recordPointBtn = tk.Button(self, image=self.rec_image, command=self.recordPoint)
        self.recordPointBtn.grid(row=0, column=3, pady=10, padx=10, columnspan=4, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.recordPointBtn, text='record point')
        self.parent.buttons_set.add(self.recordPointBtn)

        self.del_image = tk.PhotoImage(file="GUI/resources/del.gif")
        self.deletePointBtn = tk.Button(self, image=self.del_image, command=self.delete_point)
        self.deletePointBtn.image = self.del_image
        self.deletePointBtn.grid(row=0, column=8, pady=10, padx=10, columnspan=4, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        Tooltip(self.deletePointBtn, text='delete point')
        self.parent.buttons_set.add(self.deletePointBtn)

    def recordPoint(self):
        num_str = self.parent.point_selection_frame.currentPointBox.get()
        num = self.get_point_as_int(num_str)
        coords = self.get_point_coords()
        motors_position = self.get_point_motors_positions()
        if not (num and coords):
            return False
        if self.parent.is_point_absolute.get() == 1:
            is_recorded = self.teach_robot_absoulute_func(num, coords[0], coords[1], coords[2], coords[3], coords[4], motors_position)
            print(is_recorded)
        else:
            relative_str = self.parent.point_selection_frame.relativePointBox.get()
            if relative_str == '':
                messagebox.showinfo("Error", "choose a relative point number")
                return False
            if (relative_str == num_str):
                messagebox.showinfo("Error", "both points can't have the same number")
                return False
            is_recorded = self.teach_robot_relative_func(num, coords[0], coords[1], coords[2], coords[3], coords[4], int(relative_str), motors_position)
        if not is_recorded:
            messagebox.showinfo("Error", "Coordinates are not in the robot workspace")
        else:
            self.parent.recorded_points.add(num)
            messagebox.showinfo("Info", "Point has been recorded successfully")
            self.parent.point_selection_frame.currentPointBox['values'] = self.parent.point_selection_frame.get_recorded_points()
            self.parent.point_selection_frame.relativePointBox['values'] = self.parent.point_selection_frame.get_recorded_points()

    def delete_point(self):
        num_str = self.parent.point_selection_frame.currentPointBox.get()
        num = self.get_point_as_int(num_str)
        if not num:
            return
        is_deleted = self.parent.robot.delete_point(num)
        if not is_deleted:
            messagebox.showinfo("Error", "Could not delete point from memory")
        else:
            messagebox.showinfo("Info", f"Point {num} has been deleted from memory")
            self.parent.recorded_points.remove(num)
            self.parent.point_selection_frame.currentPointBox['values'] = self.parent.point_selection_frame.get_recorded_points()
            self.parent.point_selection_frame.relativePointBox['values'] = self.parent.point_selection_frame.get_recorded_points()

    def get_point_as_int(self, num_str):
        try:
            num = int(num_str)
        except ValueError:
            messagebox.showinfo("Error", "point number must be an integer")
            return False
        if not (1 <= num < 100):
            messagebox.showinfo("Error", "choose a point number between 1 and 99")
            return False
        return num

    def get_point_coords(self):
        coords_array = [self.parent.x_var, self.parent.y_var, self.parent.z_var, self.parent.pitch_var, self.parent.roll_var]
        result = []
        for coord in coords_array:
            try:
                result.append(coord.get())
            except ValueError:
                messagebox.showinfo("Error", "coordinates must be numbers")
                return False
        return result
    
    def get_point_motors_positions(self):
        base = self.parent.robot.base_body_sen.getValue()
        shoulder = self.parent.robot.shoulder_sen.getValue()
        elbow = self.parent.robot.elbow_sen.getValue()
        grip = self.parent.robot.grip_sen.getValue()
        roll = self.parent.robot.roll_grip_sen.getValue()
        motors_array = [base, shoulder, elbow, grip, roll]
        return motors_array

    def teach_robot_relative_func(self, point_num, x, y, z, pitch, roll, relative_num, motors_position):
        return self.parent.robot.teach_relative_xyz_position(point_num, round(float(x), 3), round(float(y), 3), round(float(z), 3), round(float(pitch * 1000), 3), round(float(roll * 1000), 3), relative_num, motors_position)

    def teach_robot_absoulute_func(self, point_num, x, y, z, pitch, roll, motors_position):
        return self.parent.robot.teach_absolute_xyz_position(point_num, round(float(x), 3), round(float(y), 3), round(float(z), 3), round(float(pitch * 1000), 3), round(float(roll * 1000), 3), motors_position)

    