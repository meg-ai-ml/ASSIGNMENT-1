# ASSIGNMENT-1
 Python List Operations: Create, Append & Remove

A beginner-friendly Python program that demonstrates the core operations on the list data structure: creating a list, accessing elements, adding elements (append, insert, extend) and removing elements (remove, pop, del, clear). It uses a list of Formula 1 drivers so each step is easy to follow.

## Features

1. Create and display a list
2. Access an element by index
3. Add elements with append(), insert() and extend()
4. Remove elements with remove(), pop(), del and clear()
5. Prints the list after every operation so you can see exactly what changed

## Requirements

Python 3.6 or higher
No external libraries

## Getting Started

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python list_operations.py
```

## Operations Covered

Operation | Syntax | What it does | Returns |
Access | `list[n]` | Reads the element at index `i` | The element |
Append | `list.append(n)` | Adds `x` to the end | `None` |
Insert | `list.insert(i, x)` | Adds `x` at index `i` | `None` |
Extend | `lst.extend(iterable)` | Adds every item of the iterable to the end | `None` |
Remove | `lst.remove(x)` | Deletes the **first** occurrence of `x` | `None` |
Pop (index) | `lst.pop(i)` | Deletes the element at index `i` | The removed element |
Pop (last) | `lst.pop()` | Deletes the last element | The removed element |
Delete | `del lst[i]` | Deletes the element at index `i` | Nothing |
|Clear | `lst.clear()` | Deletes all elements | `None` |

## Algorithm

START
    CREATE list drivers = ["Max", "Lewis", "Charles"]
    DISPLAY drivers
    DISPLAY element at index 0

    ADD ELEMENTS
        APPEND "Kimi" to the end of drivers
        INSERT "Arvid" at index 3
        EXTEND drivers with ["Carlos", "Kimi"]
        DISPLAY drivers after each step

    REMOVE ELEMENTS
        REMOVE first occurrence of "Kimi"
        POP the element at index 3
        POP the last element
        DELETE the element at index 2
        CLEAR the list
        DISPLAY drivers after each step
END




# Project Structure

1. list_operations.py
2. README.md


# What I Learned
1. How Python lists are created, read and modified
2. The difference between remove(),pop()` and del
3. The difference between append(),insert(),extend() and clear()
   
# License

This project is open source and available under the [MIT License](LICENSE).
