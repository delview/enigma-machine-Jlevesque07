



# def encoder function 
# takes the string, makes it a list, translates each letter into morse code, shows the user the encoded message
def encode(string: str) -> list:
    encoded_message = []
    for letter in string:
        if letter == 'a':
            encoded_message.append(".-")
        elif letter == 'b':  
            encoded_message.append("-...")
        elif letter == 'c':
            encoded_message.append("-.-.")
        elif letter == 'd':
            encoded_message.append("-..")
        elif letter == 'e':
            encoded_message.append(".")
        elif letter == 'f':
            encoded_message.append("--.")
        elif letter == 'g':
            encoded_message.append("-...")
        elif letter == 'h':
            encoded_message.append("....")
        elif letter == 'i':
            encoded_message.append("..")
        elif letter == 'j':
            encoded_message.append(".---")
        elif letter == 'k':
            encoded_message.append("-.-")
        elif letter == 'l':
            encoded_message.append(".-..")
        elif letter == 'm':
            encoded_message.append("--")
        elif letter == 'n':
            encoded_message.append("-.")
        elif letter == 'o':
            encoded_message.append("---")
        elif letter == 'p':
            encoded_message.append(".--.")
        elif letter == 'q':
            encoded_message.append("--.-")
        elif letter == 'r':
            encoded_message.append(".-.")
        elif letter == 's':
            encoded_message.append("...")
        elif letter == 't':
            encoded_message.append("-")
        elif letter == 'u':
            encoded_message.append("..-")
        elif letter == 'v':
            encoded_message.append("...-")
        elif letter == 'w':
            encoded_message.append(".--")
        elif letter == 'x':
            encoded_message.append("-..-")
        elif letter == 'y':
            encoded_message.append("-.--")
        elif letter == 'z':                      
            encoded_message.append("--..")
        else:
            encoded_message.append("----")
    print(encoded_message)

    
# def decoder function 
# takes a list of morse codes, translates them into letters, regroups the letters into a string, shows the user the string


# define dictionary for morse code to letter translations
string = input("Input a message. ")
encode(string)
# user interface, options to encode or decode