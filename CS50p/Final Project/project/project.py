'''
Author: Adam Walters
City: Bronx, NY
Country: United States

Description: This project allows the user to access the weather in Farenheits of any city in the world at any time
through entering their city of choice through Command-line argument(s)(no more than three words in its name)  or as input(no limit on words in its name).

'''
import requests # requesting API
import sys #for accepting terminal arguments
import inflect

p = inflect.engine()

class Fix:
    def __init__(self, args):
        self.args = args

    #method/function that creates the city from command line arguments
    def change(self, a):
        return ' '.join(a)

    @property
    def args(self):
        return self._args



    @args.setter
    def args(self, args):
        if isinstance(args, tuple) == False:
            raise ValueError("Please enter a city name")
        #needs condition for setting the city variable
        self._args = args





#main function will check for city(no more than 3 words in name)
def main():
    if len(sys.argv) == 4:
        print(f"It is currently {find1(sys.argv[1],sys.argv[2],sys.argv[3])} degrees farenheit in { ' '.join(sys.argv[1:4])}")
    elif len(sys.argv) == 3:
        print(f"It is currently {find1(sys.argv[1],sys.argv[2])} degrees farenheit in {' '.join(sys.argv[1:3])}")
    elif len(sys.argv) == 2:
        print(f"It is currently {find1(sys.argv[1])} degrees farenheit in {sys.argv[1]}")
    else:
        print(in_program("Enter a city: "))

def in_program(city):
    city = input("Enter city for current weather: ")
    return f"It is currently {find2(city)} degrees farenheit in {city}"



def find1(*args):#3 inputs or read up more on the *args)
    #if user enters city in input
    fx = Fix(args)
    city = fx.change(args)

    #connect to API and get information
    # Define the base URL and API endpoint
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/current.json"

    # API key
    api_key = '1c0515411ab940ba86e23346230909 '

    # Define the query parameter (e.g., for a specific city)
    query_param = f"q={city}"  # Replace with your desired location

    # Construct the complete request URL
    url = f"{base_url}{endpoint}?key={api_key}&{query_param}"

    try:
        # Make the GET request
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            # Successfully received data
            data = response.json()
        else:
            # Handle errors based on the status code
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    weather = data['current']['temp_f']
    return weather




def find2(city):
    #connect to API and get information
    # Define the base URL and API endpoint
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/current.json"

    # API key
    api_key = '1c0515411ab940ba86e23346230909 '

    # Define the query parameter (e.g., for a specific city)
    query_param = f"q={city}"  # Replace with your desired location

    # Construct the complete request URL
    url = f"{base_url}{endpoint}?key={api_key}&{query_param}"

    try:
        # Make the GET request
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            # Successfully received data
            data = response.json()
        else:
            # Handle errors based on the status code
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    weather = data['current']['temp_f']
    return weather



if __name__ == "__main__":
    main()



