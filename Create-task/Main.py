#I did not perform too well on this, just use it as a reference or an idea.
import random
import math
import sys
dact_dict = {'easy' : '9b6r027dojnptvf^ul3zigwmk4%ex85hs1yqa$c', 'medium' : 'JaEjlrAk4zc1Bfvu#57&2sK%tNUPQnVowqC0!dRI9hx^$pyLM6SXZDWG3Yb@eFgi8OHmT', 'hard' : '0vdohAJrBw9WD7cx@u5qfXjOyQLt8MkUb_4T#6RnisF%$)zSV+apIK2meZlg^&EG!H(3C1*PNY', 'extreme' : 'z+d{o:VwmrE/g]@Li\CWtkPp)QO8*Xl2&cGD^\f(x<e4A"j~ZFu?Y>n0bK}!\7vJy1hHS5-MB=%s9aT`I|6qNR;[#3,$._U'}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def generateentropy(difficulty, length):
    return math.log(len(dact_dict[difficulty]) ** length, 2)
    
def generatepassword(difficulty, length):

    chars = dact_dict[difficulty]
    password = []
    for _ in range(length):
        password.append(random.choice(chars))
    password = ''.join(password)
    return password

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("today we are generating a password")
inputdifficulty = input("Enter the difficulty level of the password (easy, medium, hard, extreme) ")
if inputdifficulty != "easy" and inputdifficulty != "medium" and inputdifficulty != "hard" and inputdifficulty != "extreme":
    print("Invalid difficulty inputted!")
    sys.exit("Try again!")

inputlength = int(input("Enter the password length: "))

printout = generatepassword(inputdifficulty, inputlength)

t = round(generateentropy(inputdifficulty, inputlength), 2)

if inputlength < 10000 and inputlength > 5:
    print("Your generated password is -> " + (printout))
    print(f'The entropy of your password is { t} which is {"bad" if      (t < 50) else "decent" if 50 < t < 75 else "good" if 76 < t < 100 else "impeccable"} for proffesional password standards')
else:
    print("your password cannot be over 10,000 characters or lower than 6!")
