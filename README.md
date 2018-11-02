# Problem Solving - Basic Python
The objective of this repo is to solve problems using basic programming skills i.e variables, conditions, iterations and arrays.

## Problems:
* [x] Hello World
* [x] Prime Numbers
* [x] Triangle/Diamond Problems
* [x] Maze Game
* [ ] Binary to Decimal and Decimal to Binary
* [ ] Binary Numbers Addition
* [ ] Matrix Addition
* [ ] Matrix Multiplication
* [ ] Linear Search
* [ ] Binary Search
* [ ] Bubble Sort
* [ ] Palindrome

*Feel free to add problems by opening pull requests.*

------------

If anyone like to compile any problem, just write following lines in terminal
```
python3 <project_name>.py
```

## [#1 - Hello World](https://github.com/mrazam110/problem-solving-python/blob/master/Source/helloworld.py)
```bash
$ python3 helloworld.py 
Hello World
```
## [#2 - Prime Numbers](https://github.com/mrazam110/problem-solving-python/blob/master/Source/prime-number.py)
```bash
$ python3 prime-number.py
Enter a positive integer number: 10
2  is a prime number
3  is a prime number
4  is a prime number
5  is a prime number
6  is not a prime number
7  is a prime number
8  is not a prime number
9  is not a prime number
```

## [#3 - Triangle/Diamond Problems](https://github.com/mrazam110/problem-solving-python/blob/master/Source/diamond-problems.py)
```bash
$ python3 diamond-problems.py 
0 
0 0 
0 0 0 
0 0 0 0 
0 0 0 0 0 
--------------------

0 
0 0 
0 0 0 
0 0 0 0 
0 0 0 0 0 
0 0 0 0 
0 0 0 
0 0 
0 
--------------------

     0 
    0 0 
   0 0 0 
  0 0 0 0 
 0 0 0 0 0 
--------------------

     0 
    0 0 
   0 0 0 
  0 0 0 0 
 0 0 0 0 0 
  0 0 0 0 
   0 0 0 
    0 0 
     0 
```

## [#4 - Maze Game](https://github.com/mrazam110/problem-solving-python/blob/master/Source/maze.py)
User needs to move '2' to the top right '0', and '1' is a wall and '0' is a ground and user is '2'
```bash
$ python3 maze.py
['2', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: right
['0', '2', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: down
['0', '0', '1', '0', '0']
['1', '2', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: down
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '2', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: down
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '2', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: down
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '2', '0', '0', '1']
Enter direction up/down/left/right: right
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '2', '0', '1']
Enter direction up/down/left/right: right
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '2', '1']
Enter direction up/down/left/right: right
cant go right
Enter direction up/down/left/right: up
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '2', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: up
['0', '0', '1', '0', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '2', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: up
['0', '0', '1', '0', '0']
['1', '0', '1', '2', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: up
['0', '0', '1', '2', '0']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Enter direction up/down/left/right: right
['0', '0', '1', '0', '2']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '1', '0', '1']
['1', '0', '0', '0', '1']
Congradulations you won!!
```
