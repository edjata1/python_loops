print('*********** for / while loops *************')

print('*********** while *************')
# excute: (block of code), while the condition is (TRUE)

value = 1

while value < 10: # While TRUE 
    print(value) # DO THIS
    value += 1 # & DO THIS

print()

value5 = 1

while value5 <= 10: # While TRUE 
    print(value5) # DO THIS
    value5 += 1 # & DO THIS

print('*********** while, break *************')

value2 = 1

while value2 <= 10: # While True
    print(value2) # Do this
    if value2 == 5: # & Do this, BUT if TURE
        break # DO THIS -- STOP LOOP
    value2 += 1 # & DO this

print('*********** while, continue *************')

value3 = 0

while value3 < 10: # While True
    
    value3 += 1 # Do this, must increament here not after continue
    
    if value3 == 5: # & Do this, BUT if TURE
        continue # & Do this, SKIP # 5 & continue 
    print(value3) # & Do this

print()

value6 = 0

while value6 <= 10: # While True
    
    value6 += 1 # Do this, must increament here not after continue
    
    if value6 == 5: # & Do this, BUT if TURE
        continue # & Do this, SKIP # 5 & continue 
    print(value6) # & Do this

print()

value3 = 1

while value3 <= 10: # While True
    
    value3 += 1 # Do this, must increament here not after continue
    
    if value3 == 5: # & Do this, BUT if TURE
        continue # & Do this, SKIP # 5 & continue 
    print(value3) # & Do this

print('*********** while, continue / else *************')

value4 = 1
print("Value before starting while loop : " + str(value4))
while value4 <= 10: # While True
    print("Value after starting while loop : " + str(value4))
    value4 += 1 # Do this
    print("Incrementing value: " + str(value4))
    if value4 == 5: # & Do this, BUT if TURE
        print("continue: " + str(value4))
        continue # & Do this, SKIP # 5 & continue 
    print("continue: " + str(value4))
    print("PRINT VALUE: " + str(value4)) # & Do this
else:
    print("Out of while loop. Ended at value: " + str(value4))

print()
print('*********** for loop *************')
# loops over sequence
names = ["Empress", "Heather", "Timmy", "Mike", "Steve", "Tom"] # list
for name in names:
    print(name)

for x in "Mississippi":
    print(x)

print()
print('*********** for loop, break *************')

# names = ["Empress", "Heather", "Timmy", "Mike", "Steve", "Tom", "Sara"] # list
for x in names:
    if x == "timmy".title():
        break
    print(x)


print()
print('*********** for loop, continue *************')

# names = ["Empress", "Heather", "Timmy", "Mike", "Steve", "Tom", "Sara"] # list
for x in names:
    if x == "timmy".title():
        continue
    print(x)

print()
print('*********** for loop, range *************')
for x in range(4):
    print(x)

print()
for x in range(5):
    print(x)

print()
for x in range(2, 4):
    print(x)

print()
for x in range(1, 5):
    print(x)

print()
for x in range(4):
    print(x + 1)

print()
for x in range(0, 100, 10):
    print("Empress counts by 10's: " + str(x))

print()
for x in range(5, 101, 5): # how to increament
    print("Empress counts by 5's: " + str(x))
else:
    print("Glad that's over!")

print()
print('*********** nested loop *************')
names = ["Empress", "Heather", "Timmy", "Mike", "Steve", "Tom", "Sara"] # list
actions = ["code", "manage", "eats", "sleeps", "wake-up"] # list

for name in names:
    for action in actions:
        print(name +" " + action + ".")

print()
for action in actions:
    for name in names:
        print(name +" " + action + ".")
print()

