from pycolor import style_text
import datetime as dt
from time import sleep
from os import system


# Special Characters : ╚ ╗ ╔ ╝║ ═ ╣ ╠ ╩ ╦ ●


class player_profile():
    def __init__(self):
        pass

class game_menu():
    def __init__(self):
        self.logo = self.recall_logo()
        self.active_profile = None
        
    def recall_logo(self):
        with open("logo.txt", 'rt') as file:
            logo = file.read()
            return logo
        
    def display_menu_screen(self):
        system("cls")
        print(self.logo)
        
        current_time = dt.datetime.now()
        print(" " + current_time.strftime("%A, %B %d %I:%M %p"))
        print(f" Active Player : {self.active_profile}")
        
        line_break = " ________________________________\n "
        print(line_break)
        
        menu_options = [
            {"option_long":"Set Active Profile",
             "option_short":"A"},
            {"option_long":"Start Game",
             "option_short":"G"},
            {"option_long":"Show High Scores",
             "option_short":"H"},
            {"option_long":"Create New Profile",
             "option_short":"C"},
            {"option_long":"Delete Profile",
             "option_short":"D"},
            {"option_long":"Exit Game",
             "option_short":"X"},
        ]
        
        for option in menu_options:
            print(f" [{option['option_short']}] {option['option_long']}")
            
        print(line_break)
        
        # TODO: Make sure this ish is valid
        menu_selection = str(input(" Selection : "))
        print(line_break)
        
        self.menu_selection_handler(menu_selection)
        
    def menu_selection_handler(self, menu_selection:str):
        match menu_selection:
            case "A":
                print("Setting Active Profile")
            case "G":
                print("Starting Game")
            case "H":
                print("Showing High Scores")
            case "C":
                print("Creating New Profile")
            case "D":
                print("Deleting Profile")
            case "X":
                print(" Exiting Game...")
                sleep(1)
                system("cls")
                exit()
    
class player_guess():
    def __init__(self):
        pass

class code():
    def __init__(self):
        pass

class game_board():
    def __init__(self):
        pass
    
def main():
    menu = game_menu()
    menu.display_menu_screen()

if __name__ == "__main__":
    main()