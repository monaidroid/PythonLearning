# This file contains If else if statements
# One type of Chatbot program basic..

while True:
    user_input: str = input('You :')
    if user_input.lower() == 'how are you?' :
        print('Alice, I am Good!, What about you?')
    elif user_input.lower() == 'hello' :
        print('Alice, Hello!')
    elif user_input.lower() == 'bye' :
        print('Alice : Good Bye!')
    else :
        print("Sorry, I didn't understand it.")
       