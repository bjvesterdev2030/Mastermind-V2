import json
import datetime as dt
import random as rnd

from pycolor import style_text
from time import sleep
from os import system


# Special Characters : ╚ ╗ ╔ ╝║ ═ ╣ ╠ ╩ ╦ ●

# BUG: Cannot escape the set_active_player() or delete_profile() functions if there are no profiles. Fix this.

# TODO: Begin working on the game portion of this project. Except for the above bug, the menu is complete.  
# TODO: Fix the player profile class... should have included that to begin with... do this last. Maybe its not needed
class player_profile():
    def __init__(self):
        pass

class game_menu():
    def __init__(self):
        self.logo = self.recall_logo()
        self.active_profile = None
        self.player_profiles = self.recall_profiles()

    # --- Methods for data recall --- #
    
    def recall_profiles(self):
        with open("player_profiles.json", "rt") as profiles_file:
            profiles = json.load(profiles_file)
            return profiles
        
    def recall_logo(self):
        with open("logo.txt", 'rt') as file:
            logo = file.read()
            return logo
        
    # --- Menu operation functions --- #
        
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
        
        valid_input = [option["option_short"] for option in menu_options]
        
        menu_selection = ""
        while menu_selection not in valid_input:
            menu_selection = str(input(" Selection : "))
            if menu_selection not in valid_input:
                print(" This input is invalid. Please enter a valid input.")
        print(line_break)
        
        self.menu_selection_handler(menu_selection)
        
    def menu_selection_handler(self, menu_selection:str):
        match menu_selection:
            case "A":
                print(" Setting Active Profile...")
                sleep(1)
                self.set_active_profile()
            case "G":
                print(" Starting Game...")
                sleep(1)
                game = game_board(active_player=self.active_profile)
                game.play()
            case "H":
                print(" Showing High Scores...")
                sleep(1)
                self.show_high_scores()
            case "C":
                print(" Creating New Profile...")
                sleep(1)
                self.create_new_profile()
            case "D":
                print(" Deleting Profile...")
                sleep(1)
                self.delete_profile()
            case "X":
                print(" Exiting Game...")
                sleep(1)
                system("cls")
                exit()
                
    def return_to_menu(self):
        input(" \n Press any key to return to menu...")
        self.display_menu_screen()
                
    # --- Menu option functions --- #
                
    def set_active_profile(self):
        system("cls")
        print("\n <--> <--> Select Profile <--> <--> \n")
        
        for i, profile in enumerate(self.player_profiles):
            (print(f" [{i+1}] {profile['player_name']}"))
        print()
        
        valid_input = [str(num) for num in range(1, len(self.player_profiles)+1)]
        
        profile_selection = 0
        while (profile_selection not in valid_input):
            profile_selection = str(input(" Selection : "))
            if profile_selection not in valid_input:
                print(" This input is invalid. Please enter a valid input.")
        
        profile_selection = int(profile_selection)-1
        self.active_profile = self.player_profiles[profile_selection]
        
        print(f"\n Active Profile set to... {self.active_profile['player_name']}")
        
        self.return_to_menu()
        
    def show_high_scores(self):
        system("cls")
        print("\n <--> <--> Highscores <--> <--> \n")
        
        profile_by_high_score = sorted(self.player_profiles, key=lambda profile: profile["player_highscore"])
        profile_by_high_score = reversed(profile_by_high_score[-5::])
        
        for i, profile in enumerate(profile_by_high_score):
            print(f" {i+1}. {profile['player_name']} -- {profile['player_highscore']}")
            
        self.return_to_menu()
    
    def create_new_profile(self):
        system("cls")
        print("\n <--> <--> Create Profile <--> <--> \n")
        
        valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_. "
        
        player_name_validity = False
        while player_name_validity == False:
            player_name = str(input(" Enter player name : "))
            
            if len(player_name) < 3:
                print(" Player name is too short. Player name should be longer than three characters.")
                player_name_validity = False
                continue
            
            for character in player_name:
                if character not in valid_characters:
                    print(" This input is invalid. Please enter a valid input.")
                    player_name_validity = False
                    continue
                else:
                    player_name_validity = True
            
        player_id = f"M-{len(self.player_profiles)+1}"
        
        new_player_profile = {
            "player_id" : player_id,
            "player_name" : player_name,
            "player_highscore" : 0
        }
        
        self.player_profiles.append(new_player_profile)
        profile_file_update = json.dumps(self.player_profiles, indent=4)
        
        with open("player_profiles.json", "wt") as profiles_file:
            profiles_file.write(profile_file_update)
        profiles_file.close()
            
        print(f"\n Created profile... {new_player_profile['player_name']}")
        
        self.return_to_menu()
        
    def delete_profile(self):
        system("cls")
        print("\n <--> <--> Delete Profile <--> <--> \n")
        
        for i, profile in enumerate(self.player_profiles):
            (print(f" [{i+1}] {profile['player_name']}"))
        print()
        
        valid_input = [str(num) for num in range(1, len(self.player_profiles)+1)]
        
        profile_selection = 0
        while (profile_selection not in valid_input):
            profile_selection = str(input(" Selection : "))
            if profile_selection not in valid_input:
                print(" This input is invalid. Please enter a valid input.")
                
        profile_selection = int(profile_selection)-1
        
        print(f"\n Deleting profile... {self.player_profiles[profile_selection]['player_name']}")
        
        if (self.active_profile != None) and (self.active_profile["player_id"] == self.player_profiles[profile_selection]["player_id"]):
            self.active_profile = None
        
        self.player_profiles.pop(profile_selection)
        
        profile_file_update = json.dumps(self.player_profiles, indent=4)
        
        with open("player_profiles.json", "wt") as profiles_file:
            profiles_file.write(profile_file_update)
        profiles_file.close()
        
        self.return_to_menu()
        
