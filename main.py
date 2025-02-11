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
    dec = []
    bin = []

    #read the file line by line and store into the initialzed array
    file = open(filename, "r")
    for line in file :
        dec.append(int(line))
    
    # use the array to get each number and convert it into binary
    for i in dec :
        bin.append(convert_dec_to_bin(i))

    # return the array of numbers and array of binary values
    return dec, bin

def convert_bin_to_dec(bin) :
    result = 0
    exponent = 0    #keep track of the power of 2s

    for digit in reversed(str(bin)) :
        if digit == "1" :
            result += 2**exponent
        exponent += 1  #increment the exponent to handle the next digit
    
    return result

def file_convert_bin_to_dec(filename) :
    # store an array of all the numbers read in the file
    bin = []
    dec = []

    #read the file line by line and store into the initialzed array
    file = open(filename, "r")
    for line in file :
        bin.append(int(line))

    # use the array to get each number and convert it into decimals
    for i in bin :
        dec.append(convert_bin_to_dec(i))

    # return the array of numbers and array of binary values
    return bin, dec

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
    print("DISCLAIMER: A DECIMAL IS REFERED TO A WHOLE NUMBER IN THIS CONTEXT AS DECIMAL REFERS TO THE STANDARD BASE 10 SYSTEM\n")
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
    print("1. Manual Input\n2. File Input (from Working Directory)\n")
    
    input_process = input("Processing Option: ")      #select how to use the converter
    #error handling
    while ((input_process != '1' and input_process != '2') or not input_process.isdigit()) :
        input_process = input("Re-enter the Processing Option: ")

    if (input_process == '1') :
        # Manually input a decimal to convert into binary
        print("\nEnter a DECIMAL to convert it into its BINARY value!\n")
        decimal_num = input("[Decimal]: ")

        while (not decimal_num.isdigit()) :
            decimal_num = input("INVALID: Re-enter [Decimal]: ")
        
        decimal_num = int(decimal_num)

        #Run the entered number into the decimal-to-binary converter
        result = convert_dec_to_bin(decimal_num)

        print("\n[Binary]: " + result)
    
    elif (input_process == '2') :
        # use a file based input to convert a list of decimal numbers to binary
        print("\nEnter the file name you wish to get BINARY values from!\n")
        filename = input("[File]: ")

        while(not os.path.isfile(filename)) :   # check to see if the file exist in the working directory
            filename = input("INVALID: Re-enter [File]: ")

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
    print("1. Manual Input\n2. File Input (from Working Directory)\n")
    
    input_process = input("Processing Option: ")      #select how to use the converter
    #error handling
    while ((input_process != '1' and input_process != '2') or not input_process.isdigit()) :
        input_process = input("Re-enter the Processing Option: ")

    if (input_process == '1') :
        # Manually input a binary to convert into decimal
        print("\nEnter a BINARY to convert it into its DECIMAL value! Make sure it has only 0's and 1's\n")
        bin_num = input("[Binary]: ")
        #error handling:
        while (not set(bin_num).issubset({'0', '1'})) :     # checks if the str has only 0's and 1's
             bin_num = input("INVALID: Re-enter [Binary]: ")

        #Run the entered number into the binary-to-decimal converter
        result = convert_bin_to_dec(bin_num)

        print("\n[Decimal]: " + str(result))
    
    elif (input_process == '2') :
        # use a file based input to convert a list of binary numbers to decimal
        print("\nEnter the file name you wish to get DECIMAL values from!\n")
        filename = input("[File]: ")

        while(not os.path.isfile(filename)) :   # check to see if the file exist in the working directory
            filename = input("INVALID: Re-enter [File]: ")

        bin, dec = file_convert_bin_to_dec(filename)    #get a list of the binary numbers and the corresponding decimal numbers

        print("\n[List of Conversions] from " + filename)
        for i in range(len(dec)) :
            print("[Binary]: " + str(bin[i]) + "\n[Decimal]: " + str(dec[i]) + "\n")


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
while(True) :
    home_page()
    nav = input("User's Input: ")    # get user's entered input
    #error handling user input
    while ((nav != '1' and nav !=  '2' and nav != '3') or not nav.isdigit()) :
        nav = input("Re-enter User's Input: ")
    
    if(nav == '1') :
        # Clear terminal and navigate to Decimal-to-Binary Converter Sreen
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        decimal_to_binary()

        proceed = input("\nClick [Enter] to proceed back to home: ")
        #error handle
        while (proceed != "") :
            proceed = input("\nTry Again. Click [Enter] to proceed back to home: ")
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        

    elif (nav == '2') :
        # Clear terminal and navigate to Binary-to-Decimal Converter Sreen
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        binary_to_decimal()

        proceed = input("\nClick [Enter] to proceed back to home: ")
        #error handle
        while (proceed != "") :
            proceed = input("\nTry Again. Click [Enter] to proceed back to home: ")
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        
    elif(nav == '3') :
        # exit the program
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        exit_page()
        
        exit_option = input("User's Input: ")
        #error handling
        while (exit_option != 'y' and exit_option != 'n') :
            exit_option = input("Re-enter User's Input: ")
        
        if (exit_option != 'y') :
            # if user wishes to stay in the application, route user back to the home page
            os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        
        else :
            break