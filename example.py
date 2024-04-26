# REVIEW: While loops evalue true/false

value = True

# while value == True:
while value: # implied True
    print(value)
    value = False # causes loop to exit


print("---------------------- evalues 0 as false ---------------------")
value = True

# while value == True:
while value: # implied True
    print(value)
    value = 0 # causes loop to exit


print("---------------------- while value exist ----------------------")
value = "y"

# evaluate as True:
while value: # implied True
    print(value)
    value = 0 # causes loop to exit

print("---------------------- does not exist ----------------------")
value = 0

# evaluate as True:
while value: # implied True
    print(value)
    value = 0 # causes loop to exit


print("does not exist!")

print("---------------------- expland ----------------------")

value = "y"
count = 0 

# while value == True:
while value: # implied True
    count += 1
    print(count)
    if (count==5):
        break
    else:
        value = 0 # causes loop to exit
        continue 
