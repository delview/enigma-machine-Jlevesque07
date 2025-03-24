# def encoder function 
def encode(string: str) -> list: # takes the string, makes it a list

    encoded_message = []
    for letter in string: # translates each letter into morse code
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
            encoded_message.append("..-.")
        elif letter == 'g':
            encoded_message.append("--.")
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
    encoded_message = ' '.join(encoded_message)
    print(f"Your encoded message: {encoded_message}") # shows the user the encoded message



# def decoder function 
def decode(list: str) -> str: # # takes a list of morse codes
    
    decoded_message = []
    for code in list: # translates them into letters
        if code == ".-":
            decoded_message.append("a")
        elif code == "-...":
            decoded_message.append("b")
        elif code == "-.-.":
            decoded_message.append("c")
        elif code == "-..":
            decoded_message.append("d")
        elif code == ".":
            decoded_message.append("e")
        elif code == "..-.":
            decoded_message.append("f")
        elif code == "--.":
            decoded_message.append("g")
        elif code == "....":
            decoded_message.append("h")
        elif code == "..":
            decoded_message.append("i")
        elif code == ".---":
            decoded_message.append("j")
        elif code == "-.-":
            decoded_message.append("k")
        elif code == ".-..":
            decoded_message.append("l")
        elif code == "--":
            decoded_message.append("m")
        elif code == "-.":
            decoded_message.append("n")
        elif code == "---":
            decoded_message.append("o")
        elif code == ".--.":
            decoded_message.append("p")
        elif code == "--.-":
            decoded_message.append("q")
        elif code == ".-.":
            decoded_message.append("r")
        elif code == "...":
            decoded_message.append("s")
        elif code == "-":
            decoded_message.append("t")
        elif code == "..-":
            decoded_message.append("u")
        elif code == "...-":
            decoded_message.append("v")
        elif code == ".--":
            decoded_message.append("w")
        elif code == "-..-":
            decoded_message.append("x")
        elif code == "-.--":
            decoded_message.append("y")
        elif code == "--..":
            decoded_message.append("z")
        else:
            decoded_message.append(" ")

    decoded_message = ''.join(decoded_message) # regroups the letters into a string
    print(f"Your decoded message: {decoded_message}.") # shows the user the string




# user interface
while True: 
    option = input("Would you like to encode a message [1]? Decode a message [2]? Or exit the program [3]? ").strip().lower()
        
    if option == "1": # option to encode
        string = input("Input a message to be encoded. ").lower()
        encode(string)

    elif option == "2": # option to decode
        list = input("Please enter an encoded message to be decoded. ")
        list = list.split()
        decode(list)

    elif option == "3": # option to quit
        print("Thank you for using my program. Have a good day. ")
        exit()

    else:
        print("Please enter either 1, 2, or 3.")