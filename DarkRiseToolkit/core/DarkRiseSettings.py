from termcolor import colored

class DarkRiseSettings(object):
    def __init__(self):
        self.Title = """
    _____          _____  _  __  _____  _____  _____ ______ 
    |  __ \   /\   |  __ \| |/ / |  __ \|_   _|/ ____|  ____|
    | |  | | /  \  | |__) | ' /  | |__) | | | | (___ | |__   
    | |  | |/ /\ \ |  _  /|  <   |  _  /  | |  \___ \|  __|  
    | |__| / ____ \| | \ \| . \  | | \ \ _| |_ ____) | |____ 
    |_____/_/    \_\_|  \_\_|\_\ |_|  \_\_____|_____/|______|

        """
        self.Copyright = """
    }-----------{+} Coded By DARK RISE Team {+}-------------{
        """

    def logo(self):
        print(colored(self.Title, "green", attrs=["bold"]))
        print(colored(self.Copyright, "red", attrs=["bold"]))