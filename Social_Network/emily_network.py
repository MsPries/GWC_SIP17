'''
This program simulates a basic social network.
This file contains the User and Network classes and starts testing each using
the main method.
'''

###### The User class starts here ######
class User:
    def __init__(self, user_name, user_id): # User constructor - requires user_name and user_id
        self.user_name = user_name
        self.user_id = user_id
        self.connections = [] # A list of the other Users this person is connected to (currently user_names)

    # Getter methods: getUserName, getUserId, getConnections
    def getUserName(self):
        return self.user_name

    def getUserId(self):
        return self.user_id

    def getConnections(self):
        return self.connections

    # Setter method: addConnection
    def addConnection(self, other_user_name):
        self.connections.append(other_user_name)

###### End of User class ######

###### The Network class starts here ######
class Network:
    def __init__(self): # Network constructor
        self.users = [] # A list of User objects

    # Getter methods: numUsers, getUserId
    def numUsers(self):
        return len(self.users) # len means length

    def getUserId(self, user_name):
        for index in range(len(self.users)):
            possible_user = self.users[index] # Remember: index and user_id are equivalent here
            if (possible_user.getUserName() == user_name):
                return possible_user.getUserId() # We found a match
        return -1 # We didn't find a User with that user_name

    # Setter methods: addUser, addConnection
    def addUser(self):
        new_user_name = input("Create a new user name: ")
        new_user_id = len(self.users) # We choose id based on index
        new_user = User(new_user_name, new_user_id) # Create a new User
        self.users.append(new_user) # Add that new User to our users list

    def addConnection(self, user_name1, user_name2):
        user_id_1 = self.getUserId(user_name1)
        user_id_2 = self.getUserId(user_name2)

        if (user_id_1 == -1 or user_id_2 == -1):
            print("Users are not in the network.")
        else:
            user1 = self.users[user_id_1]
            user2 = self.users[user_id_2]

            user1.addConnection(user_name2)
            user2.addConnection(user_name1)

###### End of Network class ######

###### Main method: currently countains testing ######
def main():
    appnexus_employee = User("AppNexus", 12) # Create a new User
    print(appnexus_employee.getUserName()) # Print that User's name to test

    net = Network() # Create a new Network
    net.addUser() # Add a User to the Network
    print(net.getUserId("cassandra")) # Print the user_id of the User with user_name "cassandra"

###### End of main method ######

###### What should our program do when this file is run directly? ######
if __name__ == "__main__":
    main()
