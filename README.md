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
