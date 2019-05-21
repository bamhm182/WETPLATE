from tkinter import *
import random
import classes.utils as utils


class AnswerPage:
    def __init__(self, parent_text, oid, answer_key, answers):
        self.answer_key = answer_key
        self.oid = oid
        self.parent_text = parent_text
        self.answers = answers
        self.popup = Tk()
        self.popup.title("Organization")
        self.popup.minsize(500, 500)
        self.popup.maxsize(500, 500)
        self.popup.eval('tk::PlaceWindow %s center' % self.popup.winfo_pathname(self.popup.winfo_id()))

        name_label = Label(self.popup, text="Org Name")
        name_label.pack()

        self.name = StringVar(self.popup)
        self.name.set(utils.get_values(utils.get_org(answers, oid), 'name', False))
        name_drop = OptionMenu(self.popup, self.name, *self.get_choices('name'),
                               command=lambda event: self.check_answers())
        name_drop.config(width=50, anchor="w")
        name_drop.pack()

        mission_label = Label(self.popup, text="Mission")
        mission_label.pack()

        curr_misson = utils.get_values(utils.get_org(answers, oid), 'mission', False)
        self.mission_written_text = StringVar(self.popup, value=curr_misson)
        mission_written_label = Label(self.popup, textvariable=self.mission_written_text, wraplength=400,
                                      justify="center")
        mission_written_label.pack()

        self.mission = StringVar(self.popup)
        self.mission.set(curr_misson)
        mission_drop = OptionMenu(self.popup, self.mission, *self.get_choices('mission'),
                                  command=lambda event: self.check_answers())
        mission_drop.config(width=50, anchor="w")
        mission_drop.pack()

        key_words_label = Label(self.popup, text="Key Words")
        key_words_label.pack()

        self.key_words = StringVar(self.popup)
        self.key_words.set(utils.get_values(utils.get_org(answers, oid), 'key_words', False))
        key_words_drop = OptionMenu(self.popup, self.key_words, *self.get_choices('key_words'),
                                    command=lambda event: self.check_answers())
        key_words_drop.config(width=50, anchor="w")
        key_words_drop.pack()

        location_label = Label(self.popup, text="Location")
        location_label.pack()

        self.location = StringVar(self.popup)
        self.location.set(utils.get_values(utils.get_org(answers, oid), 'location', False))
        location_drop = OptionMenu(self.popup, self.location, *self.get_choices('location'),
                                   command=lambda event: self.check_answers())
        location_drop.config(width=50, anchor="w")
        location_drop.pack()

        self.answer_check = StringVar(self.popup)
        self.answer_check.set("")
        answer_check_label = Label(self.popup, textvariable=self.answer_check)
        answer_check_label.pack()

        self.save_button = Button(self.popup, text="Save", state=DISABLED)
        self.save_button.configure(command=lambda: self.update_org())
        self.save_button.pack()

        position_right = int(self.popup.winfo_screenwidth() / 2 - 250)
        position_down = int(self.popup.winfo_screenheight() / 2 - 250)
        self.popup.geometry("+{}+{}".format(position_right, position_down))
        self.check_answers()

    def update_org(self, orgs=None):
        if not orgs:
            orgs = self.answers

        if orgs.oid == self.oid:
            self.parent_text.set(self.name.get())
            orgs.name = self.name.get()
            orgs.mission = self.mission.get()
            orgs.key_words = self.key_words.get()
            orgs.location = self.location.get()
            self.popup.destroy()
            return True
        if orgs.children:
            for child in orgs.children:
                if self.update_org(child):
                    break

    def check_answers(self):
        won = True

        self.mission_written_text.set(self.mission.get())

        if self.oid == "" or (
                self.name.get() == "" and self.mission.get() == "" and self.key_words.get() == "" and self.location.get() == ""):
            self.answer_check.set("Choose something!")
            return

        if self.name.get() != "" and self.answer_key[self.oid]['name'] != self.name.get():
            won = False

        if self.mission.get() != "" and self.answer_key[self.oid]['mission'] != self.mission.get():
            won = False

        if self.key_words.get() != "" and self.answer_key[self.oid]['key_words'] != self.key_words.get():
            won = False

        if self.location.get() != "" and self.answer_key[self.oid]['location'] != self.location.get():
            won = False

        if won:
            set_name = "\nSet a name to save."
            if self.name.get() != "":
                set_name = ""
                self.save_button.config(state=NORMAL)
            self.answer_check.set(f"You win!{set_name}")
        else:
            self.save_button.config(state=DISABLED)
            self.answer_check.set("Womp womp, try again!")

    def get_choices(self, value, num=5):
        choices = list()
        choices.append(self.answer_key[self.oid][value])
        all_choices = list()
        for oid in self.answer_key:
            if oid != self.oid:
                all_choices.append(self.answer_key[oid][value])

        limit = 0

        while len(choices) < num and limit < 25:
            rand = random.choice(all_choices)
            if rand != "" and rand not in choices:
                choices.append(rand)
            limit += 1

        random.shuffle(choices)

        return choices
