from datetime import datetime
name = input("Enter your name:")
year = datetime.now().year
year_of_birth = input("Enter your year of birth:")
age = int(year) - int(year_of_birth)
start_year = input("Enter the year you started working with Routes Corporation:")
work_experience = int(year) - int(start_year)
print("Hello" + name + " you are " + str(age) + " years old")
print("we Routes Corporation corporation we are glad to tell you that you have gained a " + str(work_experience) + ' year experience')
