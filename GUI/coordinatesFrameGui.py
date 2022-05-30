import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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

        self.getPositionBtn = ttk.Button(self, text="Get Point Coordinates", command=self.getPointDetails)
        self.getPositionBtn.grid(row=2, column=1, pady=10, columnspan=3)
        self.parent.buttons_set.add(self.getPositionBtn)
        self.clearBtn = ttk.Button(self, text="Reset Coordinates", command=self.clearCoords)
        self.clearBtn.grid(row=2, column=4, columnspan=3)
        self.parent.buttons_set.add(self.clearBtn)

    def getPointDetails(self):
        num_str = self.parent.point_selection_frame.currentPointBox.get()
        num = self.parent.point_management_frame.get_point_as_int(num_str)
        if not num:
            return
        if not (num in self.parent.recorded_points):
            messagebox.showinfo("Error", "no such point in memory")
            return False
        data_array = self.get_coords(num)
        print(data_array)
        self.parent.x_var.set(data_array[0])
        self.parent.y_var.set(data_array[1])
        self.parent.z_var.set(data_array[2])
        self.parent.pitch_var.set(data_array[3])
        self.parent.roll_var.set(data_array[4])
        if data_array[5] == "Absolute":
            type_string = 'absolute'
        else:
            type_string = 'relative to ' + str(data_array[5] * -1)
        self.parent.type_var.set(type_string)

    def get_coords(self, num):
        coords_list = list(self.parent.robot.get_position_coordinates(num))
        print(coords_list)
        coords_list.append(self.parent.robot.get_sensor_data('grip_pitch_Sen'))
        coords_list.append(self.parent.robot.get_sensor_data('rot_grip_Sen'))
        coords_list.append(self.parent.robot.get_position_type(num))
        # coords_list += [self.parent.robot.get_sensor_data('rot_grip_Sen')]
        # coords_list = [self.parent.robot.get_position_type(num)]
        return coords_list


    def clearCoords(self):
        self.parent.x_var.set(0.0)
        self.parent.y_var.set(0.0)
        self.parent.z_var.set(0.0)
        self.parent.pitch_var.set(0.0)
        self.parent.roll_var.set(0.0)
        self.parent.type_var.set('')