import pygame

class SoundManager:

  def __init__(self):
      self.sounds = {
        "click": pygame.mixer.Sound("pygame/assets/sounds/click.ogg"),
        "game_over": pygame.mixer.Sound("pygame/assets/sounds/game_over.ogg"),
        "meteorite": pygame.mixer.Sound("pygame/assets/sounds/meteorite.ogg"),
        "shoot": pygame.mixer.Sound("pygame/assets/sounds/tir.ogg")
      }

  def play(self, name):
    self.sounds[name].play()