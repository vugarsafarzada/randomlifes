from assets.store.locations import locations, find_country_by_country_code
from assets.helper_methods import randomItemFromList, combineLists, randomBoolean


class Environment:
    def __init__(self, from_family=None, by_country_code=None):
        self.demography = None
        self.location = None

        if from_family is None:
            selected_location = find_country_by_country_code(by_country_code) if by_country_code else randomItemFromList(locations)
            random_city = randomItemFromList(selected_location['popular_cities'])
            self.demography = {
                "nationality": [selected_location['nationality']],
                "speaking_langs": selected_location['languages']
            }
            self.location = {
                "country": selected_location['country'],
                "country_code": selected_location['country_code'],
                "city": random_city
            }
        else:
            father_environment = from_family['father']['environment']
            mother_environment = from_family['mother']['environment']
            family_environments_list = [father_environment, mother_environment]
            random_selected_environment_from_family = randomItemFromList(family_environments_list)

            self.demography = {
                'nationality': combineLists(father_environment['demography']['nationality'], mother_environment['demography']['nationality']),
                'speaking_langs': combineLists(father_environment['demography']['speaking_langs'], mother_environment['demography']['speaking_langs']),
            }
            self.location = {
                "country": random_selected_environment_from_family['location']['country'],
                "country_code": random_selected_environment_from_family['location']['country_code'],
                "city": random_selected_environment_from_family['location']['city'],
            }
            if randomBoolean():
                random_selected_another_city = randomItemFromList(find_country_by_country_code(self.location['country_code'])['popular_cities'])
                self.location['city'] = random_selected_another_city;
                if randomBoolean():
                    selected_location2 = randomItemFromList(locations)
                    random_city2 = randomItemFromList(selected_location2['popular_cities'])
                    self.location = {
                        "country": selected_location2['country'],
                        "country_code": selected_location2['country_code'],
                        "city": random_city2
                    }
                    self.demography = {
                        "nationality": self.demography['nationality'],
                        "speaking_langs": combineLists(self.demography['speaking_langs'], selected_location2['languages'])
                    }

    def data(self):
        return {
            "demography": self.demography,
            "location": self.location,
        }

