<div align="center"> 
    <h1>Sudoku Solver</h1> 
</div>

The project is a GUI Window based Sudoku Game that also solves any Sudoku Game w/ Basic GameAI.

<div align="center">
    <img src="/assets/GUI.png# sample" alt="drawing" style="box-shadow: 0 2px 24px 0 rgba(0, 0, 1, 1.8), 0 6px 20px 0 rgba(0, 0, 0, 0.19); border-radius: 13px" width="600px"/>
</div>


### Personal Motivation

Creating a game and then making an intelligent system which can play or solve the game is my fundamental goal and for some reason something that really interests me. The applications I want to build have 2 components - The Game, The AI. I wanted to create increasingly complex game-solvers to learn both game making (Software development) as well as Automation (using algorithms or Deep Learning) and my first step in learning to do so was a game I've been playing all my life, Sudoku.

An average game is a perfect example of OOP concepts coming together and being tested at their core principles and it is incredibly satifying to create good clean OOP compliant code. Creating a game teaches good OOP practices and is a great way of learning how to design architectures and class structures that scale well, which is a great skill to develop when my person goal is to build a large SaaS or OS at some point in the future.

The project was created with Tkinter as I want to learn to make and build OS based programs. Python and Tkinter also happen to be incredibly accessible and can be easily be switched to C++ and QT for improved efficiency and performance. But for now, Python will do the job, especially to understand core concepts.

An added motivation was to write production quality tests with tests and error handling wherever possible as well as being in control of deployment for now. After a few native OS GUI projects however, it might be better to switch to web based hosting as Tkinter and QT aren't very scalable and make it tough to build complex programs unlike Full Stack programs on the web.

### Features

The Game has 3 Fundamental features-
- Act as a basic Sudoku Game. Take input of numbers and check if solution is valid.
- Generate new Sudoku Games. 
    - Take input for difficulty.
    - Generate new games based on input.
- Solve any given Sudoku puzzle.

The features will be expanded upon in the Class Structures section and an upcoming blog post.

### Class Structures

#### Overview - 

[Display Picture]
The game design is comprised of 5 main classes that are organized as shown in the picture above.

##### 1. Board Class

The Board class is responsible for holding and maintaining the integrity of the structure of the basic sudoku board. Broadly speaking that's 3 responsibilities - 

1. Create a 2D - Array which holds the sudoku board values.
2. Raise errors if there's any errors in the shape of the Board (9 x 9) Array.
3. Raise errors if there's any errors in the input values, they should be in range (0 .. 9)

##### 2. Game Class 

The Game class is responsible for keeping all the game logic together in the same class. From starting the game to keep track of victory conditions. A fundamental responsibility is to append to the final board , the integers of the puzzle and then to check for victory conditions.

A victory condition is triggered when each of the following conditions are met:
1. Row condition
2. Column condition
3. Box condition
4. Full Board condition

In each of the above conditions, the terms to trigger victory remain the same, each of the above structures cannot have any repeating integers from 0..9. Once it's verified that each of these conditions are met, our puzzle is solved and we can wave the victory flag.

##### 3. UI Class 

[picture]

The UI Class defines the properties and behaviours of the user interface and is responsible for handling tasks any and all concerning interacting with the visual components of the application.

There are several visual components that compromise the Game Window UI. 

1. Clear Answers
2. Solve Puzzle
3. Generate new puzzle
    3.1. Easy
    3.2  Middle
    3.3  Hard
    3.4  Insane
4. 9x9 Grid
5. Individual Boxes
6. Numbers Filled down
    6.1. Number in original video.
    6.2  Number submitted by user.

The overview of the UI is that each of the grid boxes need to be placed perfectly and their positions are calculated from the mouse (x, y) coordinates and the numbers need to be placed perfectly inside the grid component which itself needs to be placed perfectly inside the larger window component.

Each of these components need to have handlers that cannot be explained in a brief readme, so I shall expand on the handlers in a blog post about the game. 2 of them however , call other classes to handle , the puzzle generator class and the puzzle solver class.

##### 4. Generator Class     
[code]

The Generator class generates new puzzles based on the input given. There are 4 levels that can be given, "Easy", "Medium", "Hard", "Insane". The generator works by creating a fully solved grid that passes the fully solved condition and then depending on the level, it removes some of the elements in the grid. The more harder levels have more sparse filled puzzles, the easier ones are almost solved with just few places to fill.


##### 5. Solver Class     
[code]

The Solver class solves any given puzzle given using a backtracking algorithm. It could be solved in a brute force algorith, but that would be an O(N!) solution. A backtracking approach brings this down to - > Time Complexity: O(9^(m * n)) and a Space Complexity: O(m*n).


## Code style
If you're using any code style like xo, standard etc. That will help others while contributing to your project. Ex. -

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)


## Screenshots
Include logo/demo screenshot etc.

## Tech

Built with
- [python](https://electron.atom.io)
- [tkinter](https://electron.atom.io)


## Code Example
Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

## How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## Contribute

Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus.

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Jaisurya]()
