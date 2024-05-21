from models.Human import Human
from assets.helper_methods import randomBoolean, randomItemFromList, randomNumberBetween


class Family:
    def __init__(self):
        self.mother = None
        self.father = None

        males_list = []
        females_list = []

        for i in range(10):
            males = Human(gender=True).data()
            females = Human(gender=False).data()
            males_list.append(males)
            females_list.append(females)
            self.father = randomItemFromList(males_list)

            if randomNumberBetween(1, 10) == 1:
                self.mother = randomItemFromList(females_list)
            else:
                self.mother = Human(gender=False, country_code=self.father['environment']['location']['country_code']).data()

            mother_birth_year = self.mother['personal_info']['birth_date']['year']
            father_birth_year = self.father['personal_info']['birth_date']['year']
            if mother_birth_year - father_birth_year >= 4:
                selected_age = self.mother['personal_info']['birth_date']['year'] - randomNumberBetween(1, 6)
                self.father['personal_info']['birth_date']['year'] = selected_age
            elif father_birth_year - mother_birth_year >= 5:
                self.father['personal_info']['birth_date']['year'] = (
                        self.mother['personal_info']['birth_date']['year'] - randomNumberBetween(0, 6))

            self.mother['personal_info']['birth_date']['str'] = \
                (f"{self.mother['personal_info']['birth_date']['day']}-"
                 f"{self.mother['personal_info']['birth_date']['month']}-"
                 f"{self.mother['personal_info']['birth_date']['year']}")
            self.father['personal_info']['birth_date']['str'] = \
                (f"{self.father['personal_info']['birth_date']['day']}-"
                 f"{self.father['personal_info']['birth_date']['month']}-"
                 f"{self.father['personal_info']['birth_date']['year']}")
    def data(self):
        return {
            "father": self.father,
            "mother": self.mother,
        }