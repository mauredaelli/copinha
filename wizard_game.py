from actors import Wizard, Creature
import random
import time

#  A simple RPG-ish game.


def main():
    name = input("\nOh mighty wizard, what's your grand name?")
    print_header()
    game_loop(name)


def print_header():
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.25)
    print('--------------------------------')
    print('         WIZARD GAME!')
    print('--------------------------------')
    print()
    time.sleep(0.5)


def game_loop(name):
    #  manually initialize creatures as objects of a class;
    #  creature(name, level, luck);
    #  TODO add MP and tricks;
    #  TODO expand, automate and randomize types, levels etc
    creatures = [
        Creature('Toad', 1, random.randint(1, 10)),
        Creature('Toad', 2, random.randint(1, 10)),
        Creature('Toad', 3, random.randint(2, 10)),
        Creature('Spider', 2, random.randint(1, 10)),
        Creature('Spider', 4, random.randint(1, 10)),
        Creature('Spider', 6, random.randint(1, 10)),
        Creature('Snake', 3, random.randint(1, 10)),
        Creature('Snake', 6, random.randint(1, 10)),
        Creature('Snake', 9, random.randint(1, 10)),
        Creature('Bat', 3, random.randint(1, 10)),
        Creature('Bat', 4, random.randint(1, 10)),
        Creature('Bat', 5, random.randint(1, 10)),
        Creature('Tiger', 10, random.randint(1, 10)),
        Creature('Tiger', 15, random.randint(1, 10)),
        Creature('Tiger', 20, random.randint(1, 10)),
        Creature('Dragon', 30, random.randint(1, 10)),
        Creature('Dragon', 35, random.randint(1, 10)),
        Creature('Dragon', 40, random.randint(1, 10)),
        Creature('Evil Wizard', 50, random.randint(1, 10)),
        Creature('Evil Wizard', 60, random.randint(1, 10)),
        Creature('Evil Wizard', 70, random.randint(1, 10)),
        Creature('Fairy', None, None)  # increases your luck points
    ]

    hero = Wizard(name, 3, 0, random.randint(1, 10))
    #  initialize one single object for the class Wizard;
    #  Wizard(name, level, XP, luck);
    #  TODO add MP and tricks (signs which consume MP and potions)

    while True:
        #  every turn: the hero attacks a creature by surprise
        #  TODO elaborate situations and choices

        active_creature = random.choice(creatures)
        if active_creature.name == 'Fairy':
            #  only good creature here; could be in a proper class
            #  with other good beings
            print("A Fairy has appeared!")
            print('''\n"Hello, dear {}, I'm your Luck Fairy. 
                     Be careful in your path! Here you receive my blessing!"\n
                  '''.format(name))
            print("Your luck has increased! Now it is {}.".format(hero.luck))
            input("Press enter to continue...")
        else:
            print("\nA {} of level {} has appeared from a "
                  "dark and foggy forest...".format(
                   active_creature.name, active_creature.level))
            print()
            print("Your stats are: level {}, xp {}, luck {}".format(
                hero.level, hero.xp, hero.luck))
            cmd = input("Do you [a]ttack or [r]unaway?").lower()

            # hero.level = 100
            if cmd == 'a':
                if hero.attack(active_creature):
                    hero.increase(active_creature)
                    creatures.remove(active_creature)
                    #  it's not necessary to remove a creature after one single bout

                else:
                    print("The wizard runs and hides taking time to recover...")
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    input("Press enter to continue...")
                    # TODO we need serious consequences here!
            elif cmd == 'r':
                print("{} has become unsure of his power and flees.".format(
                    hero.name))
                # TODO more consequences ...
                input("Press enter to continue...")
            else:
                print('OK, exiting game.')
                break


if __name__ == '__main__':
    main()
