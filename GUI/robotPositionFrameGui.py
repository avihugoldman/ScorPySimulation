import tkinter as tk

class RobotPositionFrame(tk.LabelFrame):
    def __init__(self, parent):
        # tk.LabelFrame.__init__(self, parent, text="Current Robot Position")
        super(RobotPositionFrame, self).__init__(parent, text="Current Robot Position")
        self.parent = parent
        self.grid(row=1, column=0, sticky=tk.W+tk.E, padx=10)
        self.initWidgets()

    def initWidgets(self):
        self.X_label = tk.Label(self, text="X(mm):")
        self.X_label.grid(row=0, column=0, pady=10)
        self.X_input = tk.Entry(self, bd=2, width=10, state="readonly", textvariable=self.parent.x_var)
        self.X_input.grid(row=0, column=1)

        tk.Label(self, width=4).grid(row=0, column=2)

        self.Y_label = tk.Label(self, text="Y(mm):")
        self.Y_label.grid(row=0, column=3)
        self.Y_input = tk.Entry(self, bd=2, width=10, state="readonly", textvariable=self.parent.y_var)
        self.Y_input.grid(row=0, column=4)

        tk.Label(self, width=4).grid(row=0, column=5)

        self.Z_label = tk.Label(self, text="Z(mm):")
        self.Z_label.grid(row=0, column=6)
        self.Z_input = tk.Entry(self, bd=2, width=10, state="readonly", textvariable=self.parent.z_var)
        self.Z_input.grid(row=0, column=7, sticky=tk.W)

        self.Pitch_label = tk.Label(self, text="Pitch(deg):")
        self.Pitch_label.grid(row=1, column=0, pady=10)
        self.Pitch_input = tk.Entry(self, bd=2, width=10, state="readonly", textvariable=self.parent.pitch_var)
        self.Pitch_input.grid(row=1, column=1)

        self.Roll_label = tk.Label(self, text="Roll(deg):")
        self.Roll_label.grid(row=1, column=3)
        self.Roll_input = tk.Entry(self, bd=2, width=10, state="readonly", textvariable=self.parent.roll_var)
        self.Roll_input.grid(row=1, column=4)

        self.Type_label = tk.Label(self, text="Type:")
        self.Type_label.grid(row=1, column=6)
        self.Type_input = tk.Entry(self, bd=2, width=15, state="readonly", textvariable=self.parent.type_var)
        self.Type_input.grid(row=1, column=7)