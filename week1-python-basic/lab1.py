# Exercise 1
print('Hello')
print('Yitian')

# Exercise 2
lastN = 'Wang'
carModel = 'Tesla'

# Exercise 3
# a) MEDICALprescrition is not a suitable variable name because it capitalizes the entire first word
# b) mdedical Prescription is not a suitable variable name because it contains space

# Exercise 4
fistName = 'Yitian'
lastName = 'Wang'
print(f"My full name is {fistName} {lastName}")

# Exercise 5
A = 5.3
B = 4.2
C = 6.0
result = (A + B) * C
print(f"The result is {result}")

# Exercise 6
A = 48
A = A - 1
A -= 1

# Exercise 7
remainder = 23 / 5
print(f"The remainder is {remainder}")

# Exercise 8
def showFullName(firstName, middleName,  lastName):
    print(f"My full name is {firstName} {middleName} {lastName}")
showFullName("Jane", "Jenny", "Jones")
showFullName("Yitian", "Etienne", "Wang")

# Exercise 9
def tempConvert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

print(tempConvert(100))

# Exercise 10
def showLetterGrade(percentage):
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade =  "F"
    print(f"The grade {percentage} is {grade}.", end = " ")
showLetterGrade(95)
showLetterGrade(72)
showLetterGrade(51)

# Exercise 11
def showMedicalStatus(firstName, age, highBloodPressure):
    if (age >= 55 and highBloodPressure == True):
        print(f"Medical alert: {firstName} see a doctor.")
    elif (age < 55 and highBloodPressure == True):
        print(f"Warning: {firstName}, seeing a doctor is recomended.")
    else:
        print(f"{firstName}, you are in good health, see you next checkup.")

showMedicalStatus("Bob", 60, True)
showMedicalStatus("Jane", 60, False)
showMedicalStatus("Brad", 28, True)

# Exercise 12
def showBalanceSchedule(firstName, balance, interestRate, yearsRemaining):
    print(f"*BALANCE FORECAST for {firstName} *")
    if interestRate ==  0:
        print("NA")
    else:
        a = 0
        while yearsRemaining > 0:
            balance = round(balance * interestRate, 2)
            yearsRemaining -= 1
            a += 1
            print(f"Year {a}: {balance}")

showBalanceSchedule("Louise", 5.25, 1.07, 7)
showBalanceSchedule("Larry", 52.25, 0, 6)
showBalanceSchedule("Mehri", 152.25, 1.15, 6)

# Exercise 13
for i in range(1, 6):
    print(i, end = " ")
    i += 1

# Exercise 14
def showBalanceSchedule(firstName, balance, interestRate, yearsRemaining):
    print(f"*BALANCE FORECAST for {firstName} *")
    if interestRate ==  0:
        print("NA")
    else:
        a = 0
        for i in range(yearsRemaining):
            balance = round(balance * interestRate, 2)
            a += 1
            print(f"Year {a}: {balance}")

showBalanceSchedule("Louise", 5.25, 1.07, 7)
showBalanceSchedule("Larry", 52.25, 0, 6)
showBalanceSchedule("Mehri", 152.25, 1.15, 6)

# Exercise 15
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for week in range(1, 5):
    print(f"Week {week}:", end = " ")
    for i, day in enumerate(days, start=1):
        print(f"{day}{i}")

# Exercise 16
x = 0
while x < 5:
    print(x)
    x += 1
    if x == 3:
        break

