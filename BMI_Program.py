# aylat

# This program will calculate an individual's body mass index (BMI), 
# based on their height and their weight

# Prompt user to input information
Name = input('Enter your full name: ')
Weight = float(input('Enter your weight in pounds: '))
Height = float(input('Enter your height in inches: '))

# Perform BMI calculation, based on user input
BMI = Weight * 703 / Height**2

# Use an if/elif structure to determine the user's weight category, based on BMI
print('\n')

if BMI < 18.5: 
    print(Name, ", your BMI calculation is ", format(BMI, '.1f'),
          ", which indicates your weight category is underweight.", sep='')
    
elif BMI < 24.9:
    print(Name, ", your BMI calculation is ", format(BMI, '.1f'),
          ", which indicates your weight category is ideal.", sep='')
    
elif BMI < 29.9:
    print(Name, ", your BMI calculation is ", format(BMI, '.1f'),
          ", which indicates your weight category is overweight.", sep='')
    
else:
    print(Name, ", your BMI calculation is ", format(BMI, '.1f'),
          ", which indicates your weight category is obese.", sep='')


                                                                                                    
    
          
          
