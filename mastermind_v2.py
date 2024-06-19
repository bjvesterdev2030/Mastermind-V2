from pycolor import style_text
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
    print(menu.logo)

if __name__ == "__main__":
    main()