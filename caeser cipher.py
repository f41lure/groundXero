
import cs50
import sys

def main():
    if len(sys.argv) != 2:
        print("You should provide cmd line arguments!")
        exit(1)
    key = int(sys.argv[1])
    phrase = cs50.get_string()
 
    list = phrase.split()
    newPhrase = ""
    for word in list:
        conversion = '' 
        for ch in word:  
           conversion += (chr)((ord(ch) - ord("a") + key) % 26 + ord("a"))  
        newPhrase = newPhrase + conversion + " " 
    print(newPhrase)  

if __name__ == "__main__":
    main()

                            






