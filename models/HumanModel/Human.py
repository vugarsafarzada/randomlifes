from models.HumanModel.Person import Person
from models.HumanModel.Environment import Environment


class Human:
    def __init__(self, personal_info=None, country_code=None, from_family=None, gender=None):
        self.environment = Environment(from_family=from_family, by_country_code=country_code)
        self.personal_info = personal_info if personal_info else Person(
            environment=self.environment,
            gender=gender,
            family=from_family
        )
        self.family = from_family

    def data(self):
        data = {
            "personal_info": self.personal_info.data(),
            "environment": self.environment.data(),
        }
        if self.family is not None:
            data["family"] = self.family

        return data
