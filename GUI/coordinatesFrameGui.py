import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from threading import Thread


class CoordinatesFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Selected point Coordinates")
        self.parent = parent
        self.initWidgets()

    def initWidgets(self):
        self.X_label = tk.Label(self, text="X(mm):")
        self.X_label.grid(row=0, column=0, pady=10)
        self.X_input = tk.Entry(self, bd=2, width=10, textvariable=self.parent.x_var)
        self.X_input.grid(row=0, column=1)

        tk.Label(self, width=4).grid(row=0, column=2)

        self.Y_label = tk.Label(self, text="Y(mm):")
        self.Y_label.grid(row=0, column=3)
        self.Y_input = tk.Entry(self, bd=2, width=10, textvariable=self.parent.y_var)
        self.Y_input.grid(row=0, column=4)

        tk.Label(self, width=4).grid(row=0, column=5)

        self.Z_label = tk.Label(self, text="Z(mm):")
        self.Z_label.grid(row=0, column=6)
        self.Z_input = tk.Entry(self, bd=2, width=10, textvariable=self.parent.z_var)
        self.Z_input.grid(row=0, column=7, sticky=tk.W)

        self.Pitch_label = tk.Label(self, text="Pitch(deg):")
        self.Pitch_label.grid(row=1, column=0, pady=10)
        self.Pitch_input = tk.Entry(self, bd=2, width=10, textvariable=self.parent.pitch_var)
        self.Pitch_input.grid(row=1, column=1)

        self.Roll_label = tk.Label(self, text="Roll(deg):")
        self.Roll_label.grid(row=1, column=3)
        self.Roll_input = tk.Entry(self, bd=2, width=10, textvariable=self.parent.roll_var)
        self.Roll_input.grid(row=1, column=4)

        self.Type_label = tk.Label(self, text="Type:")
        self.Type_label.grid(row=1, column=6)
        self.Type_input = tk.Entry(self, bd=2, width=15, state="readonly", textvariable=self.parent.type_var)
        self.Type_input.grid(row=1, column=7)

        self.getPositionBtn = ttk.Button(self, text="Get Point Coordinates", command=self.get_point_details)
        self.getPositionBtn.grid(row=2, column=1, pady=10, columnspan=3)
        self.parent.buttons_set.add(self.getPositionBtn)
        self.clearBtn = ttk.Button(self, text="Reset Coordinates", command=self.clearCoords)
        self.clearBtn.grid(row=2, column=4, columnspan=3)
        self.parent.buttons_set.add(self.clearBtn)

        # t = Thread(target=self.update_robot_position, args=())
        # t.start()

    def get_point_details(self):
        num_str = self.parent.point_selection_frame.currentPointBox.get()
        num = self.parent.point_management_frame.get_point_as_int(num_str)
        if not num:
            return
        if not (num in self.parent.recorded_points):
            messagebox.showinfo("Error", "no such point in memory")
            return False
        data_array = self.get_coords(num)
        # print(data_array)
        self.parent.x_var.set(round((data_array[0]), 3))
        self.parent.y_var.set(round((data_array[1]), 3))
        self.parent.z_var.set(round((data_array[2]), 3))
        self.parent.pitch_var.set(data_array[3])
        self.parent.roll_var.set(data_array[4])
        if data_array[5] == "Absolute":
            type_string = 'absolute'
        else:
            type_string = 'relative to ' + str(data_array[5] * -1)
        self.parent.type_var.set(type_string)

    def get_coords(self, num):
        coords_point = self.parent.robot.get_point_coordinates(num)
        coords_list = [coords_point.x, coords_point.y, coords_point.z, coords_point.pitch, coords_point.roll]
        # print(coords_list)
        coords_list += [self.parent.robot.get_position_type(num)]
        return coords_list

    def update_robot_position(self):
        if self.parent.robot.update_on:
            data_array = list(self.parent.robot.get_position_coordinates())
            data_array.append(self.parent.robot.get_sensor_data('grip_pitch_Sen'))
            data_array.append(self.parent.robot.get_sensor_data('rot_grip_Sen'))
            self.parent.x_var.set(round((data_array[0] * 100), 3))
            self.parent.y_var.set(round((data_array[1] * 100), 3))
            self.parent.z_var.set(round((data_array[2] * 100), 3))
            self.parent.pitch_var.set(data_array[3])
            self.parent.roll_var.set(data_array[4])
            time.sleep(0.05)

    def clearCoords(self):
        self.parent.x_var.set(0.0)
        self.parent.y_var.set(0.0)
        self.parent.z_var.set(0.0)
        self.parent.pitch_var.set(0.0)
        self.parent.roll_var.set(0.0)
        self.parent.type_var.set('')