# Research Repository
    This contains all of the information about all the projects included here.

A compilation of python projects.

## Table of Contents

- [Lectures](#lectures)
- [Python Exercises](#exercises)
- [Research](#research)
- [Usage](#usage)
- [References](#References)

## Lectures
This section contains the code examples provided by the instructors during our lectures. These code snippets serve as practical illustrations of the programming principles and concepts we've been taught in class. They are valuable for our learning, helping us understand and apply the covered materials. They act as reference points for future projects and assignments, helping us gain hands-on experience in software development.



### [Bank Account](Python_Exercises\Lectures\Bank_Account\Main.py)
When you run this code, it will create a bank account, perform the specified transactions, and display the account's information. In this example, it will show the account holder's name, account number, balance, and opening date.

This includes two classes, BankAccount class which includes everything that is needed in the program, and the Main class; It allows you to control what happens when your script is run. Code inside this block will only execute if the script is the main program (i.e., directly executed by the Python interpreter). If the script is imported as a module into another script, the code inside this block won't execute.

-    [Bank Account](Python_Exercises\Lectures\Bank_Account\BankAccount.py)
-    [Main](Python_Exercises\Lectures\Bank_Account\Main.py)



### [Library](Python_Exercises\Lectures\Library\Main.py)
This program essentially provides a text-based interface for users to interact with the library by borrowing and returning books and checking their account information.

-   [Main](Python_Exercises\Lectures\Library\Main.py)
-   [Library](Python_Exercises\Lectures\Library\Library.py)
-   [User](Python_Exercises\Lectures\Library\User.py)
-   [Book](Python_Exercises\Lectures\Library\Book.py)

### [Character](Python_Exercises\Lectures\Character.py)
This program contains basic information about OOP. It includes class Character with attributes 'name', and 'health_points'. 

### [Starter](Python_Exercises\Lectures\Ex-1-starter.py)
In this code, the turtle banana will move forward by 100 units, then turn left by 90 degrees, and finally move forward by 50 units. These commands create a simple drawing using the turtle graphics library.

### [Shapes](Python_Exercises\Lectures\Ex4-shapes.py)
When you run this code, it will display a Turtle graphics window and draw a pentagon with each side of 100 units in length. You can change the sideNums variable to draw polygons with a different number of sides.

### [Constructor](Python_Exercises\Lectures\P2.py)
This code snippet includes the basic knowledge about the OOP constructor.

### [Constructor (2)](Python_Exercises\Lectures\P3.py)
This code snippet is also about the concept known as the constructor, it shows the calling of a variable outside the class.

### [OOP](Python_Exercises\Lectures\Test.py)
This code snippet includes the introduction for OOP, it shows public and private variable,  normal method, how you call a method outside the class, and the meaning of the word 'self' in a method.

### [Loops](Python_Exercises\Lectures\w1-loops.py)
This script is about python loops, 'for' loops and 'while' loops are included here. Random module and Time module was imported in this script.

### [Print & Input](Python_Exercises\Lectures\w1-print-input.py)
This is the first lecture we had in programming, it includes the basic function 'print' and 'input'. It is explained that a single quote or a double quote can be used in a one line sentence, while the triple quote is used to create a paragraph form of the sentence. You can occupy as many lines as you like, as long as you use tripe quotes. 

In this script, I also included if-else statements, just to test my capabilities and my knowledge in this certain topic. I've learned it from w3schools website.

### [Functions](Python_Exercises\Lectures\w2-functions.py)
This script is about functions. At first, I had a lot of trouble understanding it, but after awhile, I've come to understand the use of a function. It is used to prevent your code from repeating, because as the time goes by, you will need to have more classes, more functions, and more attributes. And knowing the basic information about Functions is a must.
    
This script includes the basic information about Functions, how to use and call it.

### [Lists](Python_Exercises\Lectures\w2-lists.py)
This script shows different kinds of lists, whether it is string or integer. In this script, not only the lists were used, for loops and importing modules were also executed.

### [Random Choice](Python_Exercises\Lectures\w2-random-choice.py)
This script includes random module, it shows how to import a specific, class, attribute or variable from a module. 

### [Strings](Python_Exercises\Lectures\w2-strings.py)
This lecture is the continuation and more broad knowledge about strings. The instructor discussed different kinds of strings and taught us some basic shortcut we can use in coding.

### [Class](Python_Exercises\Lectures\w3-class.py)
This lecture is about Class, class Test is used as an example. Privacy and protection of variable is also discussed in this script. The instructor showed us how to call a method outside the class, and taught us that the private variable cannot be called outside and will basically error.

## Exercises
This section is for python exercises given by the lecturers and was done by the students. These are the weekly activities given to test the python skills of the students, and to expand their knowledge in python.

### [Ex1-1 Name](Python_Exercises\Exercises\ex1-1-name.py)
In this exercise, I used 'input' function and 'print' function. The user will be asked to input their first name and their last name. And as a result, it will print: "Hi, (first name) (last name)". 

### [Ex1-3 Farenheit to Celsius](Python_Exercises\Exercises\ex1-3-f-to-c.py)
This system is a temperature converter, it converts Farenheit to Celsius. To make this work, I used 'print & input' function again. I added a small title at the beginning and put the input function where the user can input the temperature in Farenheit (only numbers are accepted, whether it is a whole number or a decimal number), I added a variable that contains the formula of the conversion and print the result afterwards.

### [Ex2-3 Inspiration](Python_Exercises\Exercises\ex2-3-insp.py)
This exercise uses input and print function and the if-else statements. When you run this script, it will ask you to input a programming language, and based on your input, it will provide a suggestion for the type of developer role you can pursue. If your input doesn't match any of the specified languages, it will encourage you to focus on problem-solving skills instead.

### [Ex2-4 Grade Calculator](Python_Exercises\Exercises\ex2-4-gradecal.py)
This Python code takes a user's input as their exam mark, evaluates the mark, and then prints out a corresponding grade or message based on the mark. This python code also uses input and print function, and if-else statements.

### [Ex2 Method Function](Python_Exercises\Exercises\Ex2-method-function.py)
This Python code uses the Turtle graphics library to draw a series of squares with different colors and a red circular turtle cursor. After drawing the squares, the program will wait for you to click on the screen to close the graphics window.

### [Ex3-1 Multiplication Table](Python_Exercises\Exercises\ex3-1-xtable.py)
When you execute this code, it will prompt you to input a whole number. After you provide a number, the program will utilize a 'for' loop to compute and display the multiplication table for that specific number, covering the range from 1 to 20.

### [Ex3-2 Star](Python_Exercises\Exercises\ex3-2-star.py)
In this code, I've tried different ways to do it, the first try, I used:

     for x in range(1):
         num_str = ''
         for i in("*"):
             num_str += str(i) + " "
         for x in("*********"):
             print(num_str)
             num_str += str(i) + " "

     for i in range(11, 1, -1):
         num_str = ''
         for x in range(0, i-1):
             num_str += str(i) + " "
             print("*", end="")
         print('\n')


     for i in range(11,1,-1):
         for star in range(0, i-1):
             print("*", end="")
         print("\n")

But unfortunately, the code that I used isn't right, the first one came out the way I expected, but the bottom one is broken. 

When I tried for the second time, I made this script:

    for x in range(1):
    num_str = ''
    for i in("*"+"*"+"*"+"*"+"*"+"*"+"*"+"***"):
        num_str += str(i) + " "
        print(num_str)

It came out great but it only prints the top line. And in my third try, it finally worked as expected. This is the final output:

    for x in range(10):
    num_str = ''
    for i in range(1, x):
        num_str += "* "
    print(num_str)

 
    for x in range(10, 1, -1):
        num_str = ''
        for i in range(1, x):
            num_str += "* "
        print(num_str)

So when you run this code, you'll see two patterns of asterisks. The first pattern starts with one asterisk and increases up to nine asterisks, and the second pattern starts with nine asterisks and decreases down to one asterisk.

### [Ex3-3 Bingo](Python_Exercises\Exercises\ex3-3-bingo.py)
This Python code generates and prints two rows of random numbers, each row containing five random integers between 1 and 99, separated by "|".

### [Ex3-4 Guessing Game](Python_Exercises\Exercises\ex3-4-guessgame.py)
This code creates an interactive number guessing game where the user is prompted to guess a random number, and they receive feedback on whether their guess is too high or too low. The game continues until the user correctly guesses the number, at which point they receive a congratulations message.

### [Ex4-1 Lists](Python_Exercises\Exercises\ex4-1.py)
This program allows the user to enter a varying number of inputs in each of the five iterations of the outer loop. It stores these inputs in a list (user_inputs) and then prints the entire list, showing all the inputs entered by the user.

### [Ex4-2 Random](Python_Exercises\Exercises\ex4-2.py)
This program is a fun demonstration of how ANSI escape codes can be used to change text colors in a terminal. It generates "Hello, Students!" messages in random colors and prints them to the terminal. The inner loop, which is commented out, doesn't affect the output and could be safely removed from the code.

### [Ex4-3 Statistics](Python_Exercises\Exercises\ex4-3.py)
This program performs basic statistical operations on a list of numbers. It calculates the product, sum, average, minimum, and maximum values of the given list and prints the results.

### [Ex4-4 Random Students](Python_Exercises\Exercises\ex4-4.py)
This program demonstrates how to use Python to create dynamic and visually appealing text messages. It generates a random invitation message for a student, including details about an upcoming event, and uses ANSI escape codes to add color to specific parts of the message.

### [Ex5-1 Nicknames](Python_Exercises\Exercises\ex5-1-nicknames.py)
This program generates a fun and whimsical nickname by randomly selecting words from predefined lists of adjectives, nouns, and titles. It uses ANSI escape codes to add a touch of color to the printed nickname. Each time you run the program, you'll get a different nickname.

### [Ex5-2 Geometry Formula](Python_Exercises\Exercises\ex5-2-geo-formulas.py)
This Python program defines several functions to calculate various geometric properties, such as the circumference of a circle, the area of a circle, the surface area of a sphere, the volume of a sphere, the perimeter of a rectangle, and the area of a rectangle using mathematical formulas.

### [Ex5-3 Factorial](Python_Exercises\Exercises\ex5-3-factorial.py)
This Python program calculates the factorial of a given whole number n using a recursive function. If the user enters a non-zero positive integer for n, the function will calculate its factorial by recursively calling itself with smaller values of n until it reaches the base case of n = 0. Then, it starts returning values up the recursion stack, multiplying them along the way to compute the final factorial.

### [Ex5-4 Ticket Calculator](Python_Exercises\Exercises\ex5-4-ticket-cal.py)
The program constructs a message indicating the ticket price based on the provided age (if available) and returns this message. It then demonstrates this by calling the function with different age values and printing the resulting messages.

### [Ex6-1 Inspiration](Python_Exercises\Exercises\ex6-1.py)
This program demonstrates how to use the upper(), lower(), and title() string methods to change the case of characters in a string and capitalize the first letter of each word. It then prints the original and modified strings to the console.

### [Ex6-2 Password Generator](Python_Exercises\Exercises\ex6-2.py)
This program demonstrates how to generate random characters by selecting from predefined character sets and print them to the console in sequence. The character sets include alphabetic characters, punctuation symbols, and digits, and a random selection is made from these sets in each iteration of the loop.

### [Ex6-2-3 Password Generator(2)](Python_Exercises\Exercises\ex6-2-3.py)
This program demonstrates how to create a random password by selecting characters from various predefined character sets and then printing the generated password to the console. The resulting password contains a mix of lowercase and uppercase letters, punctuation symbols, and digits.

### [Ex6-3 Good morning](Python_Exercises\Exercises\ex6-3.py)
This program uses the time module to get the current time, extracts the hour component, and checks if it's morning (before noon). If it's morning, it prints a friendly "Good morning!" message to the console.

### [Cat Details](Python_Exercises\Exercises\main-3.py)
This program showcases OOP principles. It defines a base Cat2 class, inherits from it to create specific types of cats, and demonstrates polymorphism through method overriding. It also exemplifies encapsulation by using private attributes like __isHappy and provides getter and setter methods for them.

    `Cat2.py`
    `main-3.py`

### [Menu](Python_Exercises\Exercises\Product.py)
This Python program defines a Product class that represents a product in a cafe. It has various methods to manage the product's attributes such as name, price, and quantity, and it simulates selling and cost calculation. 

### [Turtle](Python_Exercises\Exercises\Test1.py)
This Python program uses the Turtle graphics library to create a colorful mandala-like pattern of circles on the screen.

### [Cat](Python_Exercises\Exercises\Cat\Main.py)
This program demonstrates object-oriented programming by creating Cat objects with specific attributes and behaviors (displaying information, displaying the cat, and making a sound). The program uses ASCII art and colored text to make the output visually interesting.

### [Stock System](Python_Exercises\Exercises\Stock_System\mainss.py)
This program provides a simple text-based interface for managing a list of products. Users can view existing products and add new ones. Note that there are some issues in the add_new_product method where price is assigned to the quantity variable. Additionally, it's important to validate user inputs for robust functionality.

### [Products](Python_Exercises\Exercises\Stock_System\Main.py)
This program is a simple inventory management system for different types of products. It demonstrates object-oriented programming principles, including inheritance and polymorphism. 

### [Book](Python_Exercises\Exercises\Book-1.py)
When you run this program, it creates a Book object, sets its attributes, and displays the book's information using the displayData method. In this case, it will print out the quantity, price, author, and publication name for the book "Tiramisu" authored by "Huie" with a quantity of 10 and a price of $95.

## Research
This section is for the projects that I found in GitHub, YouTube and Google. I've watched several tutorial videos from YouTube, got source codes from GitHub and Google. After that, I've studied each project, modify it to improve the program and to make it work in my device.

### Turtle
-   [Spring](spring.py)

    When you run this program, it will use Turtle graphics to draw a stylized representation of a flowering tree on the screen, with branches, leaves, and petals. The appearance may vary depending on the random values generated during execution. You can click on the drawing window to close it when you're done viewing the tree.

-   [Starry Night](starrynight.py)
        
    When you run this program, it creates a starry sky on a black background with a white moon in the center. The stars are randomly distributed across the screen, creating a visually appealing night sky scene. You can close the graphics window by clicking on it.

-   [Flower](flower.py)

    When you run this program, it will create a mesmerizing pattern with colorful, curved shapes on a dark gray background. The colors change for each layer of shapes, creating an interesting visual effect. You can close the graphics window by clicking on it.


### Pygame
-   [Flappy Bird](Flappy-Bird\main.py)

    This Python program is a simplified version of the popular game "Flappy Bird." It uses the Pygame library to create a game in which the player controls a bird (called "Grumpy") that must navigate through pipes without colliding with them.

-   [Hangman](Hangman-the-game-master\hangman.py)

    This Python program is an implementation of the classic game Hangman using the Pygame library. It allows players to guess letters in a hidden word until they either guess the entire word or run out of attempts.

-   [Pixel Runner](Pixel-Runner\runner_class_only.py)

    This Python program is a simple endless runner game built using the Pygame library. The player controls a character that can jump to avoid obstacles, and the goal is to achieve the highest score possible by surviving as long as possible. 

## Usage

## References
| Developer | Type     | Source Code                              |
| :-------- | :------- | :-------------------------------- |
| `Soham Kulkarni`      | `pygame` | [Hangman](https://github.com/bananafondue/Hangman-the-game.git) |
`Vast Coding`           | `pygame` | [Flappy Bird](https://drive.google.com/file/d/142SunlwrDJtbx7OvM-1Act0pbu8H8hma/view)
`Clear Code`            | `pygame` | [Pixel Runner](https://github.com/clear-code-projects/UltimatePygameIntro.git)
`Dany Setiawan`         | `turtle` | [Flower](https://github.com/dansyt/Flower-turtle-Python.git)
`BugNinza`              | `turtle` | [Spring](https://www.youtube.com/shorts/nIgkClbUIME)
`sagartomar9927` and `gowthammallela231`          | `turtle` | [Starry Night](https://www.geeksforgeeks.org/draw-starry-sky-with-moon-using-turtle-in-python/)

You can find the APA format of these references for this project in the [Research Repository](./documentation.pdf) file.
