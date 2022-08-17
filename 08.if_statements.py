day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")
elif day_of_week == "Friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")

# Additional Info: The order of the keywords is important. Remember that the if comes first, then any elif, if you want them, and finally the else. The elif and else keywords are optional if you want to add those branches to your if statement 



# -- Problem: user not entering what we expect --

day_of_week = input("What day of the week is it today? ").lower()
# the .lower() makes the function avaialale to both uppercase and lower case functionality.



if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")