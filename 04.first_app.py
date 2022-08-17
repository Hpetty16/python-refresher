# a cleaner way to write the code would be user_age = int(input ("Enter your age please: ")), and changing line 5 to months = user_age * 12

user_age = input ("Enter your age please: ")
years = int(user_age)
months = years * 12
print(f"Your age, {years}, is equal to {months} seconds.")