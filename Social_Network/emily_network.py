class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    def getUserName(self):
        return self.user_name

    def getUserId(self):
        return self.user_id

    def getConnections(self):
        return self.connections

    def addConnection(self, other_user_name):
        self.connections.append(other_user_name)
