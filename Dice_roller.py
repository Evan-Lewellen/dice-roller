from random import randint


class Dice:
    def __init__(self):
        pass

    def main(self):
        self.start()
        self.result()

    def start(self):
        print('''
            Roll the Dice!
            [Press Enter to Continue]
        ''')
        input()

    def roll(self):
        while True:
            cmd = input('[a]d20 [b]d12 [c]d10 [d]d8 [e]d6 [f]d4 [g]d100  ')
            if cmd == 'a':
                dice = 'd20'
                print('You rolled a {}'.format(dice))
                throw = randint(1, 20)
                if throw == 1:
                    print('Natural 1...')
                    return 1
                elif throw == 20:
                    print('Natural 20!!')
                    return 20
                else:
                    return randint(2,19)
            elif cmd == 'b':
                dice = 'd12'
                print('You rolled a {}'.format(dice))
                return randint(1, 12)
            elif cmd == 'c':
                dice = 'd10'
                print('You rolled a {}'.format(dice))
                return randint(1, 10)
            elif cmd == 'd':
                dice = 'd8'
                print('You rolled a {}'.format(dice))
                return randint(1, 8)
            elif cmd == 'e':
                dice = 'd6'
                print('You rolled a {}'.format(dice))
                return randint(1, 6)
            elif cmd == 'f':
                dice = 'd4'
                print('You rolled a {}'.format(dice))
                return randint(1, 4)
            elif cmd == 'g':
                dice = 'd100'
                print('You rolled a {}'.format(dice))
                return randint(1, 100)
            else:
                print('Invalid option')


    def result(self):
            result = self.roll()
            while True:
                modifier = input("\nWhat is your modifier?   ")
                if modifier.isdigit():
                        mod = int(modifier)
                        print('\nYou rolled a {} with a {} modifier, for a total of {}'.format(result, mod, result + mod))
                        print('* ' * 30)
                        break
                elif modifier.isalpha():
                        print('Invalid entry')
                else:
                        mod = 0
                        print('\nYou rolled a {} with a {} modifier, for a total of {}'.format(result, mod, result + mod))
                        print('* ' * 30)
                        break

while True:
    if __name__ == '__main__':
        Dice().main()
