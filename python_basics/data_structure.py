# list

fruits = ["apple", "orange", "cherry", "banana", "mango"]
fruits2 = ["pineapple", "papaya"]

fruits[2] = "blackCurrant"  # replace the item
fruits.insert(2, "grapes")
fruits.append("kiwi")
fruits.extend(fruits2)
fruits.remove("banana")

fruits.sort()

print(fruits)

# =========================
# dictionaries

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]}

for key, value in car.items():
  print(key, value)

print(car["brand"])
print(car)
print(car.values())
print(car.keys())
print(car.get("year"))

car["colors"] = "white"

print(car.items())
