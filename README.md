# Simple Interpreter
## Description
This is an interpreter for the programming language Simple. It allows you to write and run Simple code, which is a simple and easy to learn programming language.

## Requirements
To use this interpreter, you will need:

Python 3.6 or later
The colorama module, which can be installed using pip install colorama
Usage
To use the interpreter, run the script with the Simple code as an argument:

```bash
python main.py -f path/to/your/code.simp
```
Features
This interpreter supports the following features:

- Printing to the console
- Reading input from the user
- Delaying execution with the sleep command
- Single line comments with //
- Jumping to a specific line of code with the goto command
- Declaring and assigning variables with the var command
- Performing arithmetic operations with variables
- Conditional statements with the if command
- Defining and calling functions with the DEF and RUNDEF commands
- 
## Author
This interpreter was created by ousmblueninja.

# Documentaion


The Simple Interpreter supports the following instructions:

Printing
Use the print command to print a message or the value of a variable to the console:

```
print "Hello, World!";
END;
```
```
var x="10";
print "$x";
END;
```
Input
Use the input command to read input from the user:

```
print "What is your name?";
input in; << saves the input text to the variable in
print "Hello";
print "$in";
print "!";
END;
```

Delaying Execution
Use the sleep command to delay the execution of the program for a specified number of seconds:

```
sleep 2;
END;
```
Single Line Comments

Use the // symbol to add a single line comment to your code:
```
// This is a comment; << must end in ";"
print "Hello, World!";
END;
```
Jumping to a Specific Line
Use the goto command to jump to a specific line of code:

```
goto 10;
END;
```
Declaring and Assigning Variables
Use the var command to declare and assign a value to a variable:

```
var x = 10;
END;
```
You can**t** also perform arithmetic operations with variables, **YET**:

```
var x = 10;
var y = 20;
var z = $x + $y;
END;
```
Conditional Statements
Use the if command to execute a block of code if a condition is met:

```
var x = 10;
if ($x=="10"){11} << goto Line Number 11 if x is equal to 10
if ($x=="10"){*main} << goto function main if x is equal to 10
END;
```
Defining and Calling Functions
Use the DEF and RUNDEF commands to define and call functions:

```
DEF myFunction
print "This is my function";
ENDDEF;

RUNDEF myFunction;
END;
```

## List of commands

1. print
2. input
3. sleep
4. goto
5. RESET << Clears all variable
6. END
7. var
8. ALOC << alocates a variable name
9. if
10. PSTK << prints all variable
11. DEF
12. DEFEND
13. RUNDEF
14. CLR 