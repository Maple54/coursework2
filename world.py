import pygame,os
from states import State




class main_game(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.map = os.path.join(self.game.assets_dir,'graphics/untitled.tmx')
        
    def update(self, delta_time, actions):
      pass


    def render(self, display):
      display.blit(self.map,(0,0))
      pass


        

