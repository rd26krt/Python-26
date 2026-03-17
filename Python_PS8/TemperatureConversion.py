
def celciusToFahrenheit(tempIncelcius):
    fahreheitTemp = (tempIncelcius * 9)/5 +32
    return fahreheitTemp

tempIncelcius = int(input("Enter a temperature in celcius"))
tempInFahrenheit = celciusToFahrenheit(tempIncelcius)
print("Temperature in fahrenheit is {}".format(tempInFahrenheit))
