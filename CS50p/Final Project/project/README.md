# Weather Program for Cities worldwide
### Video Demo:  <https://youtu.be/OKPL_KjFdnI>
### Description:

My project is essentially a simple weather program that tells me the weather of any city of choice from the user. The weather is given in Farenheit and it is also something that changes due to the program accessing weather information from an API call to the following link:
"http://api.weatherapi.com/v1".

How the program works
1. The program allows the user to enter their city either as a command line argument or as actual input.

2. If a user enters their city using command line arguments, the program relies on an object I created through a class called FIX to transform their city into an actual string.

3. If the user enters their city through input, they bypass using the object I created in the FIX class.

4. Once the city is established, an API call is set up using endpoints and an API key provided using the weatherAPI.

5. Once the call is made, the varying functions return the weather as a float or in the case of the "in_program" aka input based function, it returns the float along with the appropriate sentence relating to the city. The main function prints out the appropriate sentences for the command line arguments.

### Testing:

Testing incorporates pytest and unittest. I had to learn and read some documentation on unittest because normal unit testing covered in this course won't suffice for the ever changing outcome that is produced by the weather and also potentially, the user's input or command line argument for the city of choice.

* For unittest, it specifically uses mock and patch which allow for creating controlled scenarios outcomes of my code to test with.

* For unittest, it specifically uses fixture which allows for a certain defined code to be reused for other functions throughout

### Understanding the tests

1. The file imports pytest and the unittest.mock library. Additionally it imports the functions other than main and the class function from project.py for testing
    * For unittest.mock we take the mock and patch decorator
    * If pytest is not already installed be sure to install it through the command line using "pip install pytest"

2. We use the pytest.fixture decorator to reference the function mock_reponse which hold the mock scenario that we want to test for out code
    * This includes successful connection to the API represented by the return of the number 200
    * Dictionary containing the temperature to be accessed if the city of choice chosen is New York

3. What is done in each test of a functions find1, find2, and in_program
- `test_find1`:
    - Mocks the `requests.get` function to simulate API responses.
    - Tests the `find1` function with a predefined mock response and asserts the result.

- `test_find2`:
    - Similar to `test_find1`, it also mocks the `requests.get` function.
    - Tests the `find2` function with a predefined mock response and asserts the result.

- `test_in_program`:
    - Mocks both the `input` function (user input) and the `requests.get` function.
    - Simulates user input to the `in_program` function.
    - Tests the `in_program` function with a predefined mock response and asserts the result.

## Overall

That covers the entire weather project and its associated testing. Feel free to try the program yourself and have FUN!