print("welcome to my quiz")

playing = input("do you wanna play  ")

if playing != "yes":
    quit()
    
# Initialize score as an integer
score = 0

print("""What is the capital of France?
      A) Berlin
      B) Madrid
      C) Paris
      D) Rome""")

# Take user input
answer1 = input("")

# Check if the answer is correct
if answer1 == 'c' or answer1 == 'C':
    score += 1
    
print("""Which element has the chemical symbol 'O'?
A) Gold
B) Oxygen
C) Silver
D) Iron""")

answer2 = input("")

if answer2 == 'b' or answer2 == 'B':
    score += 1
    
print("""Who wrote the play "Romeo and Juliet"?
A) Charles Dickens
B) William Shakespeare
C) Mark Twain
D) Jane Austen""")

answer3 = input("")

if answer3 == 'b' or answer3 == 'B':
    score += 1
    
print("""What is the largest planet in our Solar System?
A) Earth
B) Mars
C) Jupiter
D) Saturn""")

answer4 = input("")

if answer4 == 'c' or answer4 == 'C':
    score += 1
    
print("""In what year did the Titanic sink?
A) 1905
B) 1912
C) 1920
D) 1935""")

answer5 = input("")

if answer5 == 'b' or answer5 == 'B':
    score += 1
    
print("""What is the main ingredient in guacamole?
A) Tomato
B) Onion
C) Avocado
D) Pepper""")
answer6 = input("")

if answer6 == 'c' or answer6 == 'C':
    score += 1
    
print("""Which country is known as the Land of the Rising Sun?
A) China
B) Japan
C) Thailand
D) India""")

answer7 = input("")

if answer7 == 'b' or answer7 == 'B':
    score += 1
    
print("""What is the freezing point of water in degrees Celsius?
A) -1°C
B) 0°C
C) 1°C
D) 100°C""")
answer8 = input("")

if answer8 == 'b' or answer8 == 'B':
    score += 1
    
print("""Who painted the Mona Lisa?
A) Vincent van Gogh
B) Pablo Picasso
C) Leonardo da Vinci
D) Claude Monet""")
answer9 = input("")

if answer9 == 'c' or answer9 == 'C':
    score += 1
    
print ("""Which ocean is the largest by surface area?
A) Atlantic Ocean
B) Indian Ocean
C) Arctic Ocean
D) Pacific Ocean""")
answer9 = input("")

if answer9 == 'd' or answer9 == 'D':
    score += 1
    

print("Your score is:", score)
print("out of 10")
