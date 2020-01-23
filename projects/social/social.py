import random #to get shuffle
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        # SEEDING FUNCTION
        # USERS AND AVG # OF FRIENDSHIPS
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # To create N random friendships, you could create a list with all possible 
        # friendship combinations, shuffle the list, then grab the first N elements 
        # from the list. You will need to `import random` to get shuffle.
        
        possible_friendships = [] #list of possible friendships
        
        #nested loops for all possiblities 
        for user_id in self.users: #get id of all users
            for friend_id in range(user_id+1, self.last_id+1): 
                #wouldn't work without self, why?
                #data is ordered just loop through and add +1 move forward 1
                #connection already made no need to go back
                possible_friendships.append((user_id, friend_id)) 
                #TypeError: append() takes exactly one argument (2 given) needs two ()
                #append to empty list above
        #shuffle the list        
        random.shuffle(possible_friendships)

        all_friendships = num_users * avg_friendships
        for i in range(all_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()  # Instantiate a queue

        q.enqueue([user_id]) #enqueue list of user ids in order to build path

        while q.size() > 0:
            path = q.dequeue()
            user = path[-1]
            print('THIS IS PATH', path)
            print('THIS IS USER', user)

            if user not in visited: 
                #search/traverse through and check / add unvisited node
                visited[user] = path #adds this path/node to dictionary
                print("VISITED CUE", visited)

                for friend in self.friendships[user]: #each edge
                    copy_of_path = path.copy() #avoid error
                    copy_of_path.append(friend)
                    q.enqueue(copy_of_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("FRIENDSHIPS", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("CONNECTIONS",connections)
