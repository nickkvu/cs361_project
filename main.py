# Main program of CS 361 Course Project: Decimal-Binary Converter CLI
# Author: Nicholas Vu

import os

# Home Page Screen:
def home_page() :
    # print home screen messages to terminal
    print(r""" 
      _    _                      
     | |  | |                     
     | |__| | ___  _ __ ___   ___ 
     |  __  |/ _ \| '_ ` _ \ / _ \
     | |  | | (_) | | | | | |  __/
     |_|  |_|\___/|_| |_| |_|\___|
                                                             
    """)

    print("Be able to quickly conversions with binary and decimal numbers!\nEnter an integer corresponding to navigation option you wish to chose.\n")
    print("Navigation: ")
    print("1. Decimal-to-binary Converter\n2. Binary-to-decimal Converter\n3. Exit\n")

def decimal_to_binary() :
    # print the decimal to binary converter screen messages to terminal
    print(r""" 

     _____            _                 _   ____  _                           _____                          _            
    |  __ \          (_)               | | |  _ \(_)                         / ____|                        | |           
    | |  | | ___  ___ _ _ __ ___   __ _| | | |_) |_ _ __   __ _ _ __ _   _  | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
    | |  | |/ _ \/ __| | '_ ` _ \ / _` | | |  _ <| | '_ \ / _` | '__| | | | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
    | |__| |  __/ (__| | | | | | | (_| | | | |_) | | | | | (_| | |  | |_| | | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
    |_____/ \___|\___|_|_| |_| |_|\__,_|_| |____/|_|_| |_|\__,_|_|   \__, |  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                      __/ |                                               
                                                                     |___/                                                
    """)
    print("Would you like to enter a decimal to the CLI or enter the name of a file: \n")
    print("1. Manual Input\n2. File Input")

def binary_to_decimal() :
    print(r""" 
      ____  _                          _____            _                 _    _____                          _            
     |  _ \(_)                        |  __ \          (_)               | |  / ____|                        | |           
     | |_) |_ _ __   __ _ _ __ _   _  | |  | | ___  ___ _ _ __ ___   __ _| | | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
     |  _ <| | '_ \ / _` | '__| | | | | |  | |/ _ \/ __| | '_ ` _ \ / _` | | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
     | |_) | | | | | (_| | |  | |_| | | |__| |  __/ (__| | | | | | | (_| | | | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
     |____/|_|_| |_|\__,_|_|   \__, | |_____/ \___|\___|_|_| |_| |_|\__,_|_|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                __/ |                                                                                      
                               |___/                                                                                                                                  
    """)
    print("Would you like to enter a decimal to the CLI or enter the name of a file: \n")
    print("1. Manual Input\n2. File Input")

def exit_page() :
    print(r""" 
      ______      _ _   
     |  ____|    (_) |  
     | |__  __  ___| |_ 
     |  __| \ \/ / | __|
     | |____ >  <| | |_ 
     |______/_/\_\_|\__|
                                                                                                                                                                
    """)
    print("Are you sure you want to exit the program? (y/n)")


# Main Function:
home_page()

input = int(input("User's Input: "))    # get user's entered input

if(input == 1) :
    # Clear terminal and navigate to Decimal-to-Binary Converter Sreen
    os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
    decimal_to_binary()

elif (input == 2) :
    # Clear terminal and navigate to Binary-to-Decimal Converter Sreen
    os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
    binary_to_decimal()

elif(input == 3) :
    # exit the program
    os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
    exit_page()
