# Task 1 - matrix_divided  
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
- Input Validation:  
    - Check if the input matrix is a list of lists.
    - Ensure that all elements within the matrix are integers or floats.
    - Verify that the divisor is a non-zero integer or float.
- Matrix Structure:
    - Test if each row in the matrix has the same number of elements (rectangular matrix).
    - Create test cases where rows in the matrix have different lengths and validate that your code raises the correct exception.  
    - Check for irregular matrices where some rows have different lengths.
- Division by Zero:  
    - Test the case where the divisor is zero, and ensure it raises a ZeroDivisionError.
- Data Types:  
    - Test for different data types within the matrix (e.g., strings, tuples) and ensure it raises a TypeError.
- Float Overflow:  
    - Test with extremely large divisor values that could cause a floating-point overflow.
Test with special values such as `float('inf')` and `float('nan')` in the matrix.
- Edge Cases:  
    - Test with small matrices (1x1) and large matrices to cover edge cases.
- Output Validation:
    - Validate that the output matrix has the same dimensions as the input matrix.
    - Check if the output values are correctly computed based on the division operation.
- Negative Values:
    - Test with negative integers and floats in the matrix and divisor.  
- Missing or Extra Arguments:  
- Test cases with missing or extra arguments to ensure your code handles them gracefully.
- Testing for Non-List Data Structures:
    - Check if the input matrix contains elements other than lists (e.g., tuples) and handle them appropriately.
- A matrix consisting of lists of integers with one element as `float('inf')` or `loat('nan')`. The divisor is set to `float('inf')` or `float('nan')`
- A matrix consisting of lists of integers with one element as `float('inf')` or `float('nan')`. The divisor is set to an integer value
- validate how your code handles a matrix consisting of a list of lists of integers and The divisor is set to `float('inf')`.
## NB:
Test cases where exceptions (e.g., ZeroDivisionError, TypeError) should be raised, ensure they are raised with the correct messages.
if the message in your test doesn't correspond with the Exception message raised in your code, the test will fail. you can make use of the Exception and error message from the T standard
python Exception if a custom Exception type and message aren't given for such a scenario. e.g.: the `OverFlowError` Exception and its error message.
