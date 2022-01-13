import pygame
import random
from comet import Comet

class CometFallEvent:

  def __init__(self, game):
    self.percent = 0
    self.percent_speed = 8

    self.game = game
    self.all_comets = pygame.sprite.Group()

    self.fall_mode = False

  def comet_fall(self):
    for i in range(random.randint(5,10)):
      self.all_comets.add(Comet(self))

  def add_percent(self):
    self.percent += self.percent_speed / 100

  def is_fully_loaded(self):
    return self.percent >= 100

  def attempt_fall(self):
    if self.is_fully_loaded() and len(self.game.all_monsters) == 0:
      self.comet_fall()
      self.fall_mode = True # Activates the event

  def update_bar(self, surface):
    # update the values / trigger things
    self.add_percent()
    
    # draw the bar and it's bg
    pygame.draw.rect(surface, (0,0,0), [0,surface.get_height() - 20,surface.get_width(),10])
    pygame.draw.rect(surface, (187,11,11), [
      0, # x
      surface.get_height() - 20, # y
      (surface.get_width() / 100) * self.percent, # width
      10 # height
    ])

