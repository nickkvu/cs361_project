import time

def qref_nosave(common_conversions) :
    with open("qrefpipe.txt", "w",  encoding="utf-8") as f:
        for conversion in common_conversions :
            f.write(conversion + "\n")
        print("Common conversions was written to qrefpipe.txt\n")

def qref_save(common_conversions) :
    with open("saved_quick_reference.txt", "w",  encoding="utf-8") as f:
        for conversion in common_conversions :
            f.write(conversion + "\n")
    
    with open("qrefpipe.txt", "w",  encoding="utf-8") as f:
        for conversion in common_conversions :
            f.write(conversion + "\n")
        print("Common conversions was written to qrefpipe.txt and saved to saved_quick_reference.txt\n")


# Microservice C Implementation: Quick Reference
if __name__ == "__main__":
    common_conversions = [
        "0 --> 0", 
        "1 --> 1",
        "2 --> 10",
        "3 --> 11",
        "4 --> 100",
        "5 --> 101",
        "6 --> 110",
        "7 --> 111",
        "8 --> 1000",
        "9 --> 1001",
        "10 --> 1010"
        ]
    while (True) :
        time.sleep(1)   # sleep of 1 second for some "buffer" time before reading the pipe.txt file

        # open the pipe.txt file to see if any commands/parameters have been sent to the file
        with open("qrefpipe.txt", "r") as f :
            content = f.read().splitlines() # splits on newlines (basically strtok() on '\n') and makes a list 
        
        # start the program if there are commands/parameters in the file
        if content :    # check to see if content is empty or not
            if (content[0] == "run nosave") :
                print("Receiving request for quick reference without file-saving\n")
                qref_nosave(common_conversions)
            elif (content[0] == "run save") :
                print("Receiving request for quick reference with file-saving\n")
                qref_save(common_conversions)
            

