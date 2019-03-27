from random import randint
# Second version of dice roller program after refactoring. Still looking for ways to set 'self.xxxx' variables 
# to not have to repeat the 'self.' each time. 

class Dice:
    def main(self):
        self.start()
        self.roll()

    def start(self):
        print('''
            Roll the Dice!
            [Press Enter to Continue]
        ''')
        input()

    def line(self):
        print()
        print('*  '*30)
        print()

    def roll(self):
        while True:
            cmd = input('[a]d20 [b]d12 [c]d10 [d]d8 [e]d6 [f]d4 [g]d100  ')
            if cmd == 'a':
                self.kind = dice[0]
                throw = randint(1, 20)
                if throw == 1:
                    print('Natural 1...')
                    self.result = 1
                elif throw == 20:
                    print('Natural 20!!')
                    self.result = 20
                else:
                    print('d{}'.format(self.kind))
                    self.result = randint(2, 19)
            elif cmd == 'b':
                self.kind = dice[1]
            elif cmd == 'c':
                self.kind = dice[2]
            elif cmd == 'd':
                self.kind = dice[3]
            elif cmd == 'e':
                self.kind = dice[4]
            elif cmd == 'f':
                self.kind = dice[5]
            elif cmd == 'g':
                self.kind = dice[6]
            else:
                print('Invalid option')

            if self.kind != dice[0]:
                print('d{}'.format(self.kind))
                self.result = randint(1, self.kind)
            else:
                pass

            while True:
                modifier = input("\nWhat is your modifier?   ")
                if modifier.isdigit():
                        self.mod = int(modifier)
                        break
                elif modifier.isalpha():
                        print('Invalid entry')
                else:
                        self.mod = 0
                        break
            print('\nYou rolled a d{} for {} with a {} modifier for a total of {}.'.format(self.kind, self.result,self.mod,
                                                                                          self.result + self.mod))
            self.line()


while True:
    if __name__ == '__main__':
        dice = [20, 12, 10, 8, 6, 4, 100]
        Dice().main()
