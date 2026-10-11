# Hello, World!
A text game written in Python that teaches you Python.

(Screenshot)
**Play at: (pyterm link)**

## Features and Description
- No installation required: playable in browser via PyTerm
- **main.py** includes comments for immersion and can optionally be read as part of the game

_Hello, World!_ is an existential horror, metafiction text game written in Python that is designed to teach the user some of the basics of Python.

Topics covered in the tutorial:
- print()
- input()
- comments
- variables
- data types
- loops
- if/elif/else

## Usage
The game branches based on user input, such as:
- y/n input

```python
#Example from definition of function start()
    x = input("Begin? y/n ")
    if x == "y":
        ...
    elif x == "n":
        ...
    else:
        ...
```
- Guided input
```python
#Example from definition of function gamebegin()
    print("Type the command below. Type exactly as it is written.")
    print("print("Hello, World!")")
    x = input()
    if x == "print("Hello, World!")" :
        ...
    else:
        ...
```

### Program structure 
```mermaid
graph
k([start]) --> anotherchance & gamebegin & k
anotherchance --> e([ending1])
gamebegin --> anotherchance & helloworld
helloworld --> hellotodata
hellotodata --> datatypes
datatypes --> boolean & typequiz
playagain --> k
boolean --> comment
typequiz --> comment & j([ending2])
j --> playagain
comment --> variable
variable --> ,
 
```

## Acknowledgements
- Used [this file](https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007) by rene-d for ANSI escape codes
- Used various websites online for debugging
- Used the Python documentation for guidance and ideas on tutorial content
- Used Mermaid Documentation for help with diagrams
- Used Wikipedia for the history of Python

**Everything else is fully original. No AI was used to write the code.**
