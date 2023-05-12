
# # import random

# # launguage = ["which language is this?", "какой это язык?", "Welche Sprache ist das?", "kokia tai kalba?", "hvaða tungumál er þetta"]

# # randomlaunguage = random.choice(launguage)
# # exam = print(randomlaunguage)

# # answeringilizce = launguage[0] = "ingilizce"
# # answerrusça = launguage[1] = "rusça"
# # answeralmanca = launguage[2] = "almanca"
# # answerlitvanca = launguage[3] = "litvanca"
# # answerizlandaca = launguage[4] = "izlandaca"

# # answer = input("bu hangi dil? :")

# # if answer == answeringilizce or answer == answeralmanca or answer == answerizlandaca or answer == answerlitvanca or answer == answerrusça:
# #     print("tebrikler doğru cevap")
# # else:
# #     print("üzgünüz yanlış cevap")

# import random

# launguage = {"which language is this?": "ingilizce", "какой это язык?": "rusca", "Welche Sprache ist das?": "almanca", "kokia tai kalba?": "litvanca", "hvaða tungumál er þetta": "izlandaca"}

# random_language, correct_answer = random.choice(list(launguage.items()))
# print(random_language)

# answer = input("bu hangi dil?")

# if answer == random_language or correct_answer :
#     print("teberikler")
# else :
#     print("mal")

# import random 

# launguageiniligzce = "which language is this?"
# launguagealmanca = "Welche Sprache ist das?"
# launguagerusca = "какой это язык?"
# launguagelitvanca = "kokia tai kalba?"
# launguageizlandaca = "hvaða tungumál er þetta"

# randomexam = random.choice()

# print(randomexam)

import random

launguage = {"which language is this?": "ingilizce", "какой это язык?": "rusca", "Welche Sprache ist das?": "almanca", "kokia tai kalba?": "litvanca", "hvaða tungumál er þetta": "izlandaca"}

random_language, correct_answer = random.choice(list(launguage.items()))
print(random_language)

answer = input("bu hangi dil?: ")

if answer.lower() == correct_answer:
    print("tebrikler doğru cevap")
else:
    print("üzgünüz yanlış cevap")
