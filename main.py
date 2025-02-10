# Main program of CS 361 Course Project: Decimal-Binary Converter CLI
# Author: Nicholas Vu

import os

def convert_dec_to_bin(dec) :
    result = ""

    while dec > 0 :
        result = str(dec % 2) + result
        dec = dec // 2

    return result

def file_convert_dec_to_bin(filename) :
    # store an array of all the numbers read in the file
    nums = []
    binarys = []

    #read the file line by line and store into the initialzed array
    file = open(filename, "r")
    for line in file :
        nums.append(int(line))
    
    # use the array to get each number and convert it into binary
    for i in nums :
        binarys.append(convert_dec_to_bin(i))

    # return the array of numbers and array of binary values
    return nums, binarys

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
    print("1. Manual Input\n2. File Input\n")
    
    input_process = int(input("Processing Option: "))       #select how to use the converter

    if (input_process == 1) :
        # Manually input a decimal to convert into binary
        print("\nEnter a DECIMAL to convert it into its BINARY value!\n")
        decimal_num = int(input("[Decimal]: "))

        #Run the entered number into the decimal-to-binary converter
        result = convert_dec_to_bin(decimal_num)

        print("[Binary]: " + result)
    
    elif (input_process == 2) :
        # use a file based input to convert a list of decimal numbers to binary
        print("\nEnter the file name you wish to get BINARY values from!\n")
        filename = input("[File]: ")

        dec, bin = file_convert_dec_to_bin(filename)    #get a list of the decimal numbers and the corresponding binary numbers

        print("\n[List of Conversions] from " + filename)
        for i in range(len(dec)) :
            print("[Decimal]: " + str(dec[i]) + "\n[Binary]: " + str(bin[i]) + "\n")
            

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
    print("1. Manual Input\n2. File Input\n")


def exit_page() :
    print(r""" 
      ______      _ _   
     |  ____|    (_) |  
     | |__  __  ___| |_ 
     |  __| \ \/ / | __|
     | |____ >  <| | |_ 
     |______/_/\_\_|\__|
                                                                                                                                                                
    """)
    print("Are you sure you want to exit the program? (y/n)\n")


# Main Function:
home_page()

nav = int(input("User's Input: "))    # get user's entered input

if(nav == 1) :
    # Clear terminal and navigate to Decimal-to-Binary Converter Sreen
    os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
    decimal_to_binary()

elif (nav == 2) :
    # Clear terminal and navigate to Binary-to-Decimal Converter Sreen
    os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
    binary_to_decimal()
elif(nav == 3) :
    # exit the program
    os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
    exit_page()
