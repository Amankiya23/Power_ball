import emoji
import random
from colorama import Fore, Back



print()

print(emoji.emojize("\t\t\t:smiling_face_with_halo:"), Fore.BLACK, Back.GREEN, 'Welcome To', Back.RESET, Back.YELLOW,
      ' Lucky Lottery', Back.RESET, Back.RED, 'Numbers', Back.RESET, Fore.RESET, Back.RESET)
print("\n")


# In the next class I used Multilevel Inheritance.
# I use this class to generate random lucky & Today's number.
class Whiteball():
    def __init__(self):
        self.Today_num = sorted(random.sample(range(1, 20), 5))
        self.Lucky_num = sorted(random.sample(range(1, 20), 5))


# In the next class I Inherited white_ball Class.
# I use this class to generate random lucky & Today's number_Powerball.
class Powerball(Whiteball):
    def __init__(self):
        super().__init__()
        self.Today_num_powerball = []
        self.Lucky_num_powerball = []

    def insert(self):
        pnum = random.randint(1, 10)
        self.Today_num_powerball.append(pnum)
        pnum2 = random.randint(1, 10)
        self.Lucky_num_powerball.append(pnum2)

    def veiw(self):
        print(Back.WHITE, Fore.BLACK, f"Today's winning number is:", Fore.RESET, Back.RESET, Fore.LIGHTMAGENTA_EX,
              f"\n\t{self.Today_num}",
              Fore.RESET, Fore.YELLOW, f" {self.Today_num_powerball}", Fore.RESET)
        print(Back.WHITE, Fore.BLACK, f"your lucky number is: ", Fore.RESET, Back.RESET, Fore.LIGHTMAGENTA_EX,
              f" \n\t{self.Lucky_num}",
              Fore.RESET, Fore.YELLOW, f"{self.Lucky_num_powerball}", Fore.RESET, "\n")


# In this class I included the conditional statements that I have to use on the project.
class comparee(Powerball):

    def test(self):
        correct_numbers = len(set(self.Today_num).intersection(self.Lucky_num))
        correct_numbers2 = len(set(self.Today_num_powerball).intersection(self.Lucky_num_powerball))
        print(Back.WHITE, Fore.BLACK, "===================RESULT=======================", Back.RESET, Fore.RESET)
        if correct_numbers == 5 and correct_numbers2 == 1:
            print(emoji.emojize(":money-mouth_face:"),
                  f"{correct_numbers} 	Correct White Balls and the Powerball: Jackpot $324,000,000")
        elif correct_numbers == 5 and correct_numbers2 == 0:
            print(emoji.emojize(":money-mouth_face:"),
                  f"{correct_numbers}  Correct White Balls, but no Powerball: $1,000,000")
        elif correct_numbers == 4 and correct_numbers2 == 1:
            print(emoji.emojize(":money-mouth_face:"),
                  f"{correct_numbers} Correct White Balls and the Powerball: $10,000  ")
        elif correct_numbers == 4 and correct_numbers2 == 0:
            print(emoji.emojize(":money-mouth_face:"), f"{correct_numbers} Correct White Balls,but no Powerball: $100")
        elif correct_numbers == 3 and correct_numbers2 == 1:
            print(emoji.emojize(":money-mouth_face:"), f"{correct_numbers} Correct White Balls,and the Powerball: $100")
        elif correct_numbers == 3 and correct_numbers2 == 0:
            print(emoji.emojize(":money-mouth_face:"), f"{correct_numbers} Correct White Balls,but no Powerball: $7")
        elif correct_numbers == 2 and correct_numbers2 == 1:
            print(emoji.emojize(":money-mouth_face:"), f"{correct_numbers} Correct White Balls and the Powerball: $7")
        elif correct_numbers == 1 and correct_numbers2 == 1:
            print(emoji.emojize(":money-mouth_face:"), f"{correct_numbers} Correct White Ball and the Powerball: $4")
        elif correct_numbers == 0 and correct_numbers2 == 1:
            print(f"{correct_numbers} No White Balls, Just the Powerball:  $4")
        else:
            print("Try again!")


# Here we call the class compare to run our program.


final = comparee()
final.insert()
final.veiw()
final.test()
