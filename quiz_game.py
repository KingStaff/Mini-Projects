print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions_and_answers = [
    ("What does CPU stand for?", "central processing unit"),
    ("What does GPU stand for?", "graphics processing unit"),
    ("What does RAM stand for?", "random access memory"),
    ("What does PSU stand for?", "power supply"),
    ("What does SSD stand for?", "solid state drive"),
    ("What does HDD stand for?", "hard disk drive"),
    ("What does HTML stand for?", "hypertext markup language"),
    ("What does USB stand for?", "universal serial bus"),
    ("What does IP stand for?", "internet protocol"),
    ("What does HTTP stand for?", "hypertext transfer protocol"),
]

for question, correct_answer in questions_and_answers:
    answer = input(question + " ")
    if answer.lower() == correct_answer:
        print("Correct!✅")
        score += 1
    else:
        print("Incorrect!❌")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
