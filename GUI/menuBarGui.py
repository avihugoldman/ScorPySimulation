import tkinter as tk
from tkinter import messagebox
# import scorpy.tools as tools
from tkinter.filedialog import asksaveasfilename, askopenfilename


class MenuBar(tk.Menu):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)
        self.parent = parent
        self.parent.parent.config(menu=self)
        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New...", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_command(label="Save...", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quit...", command=self.quit)

    def get_point_numbers_from_file(self, path):
        file_object = open(path, 'r')
        points_set = set()
        for line in file_object:
            lineArray = line.split(' ')
            if (len(lineArray) > 5) and (lineArray[0] == '$p') and (int(lineArray[1]) > 1) and (lineArray[3] == 'default21') and (lineArray[4] != '2147483647'):
                points_set.add(int(lineArray[1]) - 1)
        file_object.close()
        return points_set

    def remove_extension(self, name):
        if name.lower().endswith('.pnt'):
            return name.rsplit('.', 1)[0]
        else:
            return name

    def updateUiBoxesWithPoints(self):
        self.parent.recorded_points = self.get_point_numbers_from_file(self.parent.current_file_name + '.pnt')
        self.parent.point_selection_frame.currentPointBox['values'] = self.parent.point_selection_frame.get_recorded_points()
        self.parent.point_selection_frame.relativePointBox['values'] = self.parent.point_selection_frame.get_recorded_points()

    def clear_recorded_points(self):
        for point in self.parent.recorded_points:
            self.parent.client.delete_position(point)

    def new_file(self):
        self.parent.current_file_name = self.remove_extension(asksaveasfilename(filetypes=[("point file", "*.pnt")]))
        if self.parent.current_file_name:
            self.clear_recorded_points()
        if self.parent.client.save(self.parent.current_file_name):
            self.updateUiBoxesWithPoints()

    def open_file(self):
        self.parent.current_file_name = self.remove_extension(askopenfilename(filetypes=[("point file", "*.pnt")]))
        if self.parent.current_file_name:
            if self.parent.client.open(self.parent.current_file_name):
                self.updateUiBoxesWithPoints()
            else:
                messagebox.showerror("Could not open file",
                                   "File format is wrong or peripheral axis not connected to the robot")

    def save_file_as(self):
        self.parent.current_file_name = self.remove_extension(asksaveasfilename(filetypes=[("point file", "*.pnt")]))
        if self.parent.current_file_name:
            self.parent.client.save(self.parent.current_file_name)

    def save_file(self):
        if self.parent.current_file_name:
            self.parent.client.save(self.parent.current_file_name)
        else:
            self.parent.current_file_name = asksaveasfilename(filetypes=[("point file", "*.pnt")])
            if self.parent.current_file_name:
                self.parent.client.save(self.parent.current_file_name)

    def quit(self):
        self.parent.on_closing()
