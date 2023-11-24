# Importing the ABC (Abstract Base Class) module from the abc package
from abc import ABC, abstractmethod

# Creating an abstract class named User that inherits from ABC
class User(ABC):
    # Constructor method to initialize the User object with name, email, and nid
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.__id = 0  # Private attribute, as indicated by the double underscores
        self.__nid = nid  # Private attribute, storing a National ID
        self.wallet = 0  # Attribute to store the user's wallet balance
    
    # Abstract method that must be implemented by any concrete subclass
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError  # Indicating that the method must be overridden in subclasses

# Creating a concrete subclass named Rider, inheriting from the abstract class User
class Rider(User):
    # Constructor method for initializing Rider objects, taking name, email, and nid as parameters
    def __init__(self, name, email, nid):
        current_ride = None  # Initializing a variable to hold the current ride information (not used in the provided code)
        # Calling the constructor of the parent class (User) to initialize common attributes
        super().__init__(name, email, nid)

    # Implementation of the abstract method display_profile from the parent class User
    def display_profile(self):
        print(f'Rider: {self.name} using {self.email}')

    # Method to request a ride, taking location and destination as parameters
    def request_ride(self, location, destination):
        # Checking if the rider doesn't have a current ride
        if not self.current_ride:
            ride_request = None  # Creating a ride request object (not used in the provided code)
            self.current_ride = None  # Setting the current ride to None (not used in the provided code)
