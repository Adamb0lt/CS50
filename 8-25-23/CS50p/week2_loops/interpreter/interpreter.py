def main():
     #requests input from user with math expression. Reference Pset1
    arith = input("Arithmetic expression: ").strip()

    #splits input by proper format into 3 variables
    x,y,z = arith.split(" ")

    #calls the math function
    math(x,y,z)

#math function
def math(p,g,c):
    # match and case based on g which is what determines the operation
    match g:
        case "+":
            i = float(p) +  float(c)
            
            #print output and formats it to one decimal place
            print(f"{i:.1f}")
        case "-":
            i = float(p) -  float(c)
            print(f"{i:.1f}")
        case "*":
            i = float(p) *  float(c)
            print(f"{i:.1f}")
        case "/":
            i = float(p) /  float(c)
            print(f"{i:.1f}")

main()

