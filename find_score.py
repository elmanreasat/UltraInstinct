import parsedict


def anger(emotions):

    lst = emotions
    index = 0
    total = 0

    while index < len(lst):
        total += int(lst[index].get('anger'))
        index += 1
    return total * len(emotions)




def disgust(emotions):

    lst = emotions
    index = 0
    total = 0

    while index < len(lst):
        total += int(lst[index].get('disgust'))
        index += 1
    return total * len(emotions)


def fear(emotions):
    lst = emotions
    index = 0
    total = 0

    while index < len(lst):
        total += int(lst[index].get('fear'))
        index += 1
    return total * len(emotions)


def joy(emotions):
    lst = emotions
    index = 0
    total = 0

    while index < len(lst):
        total += int(lst[index].get('joy'))
        index += 1
    return total * len(emotions)



def hate(emotions):
    lst = emotions
    index = 0
    total = 0

    while index < len(lst):
        total += int(lst[index].get('hate'))
        index += 1
    return total * len(emotions)


def main():
    kw = parsedict.parsedict_kw
    emotions = parsedict.parsedict_emotion
    emotional_value = anger(emotions) + fear(emotions) /n
    + hate(emotions) + joy(emotions) + disgust(emotions)


    if 'gun' or 'kill' or 'murder' or 'hate' or 'attack' not in kw and /n
    emotional_value == 0:
        return "Harmless (0)"


    if 'gun' and ('kill' or 'murder') and 'joy' in kw and emotional_value > 4 :

        return "Pscyho(5)"

    if 'gun' or 'kill' or 'murder' or 'joy' in kw and emotional_value > 3:

        return "Potential Psycho (4)"

    if 'gun' or 'kill' or 'murder' or 'joy' in kw and emotional_value < 2:

        return "Mild (3)"

    if 'gun' or 'kill' or 'murder' or 'joy' in kw and emotional_value < 1:

        return "Weak (2)"

    else:

        return " Unicorns (1)"