class player_guess():
    def __init__(self):
        pass

# NOTE: For the time being, the code must consist of four separate colors. Might change this later idk. Maybe this could be a difficulty setting?
class code():
    def __init__(self):
        self.code = self.generate_code()
    
    def generate_code(self):
        # TODO: Gonna make this stuff words... yeah.
        available_colors = ["91","92","93","94","95","96"]
        code_pattern = ''
        
        for _ in range(4):
            color_index = rnd.randrange(len(available_colors))
            chosen_color = available_colors[color_index]
            code_pattern += style_text("●", f"f{chosen_color}b40")
            available_colors.pop(color_index)
        
        return code_pattern    
        
class game_board():
    def __init__(self, active_player:dict):
        self.active_player = active_player
        self.code = code().generate_code()
        self.guess_rows = ["● ● ● ●" for _ in range(10)]
        self.hint_rows = ["○ ○ ○ ○" for _ in range(len(self.guess_rows))]
        self.guess_options = {
            "1":style_text("●", "f91b40"),
            "2":style_text("●", "f92b40"),
            "3":style_text("●", "f93b40"),
            "4":style_text("●", "f94b40"),
            "5":style_text("●", "f95b40"),
            "6":style_text("●", "f96b40")
        }
        
        self.turn_number = 0
        self.score = 0
        self.code_matching = False
    
    # --- The Play Function --- #
    
    def play(self):
        self.display_game_board()
        
        while self.code_matching != True:
            for _ in range(len(self.guess_rows)):
                player_guess = self.get_player_guess()
                self.evaluate_guess(player_guess)
                self.modify_score()
                self.increment_turn_number()
                
        
    # --- Game Operation Functions --- #
    
    def display_game_board(self):
        print()
        if self.active_player != None:
            print(f" Active Player : {self.active_player['player_name']}")
        else:
            print(" Active Player : Guest")
            
        print(f" Score : {self.score}")
        print(f" Turn Number : {self.turn_number}")
        
        line_break = " _________________\n"
        print(line_break)
        
        for row in self.guess_rows:
            row_index = self.guess_rows.index(row)
            print(f" {self.guess_rows[row_index]} | {self.hint_rows[row_index]}")
            
        print(line_break)
        
    def get_player_guess(self):
        pass
    
    def evaluate_guess(self, player_guess):
        pass
    
    def modify_score(self):
        pass
    
    def increment_turn_number(self):
        pass
    
        
def main():
    # menu = game_menu()
    # menu.display_menu_screen()
    
    game = game_board(None)
    game.play()

if __name__ == "__main__":
    main()