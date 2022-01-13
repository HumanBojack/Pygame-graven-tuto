import pygame
from player import Player
from monster import Monster

class Game:

  def __init__(self):
    self.has_started = False
    self.all_players = pygame.sprite.Group()
    self.player = Player(self)
    self.all_players.add(self.player)
    self.all_monsters = pygame.sprite.Group()
    self.pressed = {}

  def update(self, screen):
    # Show the player image
    screen.blit(self.player.image, self.player.rect)

    # update player's health bar
    self.player.update_health_bar(screen)

    # get player projectiles
    for projectile in self.player.all_projectiles:
      projectile.move()

    # make monsters walk and update their health bar
    for monster in self.all_monsters:
      monster.forward()
      monster.update_health_bar(screen)

    # Show the projectile image(s)
    self.player.all_projectiles.draw(screen)

    # show the monster image(s)
    self.all_monsters.draw(screen)

    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
      self.player.move_right()
    elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
      self.player.move_left()

  def start(self):
    self.has_started = True
    for i in range(2):
      self.spawn_monster()

  def game_over(self):
    # reset game and player
    self.all_monsters = pygame.sprite.Group()
    self.player.health = self.player.max_health
    self.has_started = False

  def spawn_monster(self):
    self.all_monsters.add(Monster(self))

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)