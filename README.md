## Python Collections: List, Tuple & Dictionary Operations

A beginner-friendly Python program that walks through the basic operations on three built-in collection types: the list, the tuple and the dictionary.
It uses Formula 1 drivers and teams as sample data and prints the collection after each operation, so you can see exactly what every method does.

## What the program covers
Data structure	Operations demonstrated
List:	create, display, access by index, append(), insert(), extend(), remove(), pop(), del, clear() and update a value.
Tuple: create, display, access by index, concatenation and del
Dictionary:	create, display, add a key-value pair, update a value, del, pop(), popitem() and clear()

## Requirements
Python 3.6 or higher (the program uses f-strings)
No external libraries

## How to run
bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python data_structure_operations.py

## Project structure
1. data_structure_operations.py
2. README.md
   
Data Structures
1. List	
2. Tuple
3. 	Dictionary
Syntax
1.	[ ]
2.	( )
3.	{ key: value }
Mutable (changeable in place)
1.	Yes
2.		No
3.		Yes
Ordered	
1. Yes
2. Yes
3. Yes 
Duplicates
1.	Allowed
2.		Allowed	Keys
3.		must be unique
Accessed by
1. Index
2. Index
3. Key
4. 
1. List operations

A list is mutable, so elements can be added and removed in place.

Operation	Syntax	What it does	Returns
Access	lst[i]	Reads the element at index i	The element
Append	lst.append(x)	Adds x to the end	None
Insert	lst.insert(i, x)	Adds x at index i	None
Extend	lst.extend(iterable)	Adds every item of the iterable to the end	None
Remove	lst.remove(x)	Deletes the first occurrence of x	None
Pop	lst.pop(i) or lst.pop()	Deletes the element at index i, or the last one	The removed element
Delete	del lst[i]	Deletes the element at index i	Nothing
Clear	lst.clear()	Deletes every element	None
Algorithm
START
    CREATE list drivers_list = ["Max", "Lewis", "Charles"]
    DISPLAY drivers_list
    DISPLAY the element at index 0

    ADD ELEMENTS
        APPEND "Kimi" to the end of the list
        INSERT "Arvid" at index 3
        EXTEND the list with ["Carlos", "Kimi"]
        DISPLAY the list after each step

    REMOVE ELEMENTS
        REMOVE the first occurrence of "Kimi"
        POP the element at index 3
        POP the last element
        DELETE the element at index 2
        CLEAR the list
        DISPLAY the list after each step
END
Things to notice
"Kimi" appears twice after extend(). remove("Kimi") deletes only the first one, and the second is later taken off the end by pop().
remove() raises a ValueError if the value is not in the list. pop() and del raise an IndexError if the index is out of range.
2. Tuple operations

A tuple is immutable: its contents cannot be changed after it is created. That means no append(), remove() or item assignment, so the program "adds" elements by concatenating two tuples into a new one.

Operation	Syntax	What it does
Access	tup[i]	Reads the element at index i
Concatenate	tup1 + tup2	Creates a new tuple containing both; the original tuples are unchanged
Delete	del tup	Deletes the whole tuple (the variable name); single elements cannot be deleted
Algorithm
START
    CREATE tuple drivers_tuple = ("Max", "Lewis", "Charles")
    DISPLAY drivers_tuple
    DISPLAY the element at index 0

    CREATE tuple drivers1 = ("Kimi", "Carlos")
    CONCATENATE drivers_tuple and drivers1 INTO drivers2
    DISPLAY drivers2

    DELETE drivers2
END
Things to notice
Concatenation never modifies drivers_tuple; it produces a separate tuple, drivers2.
After del drivers2, the name no longer exists. Using it again would raise a NameError.
3. Dictionary operations

A dictionary stores key-value pairs and is mutable.

Operation|Syntax|What it does|Returns
Add|d[key] = value|Adds a new key-value pair|Nothing
Update	d[key] = value	Replaces the value of an existing key	Nothing
Delete	del d[key]	Removes the pair with the given key	Nothing
Pop	d.pop(key)	Removes the pair with the given key	The removed value
Pop item	d.popitem()	Removes the last inserted pair	The removed (key, value)
Clear	d.clear()	Removes every pair	None

Algorithm
START
    CREATE dictionary drivers_dict =
        {"Max": "Red Bull", "Lewis": "Ferrari", "Kimi": "Mercedes"}
    DISPLAY drivers_dict

    ADD the key "Arvid" with the value "Racing Bulls"
    UPDATE the value of key "Lewis" to "Williams"
    DISPLAY drivers_dict after each step

    REMOVE ITEMS
        DELETE the key "Kimi"
        POP the key "Lewis" and store its value in driver
        POPITEM (remove and return the last inserted pair)
        CLEAR the dictionary
        DISPLAY the result of each step
END

## Things to notice
Adding and updating use the same syntax. If the key already exists its value is replaced; otherwise a new pair is created.
del d[key] and d.pop(key) raise a KeyError if the key is missing. d.pop(key, default) returns the default instead.

## Sample output
The original list is ['Max', 'Lewis', 'Charles'].
My favourite driver is Max
After append: ['Max', 'Lewis', 'Charles', 'Kimi']
After insert: ['Max', 'Lewis', 'Charles', 'Arvid', 'Kimi']
After extend: ['Max', 'Lewis', 'Charles', 'Arvid', 'Kimi', 'Carlos', 'Kimi']
After remove: ['Max', 'Lewis', 'Charles', 'Arvid', 'Carlos', 'Kimi']
After pop with index specified: ['Max', 'Lewis', 'Charles', 'Carlos', 'Kimi']
After pop without index specified: ['Max', 'Lewis', 'Charles', 'Carlos']
After delete: ['Max', 'Lewis', 'Carlos']
After clear: []
The original tuple is ('Max', 'Lewis', 'Charles')
My favourite driver is Max
The modified tuple is ('Max', 'Lewis', 'Charles', 'Kimi', 'Carlos')
The original dictionary is {'Max': 'Red Bull', 'Lewis': 'Ferrari', 'Kimi': 'Mercedes'}
After adding a key-value pair, {'Max': 'Red Bull', 'Lewis': 'Ferrari', 'Kimi': 'Mercedes', 'Arvid': 'Racing Bulls'}
After updating an existing value, {'Max': 'Red Bull', 'Lewis': 'Williams', 'Kimi': 'Mercedes', 'Arvid': 'Racing Bulls'}
After delete: {'Max': 'Red Bull', 'Lewis': 'Williams', 'Arvid': 'Racing Bulls'}
After pop: {'Max': 'Red Bull', 'Arvid': 'Racing Bulls'}
('Arvid', 'Racing Bulls')
{}

## What I learned
1. Lists and dictionaries are mutable; tuples are not
2. remove(), pop() and del differ in what they take and what they return
3. append() adds one item, insert() adds at a position, and extend() adds many
4. A tuple is "added to" by creating a new tuple with +, not by editing the old one

## License

This project is open source and available under the MIT License.
