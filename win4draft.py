import random


class Person:
    def __init__(self):
        self.rooms_visited = []
    def choice(self,x):
        self.choice = x

class Room:
    def __init__(self):
        pass
    rooms = ['room1','room2','room3','room4','room5','room6']

class Description:
    def __init__(self):
        pass
    desc1 = 'Sorry, this room is empty.'
    desc2 = 'You have got a ladder.'
    desc3 = 'You have got a key.'
    desc4 = 'You have got the safe box.'
    all_desc = [desc1,desc2,desc1,desc3,desc1,desc4]
class Game:
    def start_input(self):
        opt1 = input ('There are six rooms to explore, numbered from '1' to '6'. \nPress a number  of your choice or 'q' to quit the game.')
        while opt1 not in ['1','2','3','4','5','6','q']
            opt1 = input ('Wrong key, please try again.')
        if opt1 == 'q':
            print ('Goodbye!')
        else:
            print(self.room_desc[int(opt1)-1])
            if 

        
        
    def __init__(self):
        self.room_desc = {}
        random.shuffle(rooms)
        for i<6:
            self.room_desc.append(rooms[i]:all_desc[i])
        print(Welcome to Adventure Game! In this game your goal is to open a safe box with in x minutes.\n
              Inorder to open the safe you need to use a ladder and a key.

    def play(self):
        p
        
