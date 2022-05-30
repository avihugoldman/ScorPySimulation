import tkinter as tk
from tkinter import ttk



class PointSelectionFrame(tk.LabelFrame):
    def __init__(self, parent):
        # tk.LabelFrame.__init__(self, parent, text="Point Selection")
        super(PointSelectionFrame, self).__init__(parent, text="Point Selection")
        self.parent = parent
        self.grid(row=0, column=0, sticky=tk.W + tk.N + tk.S, padx=10)
        self.initWidgets()

    def initWidgets(self):
        self.initPointTypeRadio()
        self.init_record_type_radio()
        self.initComboBoxes()

    def initComboBoxes(self):
        self.currentPointBox = ttk.Combobox(self, textvariable=self.parent.current_point, width=5)
        self.currentPointBox['values'] = self.get_recorded_points()
        self.currentPointBox.grid(row=0, column=1, padx=10, sticky=tk.W)
        self.relativePointBox = ttk.Combobox(self, textvariable=self.parent.relative_point, width=5, state="readonly")
        self.relativePointBox['values'] = self.get_recorded_points()

    def initPointTypeRadio(self):
        self.pointNumberLabel = tk.Label(self, text="Point Number:")
        self.pointNumberLabel.grid(row=0, column=0)
        self.relativeToLabel = tk.Label(self, text="Relative to:")
        self.pointTypeLabel = tk.Label(self, text="Point type:")
        self.pointTypeLabel.grid(row=1, column=0, sticky=tk.W)
        self.absoluteBtn = tk.Radiobutton(self, text="Absolute", variable=self.parent.is_point_absolute, value=1,
                                          command=self.toggleRelativeCombo)
        self.absoluteBtn.grid(row=1, column=1, sticky=tk.W)
        self.parent.buttons_set.add(self.absoluteBtn)
        self.relativeBtn = tk.Radiobutton(self, text="Relative", variable=self.parent.is_point_absolute, value=0,
                                          command=self.toggleRelativeCombo)
        self.relativeBtn.grid(row=2, column=1, sticky=tk.W)
        self.parent.buttons_set.add(self.relativeBtn)
        tk.Label(self, width=20).grid(row=2, column=2, columnspan=2)

    def init_record_type_radio(self):
        self.teachType = tk.Label(self, text="Record by:")
        self.teachType.grid(row=0, column=4, sticky=tk.W)
        self.byRobotPositionBtn = tk.Radiobutton(self, text="Robot Position", variable=self.parent.teach_by_robot_positon, value=1,
                                                 command=self.parent.toggle_recording_frame)
        self.byRobotPositionBtn.grid(row=0, column=5, sticky=tk.W)
        self.parent.buttons_set.add(self.byRobotPositionBtn)
        self.byCoordinatesBtn = tk.Radiobutton(self, text="Coordinates", variable=self.parent.teach_by_robot_positon, value=0,
                                               command=self.parent.toggle_recording_frame)
        self.byCoordinatesBtn.grid(row=1, column=5, sticky=tk.W)
        self.parent.buttons_set.add(self.byCoordinatesBtn)


    def get_recorded_points(self):
        return sorted(self.parent.recorded_points)

    def toggleRelativeCombo(self):
        if self.parent.is_point_absolute.get() == 1:
            self.relativePointBox.grid_forget()
            self.relativeToLabel.grid_forget()
        if self.parent.is_point_absolute.get() == 0:
            self.relativePointBox.grid(row=0, column=3, sticky=tk.W)
            self.relativeToLabel.grid(row=0, column=2, sticky=tk.W)