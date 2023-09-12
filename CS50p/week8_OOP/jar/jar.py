import emoji

class Jar:
    #this is only for when it is first created so its best to have rules in setter which applies for everytime the class is called
    def __init__(self, capacity=12, size = 0): #12 is default value for capacity. Could be another number or not even a number based on rules I set
        # I dont have the self._ because I want python to do the error checking through the setter
        #if I dont do ._ here then it does not go through the setter and there is no error checking for my variable
        #I could also just have the error checking applied here
        self.capacity = capacity #instance variable
        self.size = size


    #special method that does overriding by allowing my object to be seen as a string and not memory location
    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Passes capacity")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Taking more than is available")
        self.size -= n


    #getter
    @property #attribute we have more control over, so a rule set in this must be met by a function that calls the class
    def capacity(self): #getter method for capacity
        return self._capacity

    @capacity.setter
    def capacity(self, capacity): #setter method for capacity
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    #getter
    @property
    def size(self): #getter method for size
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size is greater than capacity")
        self._size = size




def main():
    jar = Jar(25)
    jar.deposit(5)
    print(jar)
    jar.withdraw(6)
    print(jar)


if __name__ == "__main__":
    main()