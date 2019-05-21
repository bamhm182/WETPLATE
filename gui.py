from tkinter import *
from classes.wetplate import WETPLATE
from classes.answer_page import AnswerPage


class Window(Frame):
    def __init__(self, master=None):
        self.wet = WETPLATE()
        Frame.__init__(self, master)
        self.master = master
        self.pixel = PhotoImage(width=1, height=1)
        self.buttons = list()
        self.window_width = 1000
        self.window_height = 520
        self.init_window()
        self.toggle_button = Button(self, text='Study', height=60, width=60, image=self.pixel, compound="c", command=lambda: self.toggle_mode())
        self.toggle_button.place(x=10, y=10)
        self.popup = None

        position_right = int(master.winfo_screenwidth() / 2 - self.window_width / 2)
        position_down = int(master.winfo_screenheight() / 2 - self.window_height / 2)
        master.geometry("+{}+{}".format(position_right, position_down))

    def init_window(self):
        self.master.title("WETPLATE (Test Mode)")
        self.master.geometry(f"{self.window_width}x{self.window_height}")
        self.pack(fill=BOTH, expand=1)
        self.draw_org(self.wet.answers)

    def toggle_mode(self):
        placeholder = self.wet.answers
        self.wet.answers = self.wet.orgs
        self.wet.orgs = placeholder
        for button in self.buttons:
            button.destroy()
        self.toggle_button.configure(text='Study' if self.toggle_button.cget('text') == 'Test' else 'Test')
        self.master.title(f"WETPLATE ({'Study' if self.toggle_button.cget('text') == 'Test' else 'Test'} Mode)")
        self.draw_org(self.wet.answers)

    def draw_org(self, curr, child_num: int = 0, row: int = 0, width: float = None, start_x: float = 0,
                 parent_x: float = 0):
        if width is None:
            width = self.window_width
        row_dist = 75
        position = width / 2

        if not curr.children:
            start_x = parent_x
            position = 0
            row += 1 * (child_num + 1)
            row_dist = 50

        x = start_x + position - 30
        y = 10 + (row * row_dist)
        button_text = StringVar()
        button_text.set(curr.name)
        button = Button(self, textvariable=button_text, height=30, width=60, image=self.pixel, compound="c")
        button.configure(command=lambda: self.draw_org_set(button_text, curr.oid))
        button.place(x=x, y=y)
        self.buttons.append(button)
        if curr.children:
            for i, child in enumerate(curr.children):
                self.draw_org(child, i, row + 1, width / len(curr.children),
                              start_x + ((width / len(curr.children)) * i), start_x + position)

    def draw_org_set(self, button_text, oid):
        if self.popup is not None:
            try:
                self.popup.popup.destroy()
            except TclError:
                pass
            self.popup = None

        self.popup = AnswerPage(button_text, oid, self.wet.answer_key, self.wet.answers)


root = Tk()
app = Window(root)
root.mainloop()
