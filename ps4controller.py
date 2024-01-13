class Player():
    def __init__(self):
        self.position = [1,6]
        self.color = (100,0,0)
        self.alive = True
    def change_position(self,direction):
        if direction == "right":
            
            self.position[0] += 1
            if self.position[0] == 8:
                self.position[0] = 0
        
        elif direction == "left":
            
            self.position[0] -= 1
            if self.position[0] == -1:
                self.position[0] = 7
        
        elif direction == "up":
            
            self.position[1] -= 1
            if self.position[1] == -1:
                self.position[1] = 7
        
        elif direction == "down":
            
            self.position[1] += 1
            if self.position[1] == 8:
                self.position[1] = 0
                
    def get_position(self):
        if self.alive:
            return self.position[0] + self.position[1]*8
        else:
            return 400
    def switch_off(self):
        
        if self.alive == True:
            self.alive = False
        else:
            self.alive = True
    
#sense.show_message(str(int(sense.get_pressure())))
# 
# 
#sense.show_message(str(int(sense.get_humidity())))
#sense.show_message(str(int(sense.get_temperature())))

