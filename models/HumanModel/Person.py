import datetime
from assets.helper_methods import randomBoolean, randomItemFromList, randomNumberBetween
from assets.store.human_names import find_by_country_code


class Person:
    def __init__(self, environment=None, gender=None, family=None):
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.gender = None

        # Set gender
        if gender is not None:
            detected_gender = gender
        else:
            detected_gender = randomBoolean()

        self.gender = 'male' if detected_gender else 'female'

        # Set first_name & last_name
        current_year = datetime.datetime.now().year
        list_30_day_months = [4, 6, 9, 11]
        min_age_possibility = 19

        if environment is not None:
            country_code = environment.data()['location']['country_code']
            names_by_country_code = find_by_country_code(country_code)

            self.first_name = randomItemFromList(names_by_country_code[self.gender])
            self.last_name = randomItemFromList(names_by_country_code['male'])
            # Set birth_date
            min_birth_year = 1970

            random_birth_year = randomNumberBetween(min_birth_year, current_year - min_age_possibility);
            random_birth_month = randomNumberBetween(1, 12)
            random_birth_day = randomNumberBetween(1, 31)

            if random_birth_month < 10:
                random_birth_month = '0' + str(random_birth_month)

            if list_30_day_months.count(random_birth_month) > 0:
                random_birth_day = 30

            if random_birth_day < 10:
                random_birth_day = '0' + str(random_birth_day)

            self.birth_date = {
                "day": random_birth_day,
                "month": random_birth_month,
                "year": random_birth_year,
                "str": f"{random_birth_day}-{random_birth_month}-{random_birth_year}"

            }
        if family is not None:
            father = family['father']
            self.last_name = father['personal_info']['last_name']

            # Set birth_date
            current_day = datetime.datetime.now().day
            current_month = datetime.datetime.now().month
            current_year = datetime.datetime.now().year

            if current_month < 10:
                current_month = '0' + str(current_month)

            if list_30_day_months.count(current_month) > 0:
                current_day = 30

            if current_day < 10:
                current_day = '0' + str(current_day)

            self.birth_date = {
                "day": current_day,
                "month": current_month,
                "year": current_year,
                "str": f"{current_day}-{current_month}-{current_year}"
            }

    def data(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birth_date": self.birth_date
        }
