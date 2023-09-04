# Task 0 - add_integer
- **Document your module, classes and functions:**  
    - All your modules (files), classes, and functions (inside and outside a class) should have documentation. check [here](https://intranet.alxswe.com/rltoken/dOO785g5EQYkRU2E1wri0g) to learn how to document your module and functions/methods.  
    - Your documentation must be a real sentence explaining what's the purpose of the module(file), class or method because the length of it will be verified.
    - Validate the length of your module documentation with `python3 -c 'print(__import__("your_module").__doc__)' | wc -l`. Replace `your_module` with the name of your file without the `.py` extension, and this should print at least **5**.
    - Do the same for your function documentation with `python3 -c 'print(__import__("your_function").add_integer.__doc__)' | wc -l` Replace `your_function` with the name of your function, and this should print at least **3**.
## Testing with your Python Shell 🐍
Leveraging the Python shell can be incredibly beneficial. Here are some tips to make the most of it:  
- **Explore Various Inputs:** Use the Python shell to experiment with different inputs. Test your code with a variety of values and scenarios to ensure it behaves as intended.  
- **Verify Expected Output:** Check if your code produces the expected output for the given inputs. If the computed result matches your expectations, consider it a successful test case.
- **Handle Exceptions:** Pay attention to any traceback calls and exceptions raised during testing. Your test cases should handle these exceptions appropriately. If the task specifies a particular exception type and error message, ensure your code matches these requirements.    
## Test Cases 
- Test for the Correct sum of two integers  
- Test for the Correct sum of a positive and a negative integer.  
-  Test for the Correct sum of a float value and a positive integer  
- Test for the correct sum of a negative integer with a float value  
-  Test for an integer with a different datatype (str)  
- Check for an integer with NAN (not a number) which is undefined or unrepresentable. You can do this by trying to cast 'NAN' into a float.  
-  Check for Float negative infinity - `float('-inf')` - Learn/know about [Float infinity values](https://favtutor.com/blogs/infinity-python) if you care.
- Check for one missing argument  
- Test for both missing arguments/empty parameter - you can pass in `None` to check for this.  
- Test for Float overflow `(float('inf')`  
  
*Edit this readme and add yours right after the last test case 👆. If you are not yet good with markdown/readme formatting, then you can create a test file (eg: `add_int_test.txt`) inside  `task_0` directory and type in all the posible test and edge cases you have.*
