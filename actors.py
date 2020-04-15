import random
"""
Here we define 2 classes and their actions: wizard and creatures
"""


class Wizard:
    def __init__(self, name, level, xp, luck):
        self.luck = luck
        self.name = name
        self.level = level
        self.xp = xp

    def __repr__(self):
        #  substitutes the labels when debugging
        return "Wizard {} of level {}, xp {} and luck {}".format(
            self.name, self.level, self.xp, self.luck
        )

    def attack(self, creature):
        print("\nThe wizard {} attacks the {}!".format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, self.luck * self.level)
        creature_roll = random.randint(1, creature.level * creature.luck)
        #  the clash is decided by random results, associated with stats

        print("\nYou roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("\nThe wizard has triumphed over the {}!".format(
                creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!")
            return False

    def increase(self, creature):
        self.xp = self.xp + creature.level * random.randint(1, 10) *\
                  self.luck / 10
        self.xp = int(self.xp)
        if self.xp >= 100:
            #  level scale is linear
            #  TODO change level upgrade to a non linear scale
            self.level += 1
            self.xp = self.xp - 100 # XP resets when >= 100; could
            # ever increase, so the level upgrade must be modified;
            print("\nOh mighty {}, your level has upgraded! Yey!".format(self.name))
        else:
            print("Now your XP is {}.".format(self.xp))

    # TODO a decrease mechanism in case of defeat


class Creature:
    #  TODO level increase and decrease mechanism

    def __init__(self, name, level, luck):
        self.level = level
        self.name = name
        self.luck = luck

    def __repr__(self):
        return "Creature {} of level {} and luck {}".format(
            self.name, self.level, self.luck
        )
