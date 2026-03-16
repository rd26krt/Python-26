def convertInchesToCms(inches):
    lengthIncms = inches * 2.54

    return lengthIncms

lengthInInches = int(input("Enter length in inches"))
lengthInCentimeters = convertInchesToCms(lengthInInches)

print(f"{lengthInInches}inches converted to centimeters is {lengthInCentimeters}Cm")
