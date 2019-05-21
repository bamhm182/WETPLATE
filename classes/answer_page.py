from tkinter import *
import random
import classes.utils as utils


class AnswerPage:
    def __init__(self, parent_text, oid, answer_key, answers):
        self.answer_key = answer_key
        self.oid = oid
        self.answers = answers
        self.popup = Tk()
        self.popup.title("Organization")
        self.popup.minsize(500, 500)
        self.popup.maxsize(500, 500)

        name_label = Label(self.popup, text="Org Name")
        name_label.pack()

        name = StringVar(self.popup)
        name.set(utils.get_values(utils.get_org(answers, oid), 'name', False))
        name_drop = OptionMenu(self.popup, name, *self.get_choices('name'))
        name_drop.config(width=50, anchor="w")
        name_drop.pack()

        mission_label = Label(self.popup, text="Mission")
        mission_label.pack()

        curr_misson = utils.get_values(utils.get_org(answers, oid), 'mission', False)
        mission_written_text = StringVar(self.popup, value=curr_misson)
        mission_written_label = Label(self.popup, textvariable=mission_written_text, wraplength=400,
                                      justify="center")
        mission_written_label.pack()

        mission = StringVar(self.popup)
        mission.set(curr_misson)
        mission_drop = OptionMenu(self.popup, mission, *self.get_choices('mission'),
                                  command=lambda event: self.mission_changed(mission_written_text, mission))
        mission_drop.config(width=50, anchor="w")
        mission_drop.pack()

        key_words_label = Label(self.popup, text="Key Words")
        key_words_label.pack()

        key_words = StringVar(self.popup)
        key_words.set(utils.get_values(utils.get_org(answers, oid), 'key_words', False))
        key_words_drop = OptionMenu(self.popup, key_words, *self.get_choices('key_words'))
        key_words_drop.config(width=50, anchor="w")
        key_words_drop.pack()

        location_label = Label(self.popup, text="Location")
        location_label.pack()

        location = StringVar(self.popup)
        location.set(utils.get_values(utils.get_org(answers, oid), 'location', False))
        location_drop = OptionMenu(self.popup, location, *self.get_choices('location'))
        location_drop.config(width=50, anchor="w")
        location_drop.pack()

        answer_check = StringVar(self.popup)
        answer_check.set("")
        answer_check_label = Label(self.popup, textvariable=answer_check)
        answer_check_label.pack()

        save = Button(self.popup, text="Save")
        save.configure(command=lambda: self.update_org(parent_text, oid, name, mission, key_words, location))
        save.pack()

        check = Button(self.popup, text="Check Answers")
        check.configure(command=lambda: self.check_answers(oid, name, mission, key_words, location, answer_check))
        check.pack()

    def mission_changed(self, text, mission):
        text.set(mission.get())

    def update_org(self, parent_text, oid, name, mission, key_words, location, orgs=None):
        if not orgs:
            orgs = self.answers

        if orgs.oid == oid:
            parent_text.set(name.get())
            orgs.name = name.get()
            orgs.mission = mission.get()
            orgs.key_words = key_words.get()
            orgs.location = location.get()
            self.popup.destroy()
            return True
        if orgs.children:
            for c in orgs.children:
                if self.update_org(parent_text, oid, name, mission, key_words, location, c):
                    break

    def check_answers(self, oid, name, mission, key_words, location, label):
        won = True

        if oid == "" or (
                name.get() == "" and mission.get() == "" and key_words.get() == "" and location.get() == ""):
            label.set("Choose something!")
            return

        if name.get() != "" and self.answer_key[oid]['name'] != name.get():
            won = False

        if mission.get() != "" and self.answer_key[oid]['mission'] != mission.get():
            won = False

        if key_words.get() != "" and self.answer_key[oid]['key_words'] != key_words.get():
            won = False

        if location.get() != "" and self.answer_key[oid]['location'] != location.get():
            won = False

        if won:
            label.set("You win!")
        else:
            label.set("Womp womp, try again!")

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
