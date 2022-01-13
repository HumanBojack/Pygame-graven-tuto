import pygame
import random

class Monster(pygame.sprite.Sprite):

  def __init__(self, game):
    super().__init__()
    self.game = game
    self.health = 100
    self.max_health = 100
    self.attack = 0.3
    self.image = pygame.image.load("pygame/assets/mummy.png")
    self.rect = self.image.get_rect()
    self.rect.x = 1000 + random.randint(0, 300)
    self.rect.y = 550
    self.velocity = random.randint(1, 3)

  def damage(self, amount):
    self.health -= amount

    if self.health <= 0:
      # make it respawn (you ccould also delete it, but it saves memory)
      self.rect.x = 1000 + random.randint(0,300)
      self.velocity = random.randint(1, 3)
      self.health = self.max_health

  def forward(self):
    if not self.game.check_collision(self,self.game.all_players):
      self.rect.x -= self.velocity
    else:
      self.game.player.damage(self.attack)

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
    pygame.draw.rect(surface, (111,210,46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])