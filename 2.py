# Input USD amount
usd = float(input("Enter a USD amount"))

# Define the exchange rate
exchange_rate = 0.97

# Convert from USD to Euros
euros = usd * exchange_rate

# Display the USD and Euros
print("USD:", usd)
print("EU:", round(euros, 2))
