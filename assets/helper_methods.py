import random
from datetime import datetime


def randomNumberBetween(lower: int, upper: int) -> int:
    return random.randint(lower, upper)


def randomBoolean() -> bool:
    possibility = randomNumberBetween(0, 1)
    return possibility == 1


def randomItemFromList(itemList: list) -> tuple:
    index = randomNumberBetween(0, len(itemList) - 1)
    return itemList[index]


def combineLists(list1: list, list2: list) -> list:
    combined_list = list(set(list1).union(list2))
    return combined_list


def biographyText1(person_data):
    # Extract personal information
    first_name = person_data['personal_info']['first_name']
    last_name = person_data['personal_info']['last_name']
    gender = person_data['personal_info']['gender']
    birth_date = person_data['personal_info']['birth_date']['str']

    # Extract environmental information
    nationality = ', '.join(person_data['environment']['demography']['nationality'])
    languages = ', '.join(person_data['environment']['demography']['speaking_langs'])
    country = person_data['environment']['location']['country']
    city = person_data['environment']['location']['city']

    # Extract father's information
    father_first_name = person_data['family']['father']['personal_info']['first_name']
    father_last_name = person_data['family']['father']['personal_info']['last_name']
    father_gender = person_data['family']['father']['personal_info']['gender']
    father_birth_date = person_data['family']['father']['personal_info']['birth_date']['str']
    father_birth_city = person_data['family']['father']['environment']['location']['city']

    # Extract mother's information
    mother_first_name = person_data['family']['mother']['personal_info']['first_name']
    mother_last_name = person_data['family']['mother']['personal_info']['last_name']
    mother_gender = person_data['family']['mother']['personal_info']['gender']
    mother_birth_date = person_data['family']['mother']['personal_info']['birth_date']['str']
    mother_birth_city = person_data['family']['mother']['environment']['location']['city']

    # Construct the biography
    biography = (f"{first_name} {last_name} was born on {birth_date} in {city}, {country}. "
                 f"{gender.capitalize()} holds {nationality} nationality and is fluent in {languages}. "
                 f"{first_name} grew up in a culturally rich environment, embracing the traditions and languages of {country}. "
                 f"{first_name}'s father, {father_first_name} {father_last_name}, was born on {father_birth_date} in {father_birth_city}. "
                 f"Having {father_gender} as a role model, {first_name} learned the values of perseverance and dedication. "
                 f"{first_name}'s mother, {mother_first_name} {mother_last_name}, was born on {mother_birth_date} in {mother_birth_city}. "
                 f"{mother_first_name} imparted the importance of compassion and resilience to {first_name}. "
                 f"Growing up in {city}, {first_name} enjoyed a nurturing environment that was both supportive and inspiring. "
                 f"Surrounded by the rich history and vibrant culture of {country}, {first_name} developed a profound appreciation for their heritage. "
                 f"The blend of influences from both parents, combined with the unique experiences of growing up in {city}, "
                 f"has shaped {first_name} into a well-rounded individual with a deep connection to their roots.")

    return biography


def biographyText2(person_data):
    # Extract personal information
    first_name = person_data['personal_info']['first_name']
    last_name = person_data['personal_info']['last_name']
    gender = person_data['personal_info']['gender']
    birth_date = person_data['personal_info']['birth_date']['str']

    # Extract environmental information
    nationality = ', '.join(person_data['environment']['demography']['nationality'])
    languages = ', '.join(person_data['environment']['demography']['speaking_langs'])
    country = person_data['environment']['location']['country']
    city = person_data['environment']['location']['city']

    # Extract father's information
    father_first_name = person_data['family']['father']['personal_info']['first_name']
    father_last_name = person_data['family']['father']['personal_info']['last_name']
    father_birth_date = person_data['family']['father']['personal_info']['birth_date']['str']
    father_city = person_data['family']['father']['environment']['location']['city']

    # Extract mother's information
    mother_first_name = person_data['family']['mother']['personal_info']['first_name']
    mother_last_name = person_data['family']['mother']['personal_info']['last_name']
    mother_birth_date = person_data['family']['mother']['personal_info']['birth_date']['str']
    mother_city = person_data['family']['mother']['environment']['location']['city']

    # Construct the biography
    biography = (f"{first_name} {last_name} was born on {birth_date} in {city}, {country}. "
                 f"{gender.capitalize()} is of {nationality} nationality and speaks {languages}. "
                 f"{first_name}'s father, {father_first_name} {father_last_name}, was born on {father_birth_date} "
                 f"and resides in {father_city}. {first_name}'s mother, {mother_first_name} {mother_last_name}, was born on {mother_birth_date} "
                 f"and resides in {mother_city}.")

    return biography


