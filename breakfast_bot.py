import time

delay = 1

def print_and_wait(string):
    print(string)
    time.sleep(delay)

def ask_question(question, response1, response2):
    while True:
        response = input(question + "\n").lower()
        
        if response1 in response:
            print_and_wait(response1 +" it is!")
            break
        
        elif response2 in response:
            print_and_wait(response2 + " it is!")
            break
        
        else:
            print_and_wait("Sorry, I don't understand.")

    return response

print_and_wait("Hello! I am Bob, the Breakfast Bot.")
print_and_wait("Today we have two breakfasts available.")
print_and_wait("The first is waffles with strawberries and whipped cream.")
print_and_wait("The second is sweet potato pancakes with butter and syrup.")

while True:
    food   = ask_question("Please place your order. Would you like waffles or pancakes?", "waffles", "pancakes")
    drink  = ask_question("What do want to drink?", "coffee", "juice")
    syrup  = ask_question("Do you want syrup?", "yes", "no")
    butter = ask_question("What kind of butter do you want?", "unsalted", "salted")
    
    print(f"You ordered {food}, with {butter} butter and a {drink}")
    print_and_wait("Your order will be ready shortly.")
    order_again = ask_question("Would you like to place another order? Please say 'yes' or 'no'.?", "no", "yes")
    
    if 'no' in order_again:
        break # We need this last break statement to exit the outer loop.