# questions for the user
name = input("What is your name?")
response =input("Can i know more about you? (yes/no):")
if response == "yes":
    answer = True
elif response == "no":
    answer = False
else:
    answer = None #invalid input
print ("GREAT!!")
age = input("How old are you?")
color = input("What is your favorite color?")
food = input ("what is your favorite food?")
city = input("What city do you live in?") 
school =input("What SHS did you attend?")
team = input("What is your favorite soccer team?")
movie = input("What kind of movies do you love?")

# Display a summary
print("\n--- summary ---")
print(f"Hello, {name}!")
print(f"you are {age} years old, you love the color {color}, and enjoy eating {food}.")
print(f"you attended {school} which is my younger brother's school")
print(f"Life must be amazing and fun in {city}")
print(f"interesting how you are also a fun of {team}")
print(f"i also watch {movie} movies only when i have no movie options")

# ask if user wants to restart the process
restart = input("\nDo you want to restart the process? (yes/no):")
if restart != "yes":
    print("Okay then, Goodbye {name}")

# ask the suer to rate the assistance
def get_rating():
    while True:
        try:
            rating = int(input("Rate the assistant from 1 to 5 stars: "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


