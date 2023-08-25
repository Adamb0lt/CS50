import random

def main():
    #calls get level to get a level
    score = 0 #tracking correct
    i = 0  # for tracking mistakes
    c = 0 # tracking total questions

    get = get_level()
    #generates 10 different math questions
    while c < 10:
        t,p = generate_integer(get)
        l = input(f"{t} + {p} = ")
        if l.isnumeric() and t + p == int(l): #has to have l.isnumeric() first because python checks top down left right and p==int(l) draws and error if put first
            score += 1
            c += 1
        elif l.isnumeric() == False or t + p != int(l):
            c += 1
            d = i + 2 #for how many chances the user gets to be wrong and then right answer is given
            print("EEE") #input
            while i < d:
                if l.isnumeric() and t + p == int(l)  :
                    c += 1
                    break
                else:
                    l = input(f"{t} + {p} = ")
                    i += 1
                    if l.isnumeric() == False or t+p != int(l):
                        print("EEE")
            print(f"{t} + {p} = {t+p}")
    print("Score:", score)


#get level from the user
def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 1 <= lvl <4:
                return lvl
            else:
                raise ValueError
        except ValueError:
            pass




def generate_integer(level):
    #ensures that 1-3 is input
            #generates the random integers to do the math with per level and returns it
        if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
                return x,y
        elif level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
                return x,y
        elif level == 3:
                x = random.randint(100,999)
                y = random.randint(100,999)
                return x,y




if __name__ == "__main__":
    main()





