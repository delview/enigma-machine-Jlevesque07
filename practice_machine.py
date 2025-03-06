# Make a list called "messages" containing a series of short text messages. 

def show_messages():
    print(messages)

# def send_messages():
#     for item in messages:
#         print(f"Message '{item}' sent. ")
#         sent_messages.append(item)
#     for item in messages:
#         messages.remove(item)
#     return sent_messages

# def send_messages(sent_messages:list):
#     global messages
#     while messages:
#         item = messages.pop(0)
#         print(item)
#         sent_messages.append(item)
   
#     return sent_messages

messages = []
sent_messages = []
messages.append("You're done.")
messages.append("You look like a gnome.")
messages.append("Computer class.")
send_messages()
print(messages, sent_messages)



# 3. Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides and it should print a summary of the sandwich that's being ordered. '
# 'Call the function three times using a different number of arguments each time.

