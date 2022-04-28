# Michael Mullen
# This program will be a quiz game that asks the user for answers to questions
# and uses the answers to tally points for the total result.

print("Welcome! " * 3, "This is my integration project for Sprint 2.", sep=":) ")

print("Before anything begins I have a display to show you.")

g = float(input("Enter a high number: "))
h = float(input("Enter a lower number: "))

if g > h:
    print("By my calculations, G is greater than H")
else:
    print("Why didn't you do the right thing?")

while g > 0 and h > 0:
    print("I like that you picked positive numbers")
    g = -1

while not g > 0:
    print("But I lowered G to be less than zero so I could show you this message.")
    g = 1
    h = -1

while g > 0 or h > 0:
    print("I swapped G and H so that I could show you THIS message.")
    g = -1
    print("I had to make both negative now though, time for questions!")

name = input("What is your name? ")

print("Tanks for telling me your name", name, ".", sep=" ")

age = input("How old are you " + name + "? ")

print(age, "... Is that old?", "I'm not sure.", sep=" ")

color = input("What's your favorite color? ")

print(color, "is my favorite color too!", sep=" ")

height = input("How tall are you? ")

print("That seems tall to me. I have no body to compare")

language = input("By the way, what language is your favorite? ")

print("I've never heard of " + language + ".")

sure = input("Are you sure? ")

print("Well, everyone has weird interests.")

how_doing = input("How are you doing " + name + "? ")

print("I'm sorry to hear that...")

funny = input("I'm not good at knowing about emotions, only numbers. " + "What's your favorite number? ")

print("Thanks for telling me, but I don't like that number.", end=" >:( ")

user_num = float(input("Enter a better number please: "))

transform1 = user_num + 42

# This code adds 42 to the number entered by the user.

transform2 = transform1 - user_num

# This code removes the number the user entered from the on going value.

transform3 = transform2 * 10

# This code multiplies the value by 10.

transform4 = transform3 ** 2

# This code squares the value.

transform5 = transform4 / transform4

# This turns the value into 1 by dividing by itself.

transform6 = transform5 - transform5

# This turns the value into 0 by subtracting the value from itself.

transform7 = transform6 * 100

# This multiplies the value by 100 but doesn't change it because the value is 0.

transform8 = transform7 + user_num

#this make the value equal to the value the user entered again.

half_way = transform8

print("Your number has been twisted and warped into...", half_way, sep=" ")

good = input("Did you expect it to be the same? ")

print("Oh.")

change = input("Well can you tell what changed? ")

print("Wrong. I added a decimal and a 0 in the tenths place.")

cool = input("Did you find that cool? ")

print("I thought it was cool.")

destroy = input("Should I destroy your number? ")

print("I have already done it.")

new_sequence = half_way % half_way

# This code turns the value to 0.0 by using the modulus function.

print("Your number has been destroyed, it is now,", new_sequence)

back = input("Do you want your number back? ")

print("I am already rebuilding it.")

num1 = new_sequence + 12

# This code adds 12 to the existing value of 0.

print("One step at a time")

num2 = num1 // 3.5

# This code floor divides the value by 3.5.

print("Getting there...")

num3 = num2 + user_num

# This code adds the user entered number to the value

print("Almost done...")

fin_num = int(num3 - 3)

# This code subtracts 3 from the value.

print("Is THIS your number?", fin_num)

yn = input("Impressed? ")

print("Alright", name, "let's review.")

print("Your name is ", name, ". You are ", age, " years old. You are ", height, " tall. Your favorite color is ", color, ".", sep="")

print("Now I know everything about you.")

print("We can begin our quiz game now. Are you excited?")

excited = input()

def quiz_game():

    question_num = 1
    user_answers = []
    correct = 0
    
    for x in questions:
        print()
        print(x)
        
        for y in answer_choices[question_num - 1]:
            print(y)
        
        user_answer = input("Enter either A or B: ")
        user_answers.append(user_answer)
        question_num = question_num + 1
        correct = correct + check(questions.get(x), user_answer)

    results(correct, user_answers)

def check(answer, user_answer):

    if answer == user_answer:
        print("Correct!")
        return 1
    if answer != user_answer:
        print("Incorrect!")
        return 0

def results(correct, user_answers):
    print()
    print("Results:")
    
    print("User Answers: ", end="")
    for w in user_answers:
        print(w, end=" ")
    print()
    
    print("Answers: ", end="")
    for z in questions:
        print(questions.get(z), end=" ")
    print()

    score = int((correct/4)*100)
    print("Your score is: " + str(score) + "%")

questions = {"How many continents are there?: ": "A",
             "How many oceans are there?: ": "B",
             "How many planets are in our solar system?: ": "B",
             "What is the name of our galaxy?: ": "A"}

answer_choices = [["A. 7", "B. 10"],
                  ["A. 9", "B. 5"],
                  ["A. 12", "B. 8"],
                  ["A. Milky Way", "B. Andromeda"]]

quiz_game()

for v in range(4,5):
    print("Thank you for answering my", v, "questions!")

print()
print("Congratulations! " * 3)

print("You have completed my program, thanks for participating", name, end=". :)")


# I used W3Schools as a resource for this assignment.
