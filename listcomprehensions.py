# list comprensions allow us to build out lists using different notations. You can essentially think for loop
# build inside of brackets.

for x in range(0,6):
    print(x)

result=[x**2 for x in range(1,6)]
print(result)

even=[ a for a in range(1,21) if a%2==0]
print(even)

# celcius to fahrenheit
# fahrenheit to celcius
# write a program to calculate the number of vowels and consonant in you name.

string = "Aishwarya Neupane"
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)


# celcius to fahrenheit
def celsius_to_fahrenheit(celsius_temps):
    return [(9/5) * temp + 32 for temp in celsius_temps]

# Get a list of Celsius temperatures from the user
celsius_temps = [float(temp) for temp in input("Enter Celsius temperatures (comma-separated): ").split(',')]

# Use list comprehension to convert Celsius to Fahrenheit
fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)

# Display the results
print("Celsius Temperatures:", celsius_temps)
print("Fahrenheit Temperatures:", fahrenheit_temps)





