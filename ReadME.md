# JAVA



# first step
    sort the list 

# second step
    add first 2 indeces of the list ~ sum 

# third step
    remove the two indeces and add the sum to the list 

# forth step
    sort the list

# finally
    repeat for as long as lenth of the list is less that 1



# Python ~~  Task Scheduler
     Problem

    We are given a list of tasks (like ['A', 'B', 'A', 'B']) and a cooling period n.
    After running a task, we must wait n time units before running the same task again.
    If no task is ready, the CPU must stay idle.
    We need to find the minimum total time (including idle time) to finish all tasks.

## Approach 
    ~ Count how many of each task we need to run.
    ~ Keep track of when each task can run again using a dictionary.
    ~ Loop through each time unit:
    ~ Pick any task that is ready and still has work left.
    ~ If no task is ready, the CPU goes idle.
    ~ Stop when all tasks are done and return the total time.
    ~ This approach is simple and simulates the ~ ~ ~ process step by step — great for understanding before optimizing.


# SIMPLIFY_PATH (both java and python)

    ~ You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

## The rules of a Unix-style file system are as follows:

    ~  A single period '.' represents the current directory.

    ~  A double period '..' represents the previous/parent directory.

    ~  Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.

    ~  Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. 
    
    ~  For example, '...' and '....' are valid directory or file names.

    ~  The simplified canonical path should follow these rules:

    ~  The path must start with a single slash '/'.

    ~  Directories within the path must be separated by exactly one slash '/'.

    ~  The path must not end with a slash '/', unless it is the root directory.

    ~  The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.