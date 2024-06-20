import json
import datetime as dt

from pycolor import style_text
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
        self.player_profiles = self.recall_profiles()
        
    def recall_profiles(self):
        with open("player_profiles.json", "rt") as profiles_file:
            profiles = json.load(profiles_file)
            return profiles
        
    def recall_logo(self):
        with open("logo.txt", 'rt') as file:
            logo = file.read()
            return logo
        
    def display_menu_screen(self):
        system("cls")
        print(self.logo)
        
        current_time = dt.datetime.now()
        print(" " + current_time.strftime("%A, %B %d %I:%M %p"))
        if self.active_profile != None:
            print(f" Active Player : {self.active_profile['player_name']}")
        else:
            print(f" Active Player : None")
        
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
                print(" Setting Active Profile...")
                sleep(1)
                self.set_active_profile()
            case "G":
                print("Starting Game...")
                sleep(1)
            case "H":
                print("Showing High Scores...")
                sleep(1)
            case "C":
                print("Creating New Profile...")
                sleep(1)
            case "D":
                print("Deleting Profile...")
                sleep(1)
            case "X":
                print(" Exiting Game...")
                sleep(1)
                system("cls")
                exit()
                
    def return_to_menu(self):
        input(" \n Press Enter to return to menu...")
        self.display_menu_screen()
                
    def set_active_profile(self):
        system("cls")
        print("\n <--> <--> Select Profile <--> <--> \n")
        
        for i, profile in enumerate(self.player_profiles):
            (print(f" [{i+1}] {profile['player_name']}"))
            
        profile_selection = int(input("\n Selection : ")) - 1
        self.active_profile = self.player_profiles[profile_selection]
        
        print(f"\n Active Profile set to... {self.active_profile['player_name']}")
        
        self.return_to_menu()
        
    
        
        
    
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