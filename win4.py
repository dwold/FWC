import random


class Person:
    def __init__(self):
        self.checked_rooms = []
        self.point = 0
        self.loss = 0
        
class Room:
    def __init__(self):
        self.rooms = ['room1','room2','room3','room4','room5','room6','room7']
        self.rd = {}
        
class Description:
    def __init__(self):
        self.desc1 = 'Empty room.'
        self.desc2 = 'You have got a passcode.'
        self.desc3 = 'You have got a key.'
        self.desc4 = 'You have got a safe box.'
        self.desc5 = 'You have got a magnet.'
        self.all_desc = [self.desc1,self.desc2,self.desc1,self.desc3,self.desc1,self.desc4,self.desc5]


class Game:
    
    def __init__(self):
        self.pe = Person()
        self.de = Description()
        self.rn = Room()
        self.pt = self.pe.point
        self.lo = self.pe.loss
        self.u = self.de.desc1
        self.opt = None
        self.sh = None
        print('''Welcome to Adventure Game!\nIn this game you need to explore seven rooms numbered from \'1\' to \'7\'.
                 \nThe goal is to get a safe box, a magnet, a passscode and a key. Once you had seen a room you cannot go again.\n''')

    def asgn_room(self):
        random.shuffle(self.rn.rooms)
        for i in range (7):
            r = self.rn.rooms[i]
            d = self.de.all_desc[i]
            self.rn.rd[r] = d

    def usr_inpt(self):
        self.opt = input ('''Where do you want to go?
                            \nPress a number  of your choice \'1\' - \'7\' or press \'q\' to quit the game.\n''')
        while self.opt not in ['1','2','3','4','5','6','7','q']:
            self.opt = input ('Wrong key, please try again.')
        if self.opt == 'q':
            print ('Goodbye!')
        else:
            self.play_game()

    def play_game(self):
        if self.opt in self.pe.checked_rooms:
            self.lo -= 10
        self.pe.checked_rooms.append(self.opt)
        self.print_out(self.opt)
        if self.sh != self.u:
            self.pt += 1
        else:
            self.lo -= 1
        if self.pt+self.lo < -1:
            self.end_game(0)
        elif self.pt == 4:
            self.end_game(1)
        else:
            self.usr_inpt()

    def print_out(self,k):
        self.k=k
        if self.k=='1':
            self.sh = self.rn.rd['room1']
        elif self.k=='2':
            self.sh = self.rn.rd['room2']
        elif self.k=='3':
            self.sh = self.rn.rd['room3']
        elif self.k=='4':
            self.sh = self.rn.rd['room4']
        elif self.k=='5':
            self.sh = self.rn.rd['room5']
        elif self.k=='6':
            self.sh = self.rn.rd['room6']
        else:
            self.sh = self.rn.rd['room7']
        print(self.sh)
                
    def end_game(self,c):
        self.code = c
        sc = (self.pt+self.lo)*25
        if self.code==1:
            print('Congratulations! You Won! \n Your point was {}'.format(int(sc)))
        else:
            print('Gameover, you lost the game.\n Your point was {}'.format(int(sc)))

game = Game()
game.asgn_room()
game.usr_inpt()
