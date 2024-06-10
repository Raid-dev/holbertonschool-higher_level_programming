#!/usr/bin/env python3
"""serialize and deserialize custom Python objects
   using the pickle module. """


class CustomObject:
    """CustomObject class"""

    def __init__(self, name, age, is_student):
        """init method """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method to print out the objects attributes """

        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """method will use the pickle module, it will serialize the
           current instance of the object and save it to the provided
           filename. """

        import pickle
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error occurred:", e)

    @classmethod
    def deserialize(cls, filename):
        """method will use the pickle module, it will load and return an
           instance of the CustomObject from the provided filename. """

        import pickle

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("File not found.")
            return None
        except pickle.UnpicklingError:
            print("Error occurred while unpickling.")
            return None
        except Exception as e:
            print("Error occurred:", e)
            return None
