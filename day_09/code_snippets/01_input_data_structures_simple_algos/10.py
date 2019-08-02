# fibonnaci


# bad but clear way of doing it
# better way given in 02_functions_python folder :)
a = 1
b = 1

print(a)
print(b)

for i in range(5):
    a = a + b
    b = a + b
    print(a)
    print(b)
