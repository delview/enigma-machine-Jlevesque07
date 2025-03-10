# Make a list called "messages" containing a series of short text messages. 

def show_messages():
    print(messages)

def send_messages(sent_messages:list):
    while messages:
        item = messages.pop(0)
        print(item)
        sent_messages.append(item)
   
    return sent_messages

def sandwich(items: list) -> list:
    print(f"The toppings on this sandwich will be: {items}. ")



messages = []
sent_messages = []
messages.append("You're done.")
messages.append("You look like a gnome.")
messages.append("Computer class.")
send_messages(sent_messages)
print(messages, sent_messages)

sandwiches = 3
while sandwiches > 0:
    if sandwiches == 3:
        sandwich_1 = []
        while True:
            topping = input("What topping do you want on your sandwich? ").strip().lower()
            sandwich_1.append(topping)
            exit = input("Would you like to choose another topping? ").strip().lower()
            if exit == "y":
                pass
            else: 
                sandwich(sandwich_1)
                sandwiches = sandwiches - 1
                break

    elif sandwiches == 2:
        sandwich_2 = []
        while True:
            topping = input("What topping do you want on your sandwich? ").strip().lower()
            sandwich_2.append(topping)
            exit = input("Would you like to choose another topping? ").strip().lower()
            if exit == "y":
                pass
            else: 
                sandwich(sandwich_2)
                sandwiches = sandwiches - 1
                break

    else:
        sandwich_3 = []
        while True:
            topping = input("What topping do you want on your sandwich? ").strip().lower()
            sandwich_3.append(topping)
            exit = input("Would you like to choose another topping? ").strip().lower()
            if exit == "y":
                pass
            else: 
                sandwich(sandwich_3)
                sandwiches = sandwiches - 1
                break
        
        
        





