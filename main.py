def get_user_name():
    return input('What is your name? ')

def ask_question():
    return input('How are you feeling today? ')

def chatbot_response(response, mood_tracker):
    if 'good' in response.lower() or 'great' in response.lower():
        mood_tracker.append('positive')
        return 'I\'m glad to hear that!'
    elif 'down' in response.lower() or 'bad' in response.lower():
        mood_tracker.append('negative')
        return 'I\'m sorry to hear that. Would you like some advice to cheer you up?'
    else:
        mood_tracker.append('neutral')
        return 'Thanks for sharing.'

def favorite_color():
    return input('What is your favorite color? ')

def offer_help():
    print("\nI can help with:")
    print("1. Share a fun fact")
    print("2. Tell a joke")
    print("3. Give advice")
    print("4. Exit\n")
    return input("Choose an option (1-4): ")

def fun_fact():
    return "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!"

def joke():
    return "Why don't skeletons fight each other? Because they don't have the guts!"

def advice():
    return "Take one step at a time, and don't hesitate to ask for help when you need it. Every small step counts!"

def analyze_mood(mood_tracker):
    if mood_tracker.count('positive') > mood_tracker.count('negative'):
        return "It seems like you're having a good day overall!"
    elif mood_tracker.count('negative') > mood_tracker.count('positive'):
        return "It seems like you've had some tough moments today. Remember, it’s okay to feel this way, and things can get better."
    else:
        return "You've had a mix of feelings today. Thanks for sharing with me!"

def main():
    print('Welcome to Elite 101!')
    user_name = get_user_name()
    print(f'Nice to meet you, {user_name}!')
    mood_tracker = []

    while True:
        user_response = ask_question()
        print(chatbot_response(user_response, mood_tracker))

        color = favorite_color()
        print(f'Wow, {color} is a great choice!')

        while True:
            option = offer_help()
            if option == '1':
                print(fun_fact())
            elif option == '2':
                print(joke())
            elif option == '3':
                print(advice())
            elif option == '4':
                print(analyze_mood(mood_tracker))
                print(f'Thank you for chatting, {user_name}! Have a great day!')
                return
            else:
                print("I didn't understand that. Please choose a valid option.")

main()
