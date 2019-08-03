# fibonnaci
# sequence of numbers derived from adding the preceeding two numbers
# First two numbers are 1 and 1
# 1, 1, 2, 3, 5, 8, 13 and so on.


# bad but clear way of doing it
# better ways exist :)
a = 1
b = 1

print(a)
print(b)

for i in range(5):
    a = a + b
    b = a + b
    print(a)
    print(b)
