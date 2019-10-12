# append 
# rewrite the code to use a list comprehension to accomplish the same thing as a for loop

july_temperatures = [87, 85, 92, 79, 106]
hot_days = []

#for temperature in july_temperatures:
#    if temperature > 90:
#        hot_days.append(temperature)
#    print(hot_days)

hot_days = [temperature for temperature in july_temperatures if temperature > 90]

print (hot_days)