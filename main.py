# Main program of CS 361 Course Project: Decimal-Binary Converter CLI
# Author: Nicholas Vu

import os
import time

# Function to get number type
def get_type(prompt):
    while True:
        # Prompt user for input
        number_type = input(prompt)
        if number_type in ['int', 'float']:
            return number_type
        # Print error if user did not type valid number type
        else: 
            print("Erorr: Invalid input. Enter int or float")

# Function get number type
def get_number(prompt, number_type):
    while True:
        try:
            # Prompt user for a number
            number = input(prompt)
            if (number_type == 'int'):
                return int(number)
            elif (number_type == 'float'):
                return float(number)
            
        # Print error if user didn't enter int or float
        except ValueError:
            if (number_type == 'int'):
                print("ERROR: Please enter an integer")
            else:
                print("ERROR: Please enter a number")

# Function get decimal place
def get_decimal(prompt, number_type):
    while True:
        try:
            # Prompt user for decimal place
            decimal = int(input(prompt))

            # Reprompt user if they entered invalid decimal place
            if (number_type == 'int' and decimal != 0):
                print("ERROR: Enter 0 for integer")
                continue
            if (number_type == 'float' and decimal < 1):
                print("ERROR: Enter a number greater than 0 for float")
                continue

            # Return if the input was valid
            return decimal
        
        # Print error if user didn't enter number
        except ValueError:
            print("Error: Please enter a valid decimal place")

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

# log the conversion into the history file
def log_conversion(input_val, converted_val, filename) :
    with open(filename, "a") as file :
        file.write(f"{input_val} {converted_val}\n")

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
    print("1. Decimal-to-binary Converter\n2. Binary-to-decimal Converter\n3. History\n4. Quick Reference\n5. Hexadeciaml Converter\n6. Exit\n")

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
        # ask if you user would like ther generate a random number: 
        input_type = input("\nDo you want to generate a random number for the conversion? (y/n): ")
        if (input_type == "y") :
            minimum = get_number("\nEnter a minimum for your random number: ", "int")
            maximum = get_number("Enter a maximum for your random number: ", "int")
            # dont ask for option to choose from int or float, since my converter only works with ints
            # Combine user inputs as a csv string
            data = ["int", minimum, maximum, 0]
            csv_data = ",".join(map(str, data))

            print("\nWriting data...")
            # Sleep for 4 seconds
            for i in range(3):
                print(".")
                time.sleep(1)

            with open("data.csv", "w") as file:
                # Write csv string into data file
                file.write(f"{csv_data}")
                
            with open("data.csv", "r") as file:
                # Read data file
                file_string = file.readline().rstrip()

            # Wait to read correct input from file
            while True:
                with open("data.csv", "r") as file:
                    file_string = file.readline().rstrip()

                if file_string != csv_data:
                    break  # Exit the loop when the file changes

                print(".")
                time.sleep(2)
                
            # Print random generated number to program
            print(f"Generated random decimal number between {minimum} and {maximum}: {file_string}")
            
            decimal_num = int(file_string)

            #Run the entered number into the decimal-to-binary converter
            result = convert_dec_to_bin(decimal_num)

            #log the result into the txt file
            log_conversion(decimal_num, result, "history.txt")

            print("\n[Binary]: " + result)
        
        else :
            # Manually input a decimal to convert into binary
            print("\nEnter a DECIMAL to convert it into its BINARY value!\n")
            decimal_num = input("[Decimal]: ")

            while (not decimal_num.isdigit()) :
                decimal_num = input("INVALID: Re-enter [Decimal]: ")
            
            decimal_num = int(decimal_num)

            #Run the entered number into the decimal-to-binary converter
            result = convert_dec_to_bin(decimal_num)

            #log the result into the txt file
            log_conversion(decimal_num, result, "history.txt")

            print("\n[Binary]: " + result)
    
    elif (input_process == '2') :
        # use a file based input to convert a list of decimal numbers to binary
        print("\nEnter the file name you wish to get BINARY values from!\n")
        filename = input("[File]: ")

        while(not os.path.isfile(filename)) :   # check to see if the file exist in the working directory
            filename = input("INVALID: Re-enter [File]: ")

        dec, bin = file_convert_dec_to_bin(filename)    #get a list of the decimal numbers and the corresponding binary numbers
        
        # log all conversions to the history file
        for i in range(len(dec)) :
            log_conversion(dec[i], bin[i], "history.txt")

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

        #log the result into the txt file
        log_conversion(bin_num, result, "history.txt")

        print("\n[Decimal]: " + str(result))
    
    elif (input_process == '2') :
        # use a file based input to convert a list of binary numbers to decimal
        print("\nEnter the file name you wish to get DECIMAL values from!\n")
        filename = input("[File]: ")

        while(not os.path.isfile(filename)) :   # check to see if the file exist in the working directory
            filename = input("INVALID: Re-enter [File]: ")

        bin, dec = file_convert_bin_to_dec(filename)    #get a list of the binary numbers and the corresponding decimal numbers

        # log all conversions to the history file
        for i in range(len(dec)) :
            log_conversion(bin[i], dec[i], "history.txt")

        print("\n[List of Conversions] from " + filename)
        for i in range(len(dec)) :
            print("[Binary]: " + str(bin[i]) + "\n[Decimal]: " + str(dec[i]) + "\n")

