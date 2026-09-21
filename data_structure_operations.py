# LIST OPERATIONS

# Create a list of drivers.
drivers_list= ["Max","Lewis","Charles"]

# Display the list.
print(f"The original list is {drivers_list}.")

# Access an element from the list.
print(f"My favourite driver is {drivers_list[0]}")

# Append elements in the list.

# 1. Add element to the end of the list.
drivers_list.append("Kimi")
print(f"After append: {drivers_list}")

# 2. Add an element to a specific position.
drivers_list.insert(3,"Arvid")
print(f"After insert: {drivers_list}")

# 3. Add multiple elements at the end of the list.
drivers_list.extend(["Carlos","Kimi"])
print(f"After extend: {drivers_list}")

# Update in a list
drivers_list[5] = "Senna"
print(drivers_list)

# Remove elements from the list.

# 1. Remove the first occurrence from the list.
drivers_list.remove("Kimi")
print(f"After remove: {drivers_list}")

# 2. Removes the element at a specific index or the last element if no index is specified from the list.
drivers_list.pop(3)
print(f"After pop with index specified: {drivers_list}")

drivers_list.pop()
print(f"After pop without index specified: {drivers_list}")

# 3. Deletes an element at a specified index from the list.
del drivers_list[2]
print(f"After delete: {drivers_list}")

# 4. Remove all the elements from the list.
drivers_list.clear()
print(f"After clear: {drivers_list}")

# TUPLE OPERATIONS

# Create a tuple of drivers
drivers_tuple = ("Max","Lewis","Charles")

# Display the tuple
print(f"The original tuple is {drivers_tuple}")

# Access an element from the tuple.
print(f"My favourite driver is {drivers_tuple[0]}")

# Concatenate elements in the tuple by adding a new tuple to it.
# because We cannot directly append a tuple as tuples are immutable.

drivers1 = ("Kimi","Carlos")
drivers2 = drivers_tuple + drivers1
print(f"The modified tuple is {drivers2}")

# Updating a tuple by converting tuple to list vice versa
driver_tuple_1= list(drivers2)
driver_tuple_1[1] = "Lance"
drivers2 = tuple(driver_tuple_1)

print(f"The updated tuple is {drivers2}")

# Deleting the tuple.
del drivers2 

# DICTIONARY OPERATIONS

# Create a dictionary of drivers and teams
drivers_dict = { "Max" : "Red Bull","Lewis":"Ferrari","Kimi":"Mercedes"}

# Display the dictionary
print(f"The original dictionary is {drivers_dict}")

# Adding a key_value pair to the dictionary.
drivers_dict["Arvid"] = "Racing Bulls"
print(f"After adding a key-value pair, {drivers_dict}")

# Updating an existing value
drivers_dict["Lewis"] = "Williams"
print(f"AfTer updating an existing value, {drivers_dict}")

# Removing items from the dictionary.

# 1. Removes an item using its key.
del drivers_dict["Kimi"]
print(f"After delete: {drivers_dict}")

# 2. Removes the item with the given key and returns its value.

drivers_dict.pop("Lewis")
print(f"After pop: {drivers_dict}")

# 3. Removes and returns the last inserted key-value pair
print(drivers_dict.popitem())

# 4. Removes all items from the dictionary
drivers_dict.clear()
print(drivers_dict)








