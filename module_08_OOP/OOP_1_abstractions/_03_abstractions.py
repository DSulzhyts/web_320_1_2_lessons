class Hero:
    ranger_skill_list = ["быстрая стрельба", "скрытность"]
    warrior_skill_list = ["сокрушительный удар", "вой"]
    mage_skill_list = ["огненный шар", "барьер"]

    def __init__(self, name, hero_class):
        self.name = name
        available_classes = ["рейнджер", "воин", "маг"]
        if hero_class in available_classes:
            self.hero_class = hero_class
        else:
            self.hero_class = "воин"
        self.level = 0
        self.exp = 0
        self.skill_list = []
        self.available_skills = self.add_available_skills(hero_class, self.ranger_skill_list, self.warrior_skill_list,
                                                          self.mage_skill_list)

    @staticmethod
    def add_available_skills(hero_class, ranger_skill_list, warrior_skill_list, mage_skill_list):
        if hero_class == "рейнджер":
            return ranger_skill_list
        elif hero_class == "воин":
            return warrior_skill_list
        else:
            return mage_skill_list

    def add_exp(self, exp):
        self.exp += exp
        if self.exp >= 1000:
            self.level = 3
        elif self.exp >= 500:
            self.level = 2
            skill = input(f"Вы повысили свой уровень, выберете навык {', '.join(self.available_skills)}: ")
            self.add_skill(skill)
            self.available_skills.remove(skill)
        elif self.exp >= 200:
            self.level = 1
            skill = input(f"Вы повысили свой уровень, выберете навык {', '.join(self.available_skills)}: ")
            self.add_skill(skill)
            self.available_skills.remove(skill)
        else:
            self.level = 0
        return f"Герой {self.name} получил {exp} очков опыта!\nЕго уровень теперь {self.level}"

    def add_skill(self, skill):
        if skill not in self.available_skills:
            return "Неподходящий навык"
        else:
            self.skill_list.append(skill)
        return f"Герой {self.name} получает навык {skill}"


ranger = Hero("Леголас", "рейнджер")
print(ranger.add_exp(250))
print(ranger.skill_list)
print(ranger.add_exp(250))
print(ranger.skill_list)


warrior = Hero("Гимли", "воин")
print(warrior.add_exp(250))
print(warrior.skill_list)
print(warrior.add_exp(250))
print(warrior.skill_list)
