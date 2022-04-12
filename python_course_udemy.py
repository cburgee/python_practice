def first_lesson():
    age = 20
    sentence = "My name is Caleb and this is my first python tutorial!"
    Caleb, Enoch, Joseph = 22, 17, 15
    Rabekah = Hannah = Leah = "These are the women in the family!"
    Caleb, myage = "Benjamin Caleb Burge", 22
    print(age)
    print(sentence)
    print(Caleb, Enoch, Joseph)
    print(Rabekah, Hannah, Leah)


def second_lesson():
    age1, age2 = 12, 18
    # Showing addition, subtraction, multiplication, and division
    age_total1 = age1 + age2
    # Modulus is division but returns the remainder.
    age_modulus = age1 % age2
    #  Srings can be added and multiplied. Multiplication requires str and int.
    # Can mix strings with integers and use some operators
    first_name, last_name = "Caleb", "Burge"
    full_name = first_name + " " + last_name
    # Can splice strings
    print("First name is " + full_name[:5] + ", Last name is " + full_name[6:])
    print(full_name)
    print(age_total1)
    print(age_modulus)


def third_lesson():
    # These are called placeholders. Must define data type in placeholder (%s %d)
    name = "Caleb"
    sent = "%s is 22 years old."
    full_name = "%s %s"
    print(full_name % ("Caleb", "Burge"))
    print(sent % (name))


def fourth_lesson():
    grocery_list = ["Apples", "Oranges", "Bananas", "Cheese"]
    grocery_list2 = ["Bread", "Jam", "Peanut Butter"]
    for i in grocery_list:
        print(i)
    print(grocery_list[0:2])
    # add item to a list
    grocery_list.append("Dont forget the blueberries.")
    print(grocery_list)
    # Change current value in list at index
    grocery_list[0] = "Cherries"
    print(grocery_list)
    # Remove item from a list at index
    grocery_list.pop(1)
    print(grocery_list)
    # can add lists together and also multiply
    print(grocery_list + grocery_list2)
    print(grocery_list * 2)
    # Can minimum and maximum value out of list of integers with builtin min() max() functions


def fifth_lesson():
    student_age = {"Bob": 12, "Rachel": 13, "Emily": 15}
    print(student_age)
    # Get specific key/value pair the key being Bob
    print(student_age["Bob"])
    # Assign an exisiting key to a new value
    student_age["Rachel"] = 25
    print(student_age)
    del student_age["Emily"]
    print(student_age)
    # If same key is used, it takes the last occurence of it and assigns it the value
    redudancy_examply = {"Caleb": 22, "Caleb": 32}
    print(redudancy_examply)


def sixth_lesson():
    # Tuple is a list that is immutable. ie you cannot change individual items in the list.
    tup1 = ("Oranges", "apples", "bananas")
    tup2 = (1, 2, 3)
    print(tup1)
    print(tup1[0])
    print(tup1[0:2])
    print(tup1 + tup2)


def seventh_lesson():
    # Operators: > < >= <= == !=
    age = 16
    if age < 13:
        print("You are too young")
    elif age >= 13 and age < 18:
        print("You are a teenager")
    else:
        print("You are an adult.")
    # if using or, if either is true results to true
    # "And" requires both statements to be true to result to true


def eighth_lesson():
    list1 = ["Caleb", "Hannah", "Leah", "Enoch", "Joseph", "Rabekah"]
    for i in list1:
        print(i)
    for i in range(1, 11):
        print(i)
    # Third number in the range function is the increment amount
    for i in range(0, 11, 2):
        print(i)
    for i in range(0, 26, 5):
        print(i)


def ninth_lesson():
    c = 0
    # can use break, continue
    while c < 5:
        c = c + 1
        if c == 3:
            break
        print(c)


if __name__ == "__main__":
    # Variable assignment/Multi Assignment
    # first_lesson()
    # Explanation of different operators
    # second_lesson()
    # String splicing
    # third_lesson()
    # Lists
    # fourth_lesson()
    # Dicts
    # fifth_lesson()
    # Tuples
    # sixth_lesson()
    # Conditional statements
    # seventh_lesson()
    # Loops
    # eighth_lesson()
    ninth_lesson()
