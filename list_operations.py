# LIST AND ITS OPERATIONS
# Create a list of drivers.
drivers = ["Max","Lewis","Charles"]

# Display the list.
print(f"The original list is {drivers}.")

# Access an element from the list.
print(f"My favourite driver is {drivers[0]}")

# Append elements in the list.

# Add element to the end of the list.
drivers.append("Kimi")
print(f"After append: {drivers}")

# Add an element to a specific position.
drivers.insert(3,"Arvid")
print(f"After insert: {drivers}")

# Add multiple elements at the end of the list.
drivers.extend(["Carlos","Kimi"]) # "Kimi" is added again on purpose to show that remove() only deletes the first match.
print(f"After extend: {drivers}")

# Remove elements from the list.

# Remove the first occurrence from the list.
drivers.remove("Kimi")
print(f"After remove: {drivers}")

# Removes the element at a specific index or the last element if no index is specified from the list.
drivers.pop(3)
print(f"After pop with index specified: {drivers}")

drivers.pop()
print(f"After pop without index specified: {drivers}")

# Deletes an element at a specified index from the list.
del drivers[2]
print(f"After delete: {drivers}")

# Remove all the elements from the list.
drivers.clear()
print(f"After clear: {drivers}")

