from sense_hat import SenseHat
import random as rd
import time
import threading
from pyPS4Controller.controller import Controller
from ps4controller import Player

class MyController(Controller):
    def __init__ (self, **kwargs):
        Controller.__init__(self,**kwargs)

    def on_x_press(self):
        runner.switch_off()
        if runner.alive == True:
            tier.revive_player()
        if runner.alive == False:
            tier.delete_player()
    def on_square_press(self):
        tier.fillMapIndexes([0,9,10,16,17])
        tier.neighbor_finder()
    def on_triangle_press(self):
        tier.fillMapIndexes([17,18,19,20,24,28,36,40,43])
        tier.neighbor_finder()
    def on_circle_press(self):
        tier.clearMap()
        sense.clear()

    def on_up_arrow_press(self):
        runner.change_position("up")
    def on_left_arrow_press(self):
        runner.change_position("left")
    def on_right_arrow_press(self):
        runner.change_position("right")
    def on_down_arrow_press(self):
        runner.change_position("down")

    def on_L3_up(self,value):
        runner.change_position("up")
        time.sleep(0.1)
    def on_L3_left(self,value):
        runner.change_position("left")
        time.sleep(0.1)
    def on_L3_right(self,value):
        runner.change_position("right")
        time.sleep(0.1)
    def on_L3_down(self,value):
        runner.change_position("down")
        time.sleep(0.1)

class TileMap():
    def __init__(self):
        self.tiles = []

    def fillMapRandomly(self):
        self.tiles = []
        i = 0 
        while i < 64:
            power = rd.choice([True,False])
            self.tiles.append(Tile(i,power))
            i+=1

    def fillMapIndexes(self,indexes):
        for tile in self.tiles:
            if tile.power == True:
                indexes.append(tile.index)

        self.tiles = []
        i = 0

        while i < 64:
            if i == runner.get_position():
                self.tiles.append(Tile(i,False,player=True))
            elif i in indexes:
                self.tiles.append(Tile(i,True))
            else:
                self.tiles.append(Tile(i,False))
            i+=1


    def clearMap(self):
        self.tiles = []
        i = 0
        while i < 64:
            if i == runner.get_position():
                self.tiles.append(Tile(i,False,player=True))
            else:
                self.tiles.append(Tile(i,False))
            i+=1
    def get_displayMap(self):
        display_map = []
        for tile in self.tiles:
            display_map.append(tile.get_tile())

        return display_map

    def neighbor_finder(self):
        for tile in self.tiles:
            tile.set_neighbors()

    def check_survival(self):
        tempList = []

        i = 0
        while i < len(self.tiles):
            liveCounter = 0
            for neighbor in self.tiles[i].neighbors:   
                if self.tiles[neighbor].player == True:
                    liveCounter += 1
                elif self.tiles[neighbor].power == True:
                    liveCounter += 1
            if i == runner.get_position():
                tempList.append(Tile(i,False,player=True))
            elif self.tiles[i].power == True:        
                if liveCounter == 2 or liveCounter == 3:
                    tempList.append(Tile(i,True))
                else:
                    tempList.append(Tile(i,False))
            else:
                if liveCounter == 3:
                    tempList.append(Tile(i,True))
                else:
                    tempList.append(Tile(i,False))
            i+=1
        self.tiles = tempList
        self.neighbor_finder()


    def print_specific_neighbors(self,index):
        print(self.tiles[index].neighbors)

    def delete_player(self):

        for tile in self.tiles:
            if tile.player == True:

                tile.player = False
                tile.color = (0,0,0)
                tile.power = False
    def revive_player(self):
        for tile in self.tiles:
            if tile.index == runner.get_position():
                tile.player = True

class Tile():
    def __init__(self,index,power:bool,player = False):
        self.index = index
        self.power = power
        self.player = player

        if self.player == True:
            self.color = (0,100,0)
        elif self.power == True:
            #self.color = (0,100,0)
            self.color = self.temperature_to_color()
        else:
            self.color = (0,0,0)

        #self.tile = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
        self.neighbors = []

    def temperature_to_color(self):
        temperature = sense.get_temperature()
        normalized_temp = (temperature -20) / 20
        red = int(255*normalized_temp)
        blue = int(255*(1-normalized_temp))

        green = 0
        red = max(0,min(red,255))
        bue = max(0,min(blue,255))

        return red, green, blue

    def get_tile(self):
        return self.color

    def set_neighbors(self):

        if self.index == 0:
            self.neighbors = [63,56,57,7,1,15,8,9]
        elif self.index == 7:
            self.neighbors = [62,63,56,6,0,14,15,8]
        elif self.index == 56:
            self.neighbors = [55,48,49,63,57,7,0,1]
        elif self.index == 63:
            self.neighbors = [54,55,48,62,56,6,7,0]
        elif self.index < 7:
            self.neighbors = [56+self.index%8-1,56+self.index%8,56+self.index%8+1 ,self.index-1,self.index+1,self.index+7,self.index+8,self.index+9] 
        elif self.index > 56:
            self.neighbors = [self.index-9,self.index-8,self.index-7,self.index-1,self.index+1,self.index%8-1,self.index%8,self.index%8+1]
        elif self.index % 8 == 0:
            self.neighbors = [self.index-1,self.index-8,self.index-7,self.index+7,self.index+1,self.index+15,self.index+8,self.index+9]
        elif self.index == 15 or self.index == 23 or self.index == 31 or self.index == 39 or self.index == 47 or self.index == 55:
            self.neighbors = [self.index - 9,self.index-8,self.index-15,self.index-1,self.index-7,self.index+7,self.index+8,self.index+1]
        else:
            self.neighbors = [self.index-9,self.index-8,self.index-7,self.index-1,self.index+1,self.index+7,self.index+8,self.index+9]

controller = MyController(interface="/dev/input/js0",connecting_using_ds4drv=False)
sense = SenseHat()


tier = TileMap()
tier.fillMapRandomly()
runner = Player()
glider = [0,9,10,16,17]
lwss = [1,2,3,4,8,12,20,24,27]

def update():
    sense.set_pixels(tier.get_displayMap())
    sense.set_pixels()
def run():
    while True:   

        #sense.set_pixel(runner.position[0],runner.position[1],runner.color)
        tier.check_survival()
        sense.set_pixels(tier.get_displayMap())
        time.sleep(0.2)

def main():

    x = threading.Thread(target=controller.listen,args=(1,))  
    x.start()
    run()


sense.clear()
main()
