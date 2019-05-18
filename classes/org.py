class Org:
    def __init__(self, oid: str = "", name: str = "", mission: str = "", key_words: str = "", location: str = "",
                 children=None):
        self.oid: int = oid
        self.name: str = name
        self.mission: str = mission
        self.key_words: str = key_words
        self.location: str = location
        self.children: [Org] = children
