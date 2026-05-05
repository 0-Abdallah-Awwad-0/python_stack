# Assignment: For Loops Basic I


# 1. Basic
# Print all integers from 0 to 150
for i in range(151):
    print(i)


# 2. Multiples of Five
# Print all multiples of 5 from 5 to 1000
for i in range(5, 1001, 5):
    print(i)


# 3. Counting, the Dojo Way
# Print integers from 1 to 100
# If divisible by 10, print "Coding Dojo"
# If divisible by 5, print "Coding"
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


# 4. Whoa. That Sucker's Huge
# Add odd integers from 0 to 500,000
total = 0

for i in range(1, 500001, 2):
    total += i

print(total)


# 5. Countdown by Fours
# Print positive numbers starting at 2018, counting down by 4
for i in range(2018, 0, -4):
    print(i)


# 6. Flexible Counter
# Print numbers from lowNum to highNum that are multiples of mult
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)