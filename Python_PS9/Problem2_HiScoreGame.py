import random
def game():

    score = random.randint(1,96)
    with open("highscore.txt")as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0

        print(f"Your Score is {score}")

    if(score>highscore):
         with open("highscore.txt", "w")as f:
          f.write(str(score))

    return score

game()