def history_page() :
    print(r"""
     _    _ _     _                   
    | |  | (_)   | |                  
    | |__| |_ ___| |_ ___  _ __ _   _ 
    |  __  | / __| __/ _ \| '__| | | |
    | |  | | \__ \ || (_) | |  | |_| |
    |_|  |_|_|___/\__\___/|_|   \__, |
                                __/ |
                                |___/ 
    """)
    print("List of all conversions made by the user during this process:\n")
    
    # Microservice B: Histoy Implementation
        # write to the pipe file for the history mircoservice (historypipe.txt)
    with open("historypipe.txt", "w", encoding="utf-8") as file :
        file.write("run")   # tell the microservice to get the history and print it
    
    print("Connecting to Microservice B: History...")
    time.sleep(2)

    # wait on the Microservice B
    print("Requesting contents of history file from Microservice B server\n")
    while (True) :
        with open("historypipe.txt", "r") as f :
            print("RECEIVED LOGS:\n")
            results = f.readlines()
            for line in results :
                print(f"{line}")
            break
        time.sleep(0.5)


def quick_ref_page() :
    print(r""" 
   ____        _      _      _____       __                             
  / __ \      (_)    | |    |  __ \     / _|                            
 | |  | |_   _ _  ___| | __ | |__) |___| |_ ___ _ __ ___ _ __   ___ ___ 
 | |  | | | | | |/ __| |/ / |  _  // _ \  _/ _ \ '__/ _ \ '_ \ / __/ _ \
 | |__| | |_| | | (__|   <  | | \ \  __/ ||  __/ | |  __/ | | | (_|  __/
  \___\_\\__,_|_|\___|_|\_\ |_|  \_\___|_| \___|_|  \___|_| |_|\___\___|                                                                                                                             
    """)
    print("Displaying commonly used binary and decimal conversions (0-10) which can be used as a quick reference guide.")

    # Microservice C: Quick Reference

    # ask user if they wish to store the quick refernece data into a text file
    quick_ref_option = input("Would you like to save the quick reference list into a file? (y/n): ")      #select how to use the converter
    #error handling
    while (quick_ref_option != 'y' and quick_ref_option != 'n') :
            quick_ref_option = input("Re-enter User's Input: ")
    
    if (quick_ref_option == 'y') :
        # write to the pipe file for the requick ref mircoservice (qrefpipe.txt)
        with open("qrefpipe.txt", "w", encoding="utf-8") as file :
            file.write("run save")   # tell the microservice to get the quick reference with the option to save it to a file
    
    elif (quick_ref_option == 'n') :
        # write to the pipe file for the requick ref mircoservice (qrefpipe.txt)
        with open("qrefpipe.txt", "w", encoding="utf-8") as file :
            file.write("run nosave")   # tell the microservice to get the quick reference with the option to save it to a file

    
    print("\nConnecting to Microservice C: Quick Reference...")
    time.sleep(2)

    # wait on Microsercive C (by this point, either option should supply the same response in the pipe file)
    print("Requesting quick reference content from Microservice C server\n")
    while (True) :
        with open("qrefpipe.txt", "r") as f :
            print("COMMON CONVERSIONS (0-10):\n")
            results = f.readlines()
            for line in results :
                print(f"{line}")
            break
        time.sleep(0.5)