def biographyText3(person_data):
    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Extract personal information
    first_name = person_data['personal_info']['first_name']
    last_name = person_data['personal_info']['last_name']
    gender = person_data['personal_info']['gender']
    birth_date = person_data['personal_info']['birth_date']['str']

    # Determine pronouns based on gender
    pronoun = 'he' if gender == 'male' else 'she'
    possessive_pronoun = 'his' if gender == 'male' else 'her'

    # Extract environmental information
    nationality = ', '.join(person_data['environment']['demography']['nationality'])
    languages = ', '.join(person_data['environment']['demography']['speaking_langs'])
    country = person_data['environment']['location']['country']
    city = person_data['environment']['location']['city']

    # Extract father's information
    father_first_name = person_data['family']['father']['personal_info']['first_name']
    father_last_name = person_data['family']['father']['personal_info']['last_name']
    father_birth_date = person_data['family']['father']['personal_info']['birth_date']['str']
    father_birth_city = person_data['family']['father']['environment']['location']['city']
    father_birth_country = person_data['family']['father']['environment']['location']['country']
    father_age = datetime.now().year - int(person_data['family']['father']['personal_info']['birth_date']['year'])

    # Extract mother's information
    mother_first_name = person_data['family']['mother']['personal_info']['first_name']
    mother_last_name = person_data['family']['mother']['personal_info']['last_name']
    mother_birth_date = person_data['family']['mother']['personal_info']['birth_date']['str']
    mother_birth_city = person_data['family']['mother']['environment']['location']['city']
    mother_birth_country = person_data['family']['mother']['environment']['location']['country']
    mother_age = datetime.now().year - int(person_data['family']['mother']['personal_info']['birth_date']['year'])

    # Construct the biography
    biography = (f"{first_name} {last_name} was born on {birth_date}, which is today, in {city}, {country}. "
                 f"{pronoun.capitalize()} is a newborn of {nationality} nationality and will grow up speaking {languages}. "
                 f"{first_name}'s father, {father_first_name} {father_last_name}, was born on {father_birth_date} in {father_birth_city}, {father_birth_country}. "
                 f"He is {father_age} years old and has had a significant influence on the family with his experiences. "
                 f"{first_name}'s mother, {mother_first_name} {mother_last_name}, was born on {mother_birth_date} in {mother_birth_city}, {mother_birth_country}. "
                 f"She is {mother_age} years old and will undoubtedly provide {first_name} with a loving and nurturing environment. "
                 f"Together, {father_first_name} and {mother_first_name} will raise {first_name} in {city}, instilling in {pronoun} the values and traditions of their diverse backgrounds.")

    return biography


def biographyText4(person_data):
    # Extract personal information
    first_name = person_data['personal_info']['first_name']
    last_name = person_data['personal_info']['last_name']
    gender = person_data['personal_info']['gender']
    birth_date = person_data['personal_info']['birth_date']['str']

    # Determine pronouns based on gender
    pronoun = 'he' if gender == 'male' else 'she'
    possessive_pronoun = 'his' if gender == 'male' else 'her'

    # Extract environmental information
    nationality = ', '.join(person_data['environment']['demography']['nationality'])
    languages = ', '.join(person_data['environment']['demography']['speaking_langs'])
    country = person_data['environment']['location']['country']
    city = person_data['environment']['location']['city']

    # Extract father's information
    father_first_name = person_data['family']['father']['personal_info']['first_name']
    father_last_name = person_data['family']['father']['personal_info']['last_name']
    father_birth_date = person_data['family']['father']['personal_info']['birth_date']['str']
    father_birth_city = person_data['family']['father']['environment']['location']['city']
    father_birth_country = person_data['family']['father']['environment']['location']['country']
    father_age = datetime.now().year - int(person_data['family']['father']['personal_info']['birth_date']['year'])

    # Extract mother's information
    mother_first_name = person_data['family']['mother']['personal_info']['first_name']
    mother_last_name = person_data['family']['mother']['personal_info']['last_name']
    mother_birth_date = person_data['family']['mother']['personal_info']['birth_date']['str']
    mother_birth_city = person_data['family']['mother']['environment']['location']['city']
    mother_birth_country = person_data['family']['mother']['environment']['location']['country']
    mother_age = datetime.now().year - int(person_data['family']['mother']['personal_info']['birth_date']['year'])

    # Construct the biography
    biography = (f"{first_name} {last_name} was born on {birth_date}, which is today, in {city}, {country}. "
                 f"{pronoun.capitalize()} is a newborn of {nationality} nationality and will grow up speaking {languages}. "
                 f"{first_name}'s father, {father_first_name} {father_last_name}, was born on {father_birth_date} in {father_birth_city}, {father_birth_country}. "
                 f"He is {father_age} years old and has had a significant influence on the family with his experiences. "
                 f"{first_name}'s mother, {mother_first_name} {mother_last_name}, was born on {mother_birth_date} in {mother_birth_city}, {mother_birth_country}. "
                 f"She is {mother_age} years old and will undoubtedly provide {first_name} with a loving and nurturing environment. "
                 f"Together, {father_first_name} and {mother_first_name} will raise {first_name} in {city}, instilling in {possessive_pronoun} the values and traditions of their diverse backgrounds.")

    return biography


