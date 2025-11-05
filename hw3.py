import random

questions = [
    "What color is the sky on a clear day? ",
    "How many legs does a spider have? ",
    "What is 2 + 2? ",
    "Name a fruit that is yellow: ",
    "What is the opposite of hot? ",
    "What animal says 'meow'? ",
    "What day comes after Monday? ",
    "How many days are in a week? ",
    "What do cows drink? "
]

answers = [
    "blue",
    "8",
    "4",
    "banana",
    "cold",
    "cat",
    "tuesday",
    "7",
    "water"
]

hard_questions = [2, 3, 4]

lives = 3
asked_questions = []

def intro():
    print("Welcome to the TBAG game!")
    print("\nInstructions:")
    print("1. Only use lower-case letters.")
    print("2. Only type the answer, no unnecessary words or spaces.")
    print("3. You have 3 lives.")
    print("4. Some questions give you 1 extra life.")
    print("5. Have fun!\n")
    print("Let's start!\n")

intro()

step = 1

while len(asked_questions) < len(questions) and lives > 0:
    print(f"Step {step}:")
    print(f"Lives remaining: {lives}")
    
    n = random.choice([i for i in range(len(questions)) if i not in asked_questions])
    asked_questions.append(n)
    
    answer = input(questions[n]).strip().lower()

    if answer == answers[n]:
        print("✅ Correct!")
        if n in hard_questions:
            lives += 1
            print("🎉 You got an extra life!")
    else:
        lives -= 1
        print("❌ Wrong!")
        print(f"The correct answer was: {answers[n]}")
    
    print(f"Lives left: {lives}\n")
    step += 1

if lives == 0:
    print("💀 You ran out of lives! Game over.")
else:
    print("🏆 Congratulations! You finished the game!")