def hexadecimal_page() :
    print(r"""
     _    _                    _           _                 _    _____                          _            
    | |  | |                  | |         (_)               | |  / ____|                        | |           
    | |__| | _____  ____ _  __| | ___  ___ _ _ __ ___   __ _| | | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
    |  __  |/ _ \ \/ / _` |/ _` |/ _ \/ __| | '_ ` _ \ / _` | | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
    | |  | |  __/>  < (_| | (_| |  __/ (__| | | | | | | (_| | | | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
    |_|  |_|\___/_/\_\__,_|\__,_|\___|\___|_|_| |_| |_|\__,_|_|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
    """)
    print("\nEnter a DECIMAL to convert it into its HEXADECIMAL value!\n")
    decimal_num = input("[Decimal]: ")

    # Microservice D: Hexadecimal Converter (Decimal to Hexidecimal)
    with open("hexpipe.txt", "w", encoding="utf-8") as file :
        file.write(f"run\n{decimal_num}")   # tell the microservice to get the history and print it

    print("\nConnecting to Microservice D: Hexadecimal Converter...")
    time.sleep(2)

    # wait on the Microservice D
    print(f"Requesting hexadecimal conversion for {decimal_num} from Microservice D server\n")
    while (True) :
        with open("hexpipe.txt", "r") as f :
            result = f.read().strip()
            if (result == "invalid") :
                print(f"{decimal_num} is an INVALID input\n")
            else :
                print(f"Recieved Hexadecimal result: {result}")
            break
        time.sleep(0.5)


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
    while ((nav != '1' and nav != '2' and nav != '3' and nav != '4' and nav != '5' and nav != '6' and nav != '7') or not nav.isdigit()) :
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
        
    elif (nav == '3') :
        # Clear terminal and navigate to the history page
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        history_page()
        
        proceed = input("\nClick [Enter] to proceed back to home: ")
        #error handle
        while (proceed != "") :
            proceed = input("\nTry Again. Click [Enter] to proceed back to home: ")
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface

    elif (nav == '4') :
        # Clear terminal and navigate to the quick reference page
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        quick_ref_page()

        proceed = input("\nClick [Enter] to proceed back to home: ")
        #error handle
        while (proceed != "") :
            proceed = input("\nTry Again. Click [Enter] to proceed back to home: ")
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface

    elif (nav == '5') :
        # Clear terminal and navigate to the hexadeciaml page page
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        hexadecimal_page()
        
        proceed = input("\nClick [Enter] to proceed back to home: ")
        #error handle
        while (proceed != "") :
            proceed = input("\nTry Again. Click [Enter] to proceed back to home: ")
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface

    elif (nav == '6') :
        # exit the program
        os.system('cls' if os.name == 'nt' else 'clear')    #clear the terminal to make cleaner interface
        exit_page()
        
        exit_option = input("User's Input: ")
        #error handling
        while (exit_option != 'y' and exit_option != 'n') :
            exit_option = input("Re-enter User's Input: ")
        
        if (exit_option != 'y') :
            # if user wishes to stay in the application, route user back to the home page
            os.system('cls' if os.name == 'nt' else 'clear')    # clear the terminal to make cleaner interface
        
        else :
            # clear history for the next process
            with open("history.txt", "w") as f:
                pass  # Opening in 'w' mode clears the file

            # clear all other pipe files for next process start up
            with open("historypipe.txt", "w") as f:
                pass  # Opening in 'w' mode clears the file

            with open("qrefpipe.txt", "w") as f:
                pass  # Opening in 'w' mode clears the file

            with open("hexpipe.txt", "w") as f:
                pass  # Opening in 'w' mode clears the file
            break