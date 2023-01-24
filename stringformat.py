price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#index numbers
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age,name))

#named indexes
myorder ="I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))