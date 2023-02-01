import time

# business process automation (BPA) - Explained
# as filling out forms etc instead of filling out paperwork infront of someone, filling payrolls, doing leave etc.

#deliverables - a list of things the software should be doing
    # in terms of a house - the frame is the first deliverable, then electronics, then plumbing, each is a deliverable.
    # They can also be called as a milestone
    
#stakeholders - anyone that it effets / invested / uses the app or thing.
    
#Sponsors - the ones that decide on the final decision and usually the cause of bad faults.
    
#when doing work, try get involved in anything you're interested in, like do documentation - do the coffee run type stuff.
    #be that bounce board for discussion
    # minimal viable product - the starting point and bridge out
    
    
    #waterfall vs agile work place -> waterfall is just down the steps, you go from the start to finish without going back.
    # if you miss something that's in V2 not V1 which you're still on.
    #Agile is just going and going around constantly develope, the cycle of 1-6
    #Develop, design, plan, meet, evaluate, test
    
    
    # number 1 thing to reccomend to laern coding - come up with a project - write your own and start coding it.
    # use Pi Charm next week - Try another after 2 weeks of usage.
    
    #elif = else if, can have as man as you want just don't overlap.
    #else is the ending statement, so if you have no more ifs or if that's the last testing part use ELSE.
    
    #marcus github link -> it's in the additional content area within the automation page.
    
    



inputstring = input ("Please write your input string here: ")

print (" Why did you write this?", inputstring, "<< this thing.")

while True:
    numberOne = input ("Place your first number here: ")
    if numberOne.isdigit():
        print ("Next, ")
        break
    else:
        print("This is not an number or digit, try again.")

#numbered 1 for courtesy and consistency with test on line 52.
attempt = 1

numberTwo = input ("Place your second number here: ")

while not numberTwo.isdigit():
    numberTwo = input ("Try again. \nPlace your second number here: ")
    if attempt == 3:
        print("Try to follow the instructions and start again.")
        break
    else:
        print("You're currently at attempt: ", attempt)
        attempt = attempt + 1
    
time.sleep(1)
print ("We will add them together and check if that's a prime number, only if you can follow instructions.")
print("calculating...")
time.sleep(1)
print ("Your numbers added equal: ", int(numberOne) + int(numberTwo))
time.sleep(0.5)
primeNumber = int(numberOne) + int(numberTwo)

print("Testing...")
#print (primeNumber)
time.sleep(1)
flag = False

if primeNumber == 1:
    print(primeNumber, "This is not a prime number.")
elif primeNumber > 1:
        for i in range(2, primeNumber):
            if (primeNumber % i ) == 0:
                flag = True
                break
if flag:
    print(primeNumber, "is not a prime number.")
else:
    print(primeNumber, "is a prime number.")
    
attemptvote = 1
canVote = input ("Please state your age in digit form: ")

while not canVote.isdigit():
    canVote = input ("Restate your age as a number: ")
    if attemptvote == 3:
        print("Alright, start again. Too many attemps.")
        break
    else:
        print("You're currently at attempt: ", attemptvote)
        attemptvote = attemptvote + 1
    
    
if int(canVote) >= 18:
    print ("You can now vote")
else:
    print ("come back when you're older.")