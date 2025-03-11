import time

# Microservice B: History
if __name__ == "__main__":
    while (True) :
        time.sleep(1)

        # open the pipe.txt file to see if any commands/parameters have been sent to the file
        with open("historypipe.txt", "r") as f :
            content = f.read().splitlines() # splits on newlines (basically strtok() on '\n') and makes a list 

        if content :    # determine if there is content that exists in the pipe
            if (content[0] == "run") :
                print("Receiving history request")
                with open("history.txt", "r") as f :    # read the current state of the history file
                    results = f.readlines()     # read all the lines in the history.txt file
                # with the history results print it back to the pipe with added formatting
                # re-format the history contents for readability when printing back to the pipe
                formatted_results = [f"{line.strip().split()[0]} --> {line.strip().split()[1]}" for line in results]
                # write back to the pipe file
                with open("historypipe.txt", "w", encoding="utf-8") as f :
                    for line in formatted_results :
                        f.write(f"{line}\n")
                print("Histoy contents have bene written to the historypipe.txt")

        time.sleep(1)

                
                