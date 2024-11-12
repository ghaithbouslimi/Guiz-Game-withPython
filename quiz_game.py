print("Welcome to my computer quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes" : 
    quit()

print("okay! Let's play :)")    
score = 0 
answer = input("What is you favorite season ?")
if answer.lower() == "winter": 
    print('Correct!')
    score +=  1 
else : 
    print('Incorrect!')

answer = input("What is your favorite  subject ?")
if answer.lower() == "ia": 
    print('Correct!')
    score +=  1 
else : 
    print('Incorrect!')

answer = input("What did you prefer in the morning gym or learning?")
if answer.lower() == " i prefer going to gym": 
    print('Correct!')
    score += 1 
else : 
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100 ) + "%. ")        