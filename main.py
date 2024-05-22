import json
from models.HumanModel.Human import Human
from models.HumanModel.Family import Family
import os
os.system('clear')

family = Family().data();
human = Human(from_family=family).data()


print(json.dumps(human, indent=4, ensure_ascii=False))