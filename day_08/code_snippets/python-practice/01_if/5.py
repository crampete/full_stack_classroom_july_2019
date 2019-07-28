# elif ladder
johnny_marks = int(input("How much did Johnny score in his math test?\n"))


# The first matching condition gets executed
if johnny_marks > 100 or johnny_marks < 0:
    print("Please enter a valid mark.")

elif johnny_marks >= 90:
    print("He's a math wizard!")

elif johnny_marks > 80:
    # if you want to be explicit and
    # it also helps with documentation
    # elif johnny_marks > 80 and johnny_marks < 90:
    print("He isn't bad at all.")

elif johnny_marks > 70:
    print("He's made progress.")

else:
    print("He can do better.")
