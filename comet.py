import pygame
import random

class Comet(pygame.sprite.Sprite):

  def __init__(self, comet_event):
    super().__init__()
    self.image = pygame.image.load("pygame/assets/comet.png")
    self.rect = self.image.get_rect()
    self.velocity_y = random.randint(1, 3)
    self.rect.x = random.randint(20, 800)
    self.rect.y = - random.randint(0, 800)
    self.comet_event = comet_event

  def remove(self):
      self.comet_event.all_comets.remove(self)

      if len(self.comet_event.all_comets) == 0:
        self.comet_event.percent = 0
        for i in range(2):
          self.comet_event.game.spawn_monster()

    
  def fall(self):
    self.rect.y += self.velocity_y

    if self.rect.y >= 530:
      self.remove()

      if len(self.comet_event.all_comets) == 0:
        self.comet_event.percent = 0
        self.comet_event.fall_mode = False

    # If the comet falls on the player, deal damage
    if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
      self.remove()
      self.comet_event.game.player.damage(20)