'''
This Python file created by following Real Python tutorial "Python 3's f-Strings: An Improved String Formatting
Syntax (Guide)" by Joanna Jablonski.
Joanna's tutorial can be found here: https://realpython.com/python-f-strings/
Joanna's GitHub can be found here: https://github.com/jablonskidev
'''
#Ways of embedding Python expressions inside string literals for formatting: %-formatting, str.format(), f-strings.


#Option 1: %-formatting (easy to implement, but even Python docs admit there are quirks; it should be avoided)

#Substituting a name:
name = "Eric"
"Hello, %s." % name

#Must use a tuple for multiple variables:
name = "Eric"
age = 74
"Hello, %s. You are %s." % (name, age)

#Problem: Mo Variables == Mo Complexity:
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
"Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation)


#Option 2: str.format() (new and improved, uses normal function call syntax)

#Now the replacement fields are marked by curly braces:
"Hello, {}. You are {}.".format(name, age)

#Variables can be referenced by their index instead of order in the tuple:
"Hello, {1}. You are {0}.".format(age, name)

#Can also be referenced by variable names:
person = {'name': 'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(name=person['name'], age = person['age'])

#Can also use **dict_name to condense the above example:
person = {'name':'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(**person)

#Conclusion: str.format() is easier to read! BUT it can be quite long-winded w/ multiple paramters + longer strings...
first_name = 'Eric'
last_name = 'Idle'
age = 74
profession = 'comedian'
affiliation = 'Monty Python'
print(("Hello, {first_name} {last_name}. You are {age}. You are a {profession}." +
       "You were a member of {affiliation}.").format(first_name=first_name, last_name=last_name, age=age, \
                                                     profession=profession, affiliation=affiliation))

#f-Strings joined in Python 3.6, info @ PEP 498 by Eric V. Smith, AKA formatted string literals
#The examples above could be expressed as:
name = "Eric"
age = 74
f"Hello, {name}. You are {age}."
#or
F"Hello, {name}. You are {age}."

#f-strings are evaluated at runtime, can use expressions, call functions or methods, and use objects
#Expression:
f"{2*37}"

#Call function:
def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
f"{to_lowercase(name)} is funny."

#Call method:
f"{name.lower()} is funny."

#Use an object created from classes f-strings:
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!!"

new_comedian = Comedian("Eric", "Idle", "74")
f"{new_comedian}"

#3 types of conversion flags: !s which calls str() on the value, !r calls repr(), !a calls ascii().
#f-strings use __str__() by default, __repr()__ can be called with its conversion flag.
f"{new_comedian}"
f"{new_comedian!r}"

#Multiline f-Strings are supported
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
message

#the following code wouldn't work:
message = (
    f"Hi {name}. "
    "You are a {profession}. "
    "You were in {affiliation}."
)
message

#Can also escape a return w/ the backslash:
message = f"Hi {name}. " \
    f"You are a {profession}. " \
    f"You were in {affiliation}."

message

#Messy example with triple quotes:
message = f"""
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
"""

message

#f-strings are fast. Again, they are executed at runtime
#Speed comparison of %-formatting, str.format(), & f-Strings:
import timeit
timeit.timeit('''name="Eric"
age = 74
'%s is %s.' % (name, age)''', number=10000)

import timeit
timeit.timeit('''name="Eric"
age=74
'{} is {}.'.format(name,age)''', number=10000)

import timeit
timeit.timeit("""name="Eric"
age=74
f'{name} is {age}.'""", number=10000)
#f-Strings are the fastest @ runtime

#Need a keen eye for detail, as shown here:
#these will work:
f"{'Eric Idle'}"
f'{"Eric Idle"}'
f"""Eric Idle"""
f'''Eric Idle'''

#cannot use same type of parentheses outside of curly braces as inside
#can use an escape to weasel around this rule
f"The \"comedian\" is {name}, aged {age}."

#when using single quotes dictionary keys, use doeble quotes for the f-strings containing the keys
comedian = {'name': 'Eric Idle', 'age':74}
f"The comedian is {comedian['name']}, aged {comedian['age']}."

#Can get braces to appear if using
f'{{70+4}}'
f'{{{70+4}}}'
f'{{{{70+4}}}}'
f'{{{{{70+4}}}}}'
#this returns '{70+4}','{74}','{{70+4}}','{{74}}'

#Cannot use backslashes or comments inside of the expression part of an f-string



