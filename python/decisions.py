name = input("What is your name?")
age =int(input("How old are you?"))
skill = input("what do you want to learn?")
    
if age < 13:
    print(name + ", This is the right age to start coding!")
elif age > 18:
      print(name + ", Start Committing!")
else:
    print(name + ", You will become an amazing developer!")
 
print(skill + ", is an amazing skill to learn!")
