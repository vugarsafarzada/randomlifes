from models.HumanModel.Family import Family


class Relationships:
    def __init__(self, family=None, friends=None, love=None):
        self.family = family if family else Family()
        #self.friends = friends if friends else [Person(), Person()]
        #self.love = love if love else Person()

    def data(self):
        return {
            "family": self.family.data(),
            #"friends": [friend.data() for friend in self.friends],
            # "love": self.love.data()
        }