def biographyText(person_data):
    # Extract personal information
    first_name = person_data['personal_info']['first_name']
    last_name = person_data['personal_info']['last_name']
    gender = person_data['personal_info']['gender']
    birth_date = person_data['personal_info']['birth_date']['str']

    # Determine pronouns based on gender
    pronoun = 'he' if gender == 'male' else 'she'
    possessive_pronoun = 'his' if gender == 'male' else 'her'

    # Extract environmental information
    nationality = ', '.join(person_data['environment']['demography']['nationality'])
    languages = ', '.join(person_data['environment']['demography']['speaking_langs'])
    country = person_data['environment']['location']['country']
    city = person_data['environment']['location']['city']

    # Extract father's information
    father_first_name = person_data['family']['father']['personal_info']['first_name']
    father_last_name = person_data['family']['father']['personal_info']['last_name']
    father_gender = person_data['family']['father']['personal_info']['gender']
    father_birth_date = person_data['family']['father']['personal_info']['birth_date']['str']
    father_birth_city = person_data['family']['father']['environment']['location']['city']
    father_birth_country = person_data['family']['father']['environment']['location']['country']
    father_age = datetime.now().year - int(person_data['family']['father']['personal_info']['birth_date']['year'])

    # Extract mother's information
    mother_first_name = person_data['family']['mother']['personal_info']['first_name']
    mother_last_name = person_data['family']['mother']['personal_info']['last_name']
    mother_gender = person_data['family']['mother']['personal_info']['gender']
    mother_birth_date = person_data['family']['mother']['personal_info']['birth_date']['str']
    mother_birth_city = person_data['family']['mother']['environment']['location']['city']
    mother_birth_country = person_data['family']['mother']['environment']['location']['country']
    mother_age = datetime.now().year - int(person_data['family']['mother']['personal_info']['birth_date']['year'])

    # Construct the biography
    biography = (f"'{first_name} {last_name}' was born on {birth_date}, which is today, in {city}, {country}. "
                 f"{pronoun.capitalize()} is a newborn of {nationality} nationality and will grow up speaking {languages}. "
                 f"{first_name}'s father, {father_first_name} {father_last_name}, was born on {father_birth_date} in {father_birth_city}, {father_birth_country}. "
                 f"He is {father_age} years old and has had a significant influence on the family with his experiences. "
                 f"{first_name}'s mother, {mother_first_name} {mother_last_name}, was born on {mother_birth_date} in {mother_birth_city}, {mother_birth_country}. "
                 f"She is {mother_age} years old and will undoubtedly provide {first_name} with a loving and nurturing environment. "
                 f"Together, {father_first_name} and {mother_first_name} will raise {first_name} in {city}, instilling in {possessive_pronoun} the values and traditions of their diverse backgrounds.")

    return biography


def randomBiographyText(human):
    biographies = [
        biographyText(human),
        biographyText1(human),
        biographyText2(human),
        biographyText3(human),
        biographyText4(human),
    ]
    return randomItemFromList(biographies)


def shuffle_array(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def select_random_items(arr, num_items=6):
    if len(arr) < num_items:
        raise ValueError("The array does not have enough items to select from.")

    return random.sample(arr, num_items)