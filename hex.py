import time

# Conversion table of remainders to 
# hexadecimal equivalent 
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
                    13: 'D', 14: 'E', 15: 'F'} 
  
  
# function which converts decimal value to hexadecimal value 
def decimalToHexadecimal(decimal): 
    hexadecimal = '' 
    while(decimal > 0): 
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal 
        decimal = decimal // 16
  
    return hexadecimal 

# Microservice D Implementation: Hexadecimal Converter
if __name__ == "__main__":
    while (True) :
        time.sleep(1)

    # open the pipe.txt file to see if any commands/parameters have been sent to the file
        with open("hexpipe.txt", "r") as f :
            content = f.read().splitlines() # splits on newlines (basically strtok() on '\n') and makes a list 
        
    # start the program if there are commands/parameters in the file
        if content :    # check to see if content is empty or not
            if (content[0] == "run") :
                # first check to see if the entered value is valid
                if (not content[1].isdigit()) :
                    print(f"Receiving request for hexadecimal conversion for {content[1]}")
                    with open("hexpipe.txt", "w", encoding="utf-8") as f :
                        f.write("invalid")
                        print("Invalid number was detected. INVALID was written to hexpipe.txt")

                else :                   
                    print(f"Receiving request for hexadecimal conversion for {content[1]}")
                    with open("hexpipe.txt", "w", encoding="utf-8") as f :
                        result = decimalToHexadecimal(int(content[1]))
                        f.write(f"{result}")
                        print(f"{result} was written to hexpipe.txt")
        time.sleep(1)