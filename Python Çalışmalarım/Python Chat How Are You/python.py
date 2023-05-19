
user = input('How are you')
words = "sad", "fine", "good", "not", "okay"

def talk() :

    if words[0] in user : 
        print('Im sad')
    elif words[1] in user : 
        print('Its so nice')
    elif words[2] in user : 
        print('Im happy to hear that')
    elif words[3] in user : 
        print(':(')
    elif words[4] in user : 
        print(':)')
    else : 
        print('Ive asked you')
talk()