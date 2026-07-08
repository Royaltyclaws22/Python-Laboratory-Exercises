# Read the three side lengths separated by commas
L = input("INPUT: ")
L = L.split(",")
L = [float(i) for i in L]

# Sort the side lengths in descending order
L.sort(reverse=True)
print("The side lengths in descending order are: ", end="")
for i in L:
    print(i, end=",")

x = L[0]
y = L[1]
z = L[2]

# Calculate the perimeter and area if the sides form a valid triangle
if x < y + z:
    perimeter = x + y + z
    s = (x + y + z) / 2  # Semiperimeter
    area = (s * (s - x) * (s - y) * (s - z)) ** 0.5  # Heron's formula

    print("\nThe perimeter of the triangle is:", perimeter)
    print("The area of the triangle is:", area)

    # Check whether the triangle is equilateral or isosceles
    if x == y == z:
        print("The triangle is equilateral")
    elif x == y:
        print("The triangle is isosceles")
    elif y == z:
        print("The triangle is isosceles")
    elif x == z:
        print("The triangle is isosceles")

    # Classify the triangle based on its angles
    if x**2 == y**2 + z**2:
        print("The triangle is right-angled")
    elif x**2 > y**2 + z**2:
        print("The triangle is obtuse")
    elif x**2 < y**2 + z**2:
        print("The triangle is acute")
else:
    print("The triangle inequality is not satisfied")
