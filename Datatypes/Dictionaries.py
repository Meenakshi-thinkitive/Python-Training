country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London
country_capitals["Italy"] = "Rome"
print(country_capitals)
del country_capitals["Germany"]
print(country_capitals)
country_capitals.clear()

print(country_capitals)  
print(len(country_capitals)) 