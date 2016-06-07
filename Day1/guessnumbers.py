import random

numbers = []
guesses = []
tries = 3

while(len(numbers) < 4):
    rand = random.randint(1, 9)
    if rand not in numbers:
        numbers.append(rand)

while(tries):
    a = 0
    b = 0
    for i in range(0,4):
        guesses.append(int(input("Input number " + str(i+1) +":")))
    if numbers == guesses:
        print("Congratulations!")
        break
    else:
        for i in range(0,4):
            if(guesses[i] in numbers):
                if(guesses[i] == numbers[i]):
                    a = a + 1
                else:
                    b = b + 1
    print("A = " + str(a) + ", B = " + str(b) + ". Try again.")
    tries = tries - 1

print("These numbers are: " + str(numbers[0]) + " " + str(numbers[1]) + " " + str(numbers[2]) + " " + str(numbers[3]))
