import json
from models.Human import Human
from models.Family import Family
from assets.helper_methods import randomItemFromList, biographyText, biographyText1, biographyText2, biographyText3, biographyText4
import os
os.system('clear')

family = Family().data();
human = Human(from_family=family).data()


print(json.dumps(human, indent=4, ensure_ascii=False))