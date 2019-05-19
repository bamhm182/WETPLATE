import classes.utils as utils


class WETPLATE:
    def __init__(self):
        self.orgs = utils.read_orgs()
        self.answers = utils.wipe_values(self.orgs)
        self.answer_key = utils.build_answer_key(self.orgs)
        self.names = utils.get_values(self.orgs, 'name')
        self.missions = utils.get_values(self.orgs, 'mission')
        self.key_words = utils.get_values(self.orgs, 'key_words')
        self.locations = utils.get_values(self.orgs, 'location')
