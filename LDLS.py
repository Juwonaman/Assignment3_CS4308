class LDLS:
    MAX_L = 10  # Maximum allowed length
# a class definition with max length to set the maximum allowed length of the strings
    def __init__(self, initial_value=""):
        # Initialize the instance with an initial value, raising an error if it exceeds MAX_L
        if len(initial_value) > self.MAX_L:
            raise RuntimeError("Value exceeds max length of 10.")
        self.value = initial_value
# a constructor that is called when the class is created it takes in the initial value, inside we are checking if the length of the initial value exceeds the max length of 10 and if it does it returns a runtimeerror
    # if the length is good it will assign the initial value to the instance variable self.value
    def nextN(self, newS):
        # Add a new string if it doesn't exceed the max length, else raise an error
        if len(self.value) + len(newS) > self.MAX_L:
            raise RuntimeError("Adding this value exceeds max length of 10.")
        self.value += newS
# add nextN adds new string to the existing string if the length does not exist 10. if it does it also throws an error. but if it is valid it adds it.
    def __str__(self):
        return self.value
# this method converts the a string
try:
    # Take initial value as input
    initial_value = input("Enter the initial string for LDLS (max 10 characters): ")
    ldls = LDLS(initial_value)
    # Create LDLS object with initial value
    print("Initial value:", ldls)

    # Take additional strings to add until an error occurs or user stops
    while True:
        new_string = input("Enter a string to add to LDLS (or type 'stop' to end): ")
        if new_string.lower() == 'stop':
            break
        ldls.nextN(new_string)  # Use nextN method to add new string
        print("Updated value:", ldls)

except RuntimeError as e:
    print("Error:", e)
