name="Python"
print("I Know " + name + " programming language")
print("Slicing of string")
print("I know" + "Python" "\n" +name[0:5])
programs= "I know {} " .format("Python")
print(programs)

myLang="I know {0}, {1}, and {2}" .format("Python","Java","C++")
print(myLang)
print("Changing indexes of the string")
myLang="I know {2}, {1}, and {0}" .format("Python","Java","C++")
print(myLang)

print("--------------------------------")
lang="I know {p} {j} {c}".format(p="Python", j="Java", c="C++")
print(lang)
#lang="I know {p} {j} {c} {}".format(p="Python", j="Java", c="C++")
print(lang) 
#returns runtime error because of missing positional argument
