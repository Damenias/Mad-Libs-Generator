#Mad Libs Generator
from xml.sax import parse

print("Let's Play a MAD Libs! Fill in the blanks bellow \n")
place = input("Enter a place: ")
hobby = input("Enter your hobby: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")

#my story with user inputs

story =f"""
I always find {place} very attractive. Sadly i can't always go there. My hobby is {hobby}
so it kinda makes sense why i like {place} so much. Once I saw {animal} there. The {animal} was {verb}. 
This was a very beautiful day."""

print("\nHere is your Mad Libs Story:")
print(story)
