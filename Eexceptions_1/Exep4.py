import random

#participants = ['Cathy','Fred','Jack','Tom', "Larry"]
participants = ['Cathy','Fred','Jack','Tom']


def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if 'Larry' not in my_participant_dict:
        return None
    elif my_participant_dict['Larry'] == 9:
        return True
    else:
        return False


print(Guess(participants))