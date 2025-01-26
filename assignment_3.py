##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
# Input the years
Year1 = int(input("Enter a year please:"))
Year2 = int(input("Enter another year please:"))

# Output the years and the differance
print("Year 1:", Year1)
print("Year 2:", Year2)
print("Differance:", abs(Year1 - Year2))

#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
# Input temperature in Fahrenheit
fahrenheit = float(input("Please provide a temperature in Farenheit:"))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Display Fahrenheit and Celsius temperatures
print("Fahrenheit:", fahrenheit)
print("Celsius:", round(celsius, 2))

#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''
# Input USD amount
usd = float(input("Enter a USD amount:"))

# Define the exchange rate
exchange_rate = 0.97

# Convert from USD to Euros
euros = usd * exchange_rate

# Display the USD and Euros
print("USD:", usd)
print("EU:", round(euros, 2))




##### ASSIGNMENT ENDS HERE #####
