import pygame
import random
import animation

class Monster(animation.AnimateSprite):

  def __init__(self, game, name, size, offset=0):
    super().__init__(name, size)
    self.game = game
    self.health = 100
    self.max_health = 100
    self.attack = 0.3
    self.rect = self.image.get_rect()
    self.rect.x = 1000 + random.randint(0, 300)
    self.rect.y = 550 - offset
    self.loot_amount = 1

    self.start_animation()

  def set_speed(self, speed):
    self.default_speed = speed
    self.velocity = random.randint(1, 3)

  def damage(self, amount):
    self.health -= amount

    if self.health <= 0:
      # make it respawn (you ccould also delete it, but it saves memory)
      self.rect.x = 1000 + random.randint(0,300)
      self.velocity = random.randint(1, self.default_speed)
      self.health = self.max_health

      if self.game.comet_event.is_fully_loaded():
        self.game.all_monsters.remove(self)
        self.game.comet_event.attempt_fall()

      # add points to the score
      self.game.score += self.loot_amount

  def forward(self):
    if not self.game.check_collision(self,self.game.all_players):
      self.rect.x -= self.velocity
    else:
      self.game.player.damage(self.attack)

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
    pygame.draw.rect(surface, (111,210,46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

  def update_animation(self):
    self.animate(loop=True)

# define a mummy class
class Mummy(Monster):

  def __init__(self, game):
    super().__init__(game, "mummy", (130,130))
    self.set_speed(3)
    self.loot_amount = 20

# define an alien class
class Alien(Monster):

  def __init__(self, game):
    super().__init__(game, "alien", (300,300), 130)
    self.health = 250
    self.max_health = 250
    self.set_speed(1)
    self.attack = 0.8
    self.loot_amount = 80
