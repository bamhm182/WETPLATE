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
        self.init_window()
        self.toggle_button = Button(self, text='Study', height=60, width=60, image=self.pixel, compound="c", command=lambda: self.toggle_mode())
        self.toggle_button.place(x=10, y=10)
        self.popup = None

    def init_window(self):
        self.master.title("WETPLATE (Test Mode)")
        self.master.geometry("1000x520")
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

    def draw_org(self, curr, child_num: int = 0, row: int = 0, width: float = 1000, start_x: float = 0,
                 parent_x: float = 0):
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
        self.popup = AnswerPage(button_text, oid, self.wet.answer_key, self.wet.answers)


root = Tk()
app = Window(root)
root.mainloop()
