def simple_reflex_agent(user):
    if user == 'Happy':
        return 'smile'
    elif user == 'Sad':
        return 'cry'
    elif user == 'Angry':
        return 'frown'
    else:
        return 'no specific action'

while True:
    user = input('What do you feel? ').capitalize()

    agent = simple_reflex_agent(user)
    print(f'The agent responds your mood: {agent}')