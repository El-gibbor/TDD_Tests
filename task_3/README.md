# Task 3 - Print_square 
- **Document your module, classes and functions:**  
    - All your modules (files), classes, and functions (inside and outside a class) should have documentation. check [here](https://intranet.alxswe.com/rltoken/dOO785g5EQYkRU2E1wri0g) to learn how to document your module and functions/methods.  
    - Your documentation must be a real sentence explaining what's the purpose of the module(file), class or method because the length of it will be verified.
    - Validate the length of your module documentation with `python3 -c 'print(__import__("your_module").__doc__)' | wc -l`. Replace `your_module` with the name of your file without the `.py` extension, and this should print at least **5**.
    - Do the same for your function documentation with `python3 -c 'print(__import__("your_function").add_integer.__doc__)' | wc -l` Replace `your_function` with the name of your function, and this should print at least **3**.
## Testing with your Python Shell 🐍
Leveraging the Python shell can be incredibly beneficial. Here are some tips to make the most of it:  
Explore Various Inputs: Use the Python shell to experiment with different inputs. Test your code with a variety of values and scenarios to ensure it behaves as intended.
Verify Expected Output: Check if your code produces the expected output for the given inputs. If the computed result matches your expectations, consider it a successful test case.
Handle Exceptions: Pay attention to any traceback calls and exceptions raised during testing. Your test cases should handle these exceptions appropriately. If the task specifies a particular exception type and error message, ensure your code matches these requirements.
## Test Cases  
- Test for when a negative integer is passed as the `size` length of the square.
- Test for an invalid input where the size argument is a string.
- Test for valid integer value and Validate that the function correctly prints a square of that `size`.
    - Ensure that regular cases where a positive integer is provided for the `size` argument pass successfully.
- Test for valid inputs where the argument `size` is an integer greater than zero and correctly prints the square.
-  Test for invalid inputs where `size` is not an integer and confirm the appropriate Exception and massage is raised.  
-  Test for missing arguments.
