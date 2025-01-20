def get_user_name():
    return input('What is your name? ')

def ask_question():
    return input('How are you feeling today? ')

def chatbot_response(response):
    if 'good' in response.lower() or 'great' in response.lower():
        print('I\'m glad to hear that!')
    elif 'down' in response.lower() or 'bad' in response.lower():
        print('I\'m sorry to hear that. I hope your day gets better.')
    else:
        print('Thanks for sharing.')

def favorite_color():
    return input('What is your favorite color? ')

def main():
    print('Welcome to Elite 101!')
    user_name = get_user_name()
    print('Nice to meet you, ' + user_name + '!')

    user_response = ask_question()
    chatbot_response(user_response)

    color = favorite_color()
    print('Wow, ' + color + ' is a great choice!')

    print('Thanks for chatting with me, ' + user_name + '.')

main()
