



# def encoder function 
# takes the string, makes it a list, translates each letter into morse code, shows the user the encoded message


# def decoder function 
# takes a list of morse codes, translates them into letters, regroups the letters into a string, shows the user the string


# define dictionary for morse code to letter translations
codes = {'a':'.-' , 'b':'-...' , 'c':'-.-.' , 'd':'-..', 'e':'.' , 'f':'..-.' , 'g':'--.' , 'h':'....' , 'i':'..' , 'j':'.---' , 'k':'-.-' , 'l':'.-..' , 'm':'--' , 'n':'-.' , 'o':'---' , 'p':'.--.' , 'q':'--.-' , 'r':'.-.' , 's':'...' , 't':'-' , 'u':'..-' , 'v':'...-' , 'w':'.--' , 'x':'-..-' , 'y':'-.--' , 'z':'--..'}
 
# user interface, options to encode or decode