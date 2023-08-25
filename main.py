print("Hello World")



'''
given an unfinished sudoku puzzle, solve it
    - assume its solvable
    - must be strategic - trying each combination would take too long (~9 ^50)
    - must be easy to debug. Include .show(), should be step by step process

strategies
    - look at all instances of a single number, and try to find more certainties of that number
        - it would be nice to have a reference to each instance of a number
            - an array of indicies (size 9)
            - index: could be (x, y) or could include square location. (which square, which location in the square)
                - prob don't really need which location in the square. If I include location within the square, it could be 1-9 or (a, b) 3x3
        - this is my first strategy as a human
        - "is there a 1 in the first second and/or third row?", "is there a 1 in the first, second, and/or third column?"
            - these have to be connected
            - "given a 3x3 array (or 9 indices), how many spots are available where there's no 1 in that row, column, and also no number in that spot"
                - this is good because its obvious how to iterate through a box in this way
        - I almost want to create a data structure for each: rows, columns, boxes, number locations, and then update them all simultaneously
            - as I'm building I can see what's the most helpful
    - questions: what is the runtime of checking a number in a box based on the above strategy
        - each box has an adjustment which, when added to the row / column # of the specific number in the box gets the overall row / column
        - for each position in the box (9), available = (no existing number) && (no "1" in the row) && (no "1" in the column)
            - if only one is available, then put a 1 in there and update the data structures
            - if more than one is available, at some point I may want to think about "notations" but I'll save that for later
    - if a row or column has 8 filled, fill it in with the 9th


In summary, the strategies that I will be using to start with:
    - for each position in a given box (9), the position is available if (no existing number in position) && (no "1" in the row) && (no "1" in the column)
        - if there's only one available position for a given number in the box, then fill it in
    - for each position in a given row, the position is available if (no existing number in the position) && (no "1" in the column) && (no "1" in the box)
    - for each position in a given column....

    Now, the problem is, if I go through all of these strategies for each number once, no issue. But I might need to do this a bunch of times
    - I need a mechanism to know how many positions were checked & filled by a given strategy
    - I need a mechanism to "play" the sudoku solver step by step 
    
Other mechanisms
    - print current sudoku box
    - print data structures (for debugging)
    - update the data structures when I'm adding a number

I feel fairly confident that this strategy on its own won't be enough, because it will take too long. Including box size, row/column size, and # numbers will
help direct the energy of the program to the right spots, so maybe this will help. With that addition, this might do well on easy sudokus (or more?)

'''




## Need a data structure to store the numbers