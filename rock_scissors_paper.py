import random


class EndGameException(Exception):
    """Exception that helps to end the game."""
    pass


class RockScissorsPaper:
    """This class helps to organize Rock-Scissors-Paper game by its' methods."""

    data = ["scissors", "rock", "paper"]
    commands = ["!exit", "!rating"]
    ratings = dict()

    def __init__(self, user_name):
        """This method takes username from class initialization and construct user profile and gaming field."""
        self.users_name = user_name
        self.greetings()
        self.read_ratings()
        self.users_rating = self.set_user_rating()
        self.field = self.input_field()
        self.allowed_inputs = self.field + self.commands
        self.print_start()

    def set_user_rating(self):
        """This method search users in "Rating" database and set this number to existing user.
        If user don't exist, this method makes rating equal to zero."""
        if self.users_name in self.ratings.keys():
            users_rating = self.ratings[self.users_name]
        else:
            users_rating = 0
        return users_rating

    def read_ratings(self):
        """Method reads rating.txt and takes username and rating number to "ratings" database"""
        with open("rating.txt") as readfile:
            for line in readfile.readlines():
                info = line.strip().split()
                self.ratings[info[0]] = int(info[1])

    def print_rating(self):
        print(f"Your rating: {self.users_rating}")

    def greetings(self):
        print(f"Hello, {self.users_name}")

    @staticmethod
    def print_start():
        print("Okay, let's start")

    @staticmethod
    def read_name():
        user_name = input("Enter your name:")
        return user_name

    @staticmethod
    def computer_wins(computers_move):
        print(f"Sorry, but the computer chose {computers_move}")

    @staticmethod
    def draw(computers_move):
        print(f"There is a draw ({computers_move})")

    @staticmethod
    def player_wins(computers_move):
        print(f"Well done. The computer chose {computers_move} and failed")

    @staticmethod
    def end_game():
        print("Bye!")
        raise EndGameException

    def input_field(self):
        """This method takes variables that need to play as a string splitted by and comma and returns as a list.
         if input is an empty string returns standart variables Rock, Scissors, Paper"""
        field = input()
        if field == "":
            field = self.data
        else:
            field = field.split(",")
        return field

    def menu_command(self, command):
        """Takes command. Helps to show rating or exit."""
        if command == "!rating":
            self.print_rating()
        elif command == "!exit":
            self.end_game()

    def calculating(self, inp):
        """Calculates win and lose variables lists for input."""
        inp_index = self.field.index(inp)
        rules = self.field[inp_index + 1:] + self.field[:inp_index]
        index_slice = int(len(rules) / 2)
        win_list = rules[:index_slice]
        loose_list = rules[index_slice:]
        return win_list, loose_list

    def gameplay(self):
        """Checks user input. If it in commands program direct to command menu.
        If it in variables list it computer plays with you choosing random variable from field,
        and than analyses game results by searching in won and lose list."""
        user_input = input()
        if user_input in self.allowed_inputs:
            if user_input in self.commands:
                self.menu_command(user_input)
            else:
                win_list, loose_list = self.calculating(user_input)
                comp_input = random.choice(self.field)
                if comp_input == user_input:
                    self.users_rating += 50
                    self.draw(comp_input)
                elif comp_input in win_list:
                    self.users_rating += 0
                    self.computer_wins(comp_input)
                elif comp_input in loose_list:
                    self.users_rating += 100
                    self.player_wins(comp_input)
        else:
            print("Invalid input")

    def infinity_gameplay(self):
        """Infinite loop that makes user to play infinite matches until player inputs !exit"""
        while True:
            try:
                self.gameplay()
            except EndGameException:
                break


if __name__ == '__main__':
    name = RockScissorsPaper.read_name()
    game = RockScissorsPaper(name)
    game.infinity_gameplay()


    
