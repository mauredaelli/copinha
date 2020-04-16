from actors import Wizard, Creature
import random
import time

#  A simple RPG-ish game.


def main():
    name = input("\nOh mighty wizard, what's your grand name? ")
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
        Creature('Toad', random.randint(1, 3), random.randint(1, 10)),
        Creature('Spider', 2 * random.randint(1, 3), random.randint(1, 10)),
        Creature('Snake', 3 * random.randint(1, 3), random.randint(1, 10)),
        Creature('Bat', 2 + random.randint(1, 3), random.randint(1, 10)),
        Creature('Tiger', 10 + random.randint(1, 10), random.randint(1, 10)),
        Creature('Dragon', 30 + random.randint(1, 10), random.randint(1, 10)),
        Creature('Evil Wizard', 50 + random.randint(1, 10), random.randint(1, 10)),
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
            if hero.luck < 10:
                if random.random() < 0.6:
                    hero.luck += 1
            print("Your luck has increased! Now it is {}.".format(hero.luck))
            input("Press enter to continue...")
        else:
            print("\nA {} of level {} has appeared from a "
                  "dark and foggy forest...".format(
                   active_creature.name, active_creature.level))
            print()
            print("Your stats are: level {}, xp {}, luck {}".format(
                hero.level, hero.xp, hero.luck))
            cmd = input("Do you [a]ttack or [r]unaway? ").lower()

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
                cmd = input('Do you really wnat exit the game? (y/n): ')
                if cmd == 'y':
                    print('OK, exiting game.')
                    break


if __name__ == '__main__':
    main()
