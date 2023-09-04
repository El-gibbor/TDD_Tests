# Task 0 - add_integer
- **Document your module, classes and functions:**  
    - All your modules (files), classes, and functions (inside and outside a class) should have documentation. check [here](https://intranet.alxswe.com/rltoken/dOO785g5EQYkRU2E1wri0g) to learn how to document your module and functions/methods.  
    - Your documentation must be a real sentence explaining what's the purpose of the module(file), class or method because the length of it will be verified.
    - Validate the length of your module documentation with `python3 -c 'print(__import__("your_module").__doc__)' | wc -l`. Replace `your_module` with the name of your file without the `.py` extension, and this should print at least **5**.
    - Do the same for your function documentation with `python3 -c 'print(__import__("your_function").add_integer.__doc__)' | wc -l` Replace `your_function` with the name of your function, and this should print at least **3**.
## Try them first in your Python shell 💫
Write the given function in your Python interactive shell and check what the output is. if it is a valid computation and returns the expected output, then that should be the same as your test.   
also, examine the traceback call and Exceptions raised for failed or invalid computations, Your test should also have similar outputs when validating/testing such cases, except for where we are given a certain type of Exception and error message to raise, then you replace/use the exact Exception and error message provided in the task for it.
  
See below for what I mean:  
```REPL
>>> def add_integer(a, b=10):
...     return int(a) + int(b)
... 
>>> add_integer(5, 10)
15
```
Failed or Invalid computation  
```
>>> add_integer(10, "boy")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add_integer
ValueError: invalid literal for int() with base 10: 'boy'
```
you only need the traceback line and the Exception error line. if the Exception Type and error message don't tally with what was provided for us to use in the task, then you make use of the Exception type and error message provided for you in the intranet.  
## Test Cases 
- **Test:** Correct sum of two integers -> `(5, 10)`
- **Test:** Correct sum of a positive and a negative integer. -> `(5, -10)`
-  **Test:** Correct sum of a float and positive integer -> `(5.5, 10)`. Remember, your return value is cast to an integer. so this should return an absolute integer value.
-  **Test:** Do same for a negative integer with a float value -> `(5.5, -5)`. should return an absolute integer value too.
-  **Test:** Invalid! summing an int with a different datatype -> `(5, "10")` - pass in a traceback call with its correct Exception and error message.
-  **Test:** Check for NAN (not a number) which is undefined or unrepresentable -> `(3, float('NAN'))` - Try this on your Python shell to know the output. (Exception type and error msg)
-  **Test:** Float negative infinity - `add_integer(float('-inf') flaot('-inf'))` - Try it in your Python shell to see the output.
     - Incase you care, you can learn/know about [Float infinity values](https://favtutor.com/blogs/infinity-python) in python.
- **Test:** Missing one argument -> `add_integer(10)`. Your func already has one default positional argument - `add_integer(a, b=89)`. so this returns a valid result.
- **Test:** Missing both arguments/empty parameter -> `add_integer(None)` - this should raise an Exception for 'a' because 'b' has a default positional argument
- **Test:** Float overflow -> `add_intger(float('inf'), float('inf'))` - Try in your python shell too.
  
*Edit this readme and add yours right after the last test case 👆. If you are not yet good with markdown/readme formatting, then you can create a test file (eg: `add_int_test.txt`) inside  `task_0` directory and type in all the posible test and edge cases you have.*
