import math

def max_percents():
    pr = int(input("\nPlease enter your weight lifted: "))
    reps = int(input("For how many reps? "))
    if reps == 1:
        calculator = pr*1
    else:
        calculator = (pr*(1/(1-(.025*reps))))
    print("Your projected max is {}.".format(round(calculator)))
    print("\nWould you like to continue?")
    
def max_reps():
    hope = int(input("\nPlease enter your projected 1-rep max goal: "))
    working_weight = int(input("Please enter the weight you will rep-out: "))
    if hope == working_weight:
        how_many_reps = working_weight/hope
    elif working_weight/hope < 1 and working_weight/hope > .95:
        how_many_reps = 2
        
    else:
        how_many_reps = math.ceil((1-(working_weight/hope))/.025)
    print("You'll need to do {} reps at {} for a projected max of {}.".format(round(how_many_reps), working_weight, hope))
    
print("Welcome to the Training Max Calculator!")
print("-"*39)
print("What would you like to do?")
print("\n1.) Find out my projected 1-rep max")
print("2.) Find how how many reps I need at a submaximal weight")
print("3.) Quit")
while True:
    try:
        answer = int(input("\nPlease enter your choice here (1, 2, or 3) > "))
    except ValueError or NameError:
        print("Oh no! Please enter a valid choice ")
        continue
    if answer == 1:
        max_percents()
        continue
    elif answer == 2:
        max_reps()
        print("\nWould you like to continue?")
        continue
    elif answer == 3:
        print("Come again soon!")
        break
    else:
        print("Oh no! Please enter 1, 2, or 3")
        continue

        
    