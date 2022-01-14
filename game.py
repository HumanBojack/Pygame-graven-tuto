import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sound import SoundManager

class Game:

  def __init__(self):
    self.has_started = False
    # create player and add it to a group (where he's alone)
    self.all_players = pygame.sprite.Group()
    self.player = Player(self)
    self.all_players.add(self.player)

    self.score = 0
    self.font = pygame.font.Font("pygame/assets/SourceSansPro-Regular.ttf", 25) # To load a system font : pygame.font.SysFont("monospace", 16)

    self.comet_event = CometFallEvent(self)
    self.all_monsters = pygame.sprite.Group()
    self.pressed = {}

    self.sound_manager = SoundManager()

  def update(self, screen):
    # show the score on the screen
    score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
    screen.blit(score_text, (20, 20))

    # Show the player image
    screen.blit(self.player.image, self.player.rect)

    # update player's health bar
    self.player.update_health_bar(screen)

    # update the game event bar
    self.comet_event.update_bar(screen)

    # update player animation
    self.player.update_animation()

    # move player projectiles
    for projectile in self.player.all_projectiles:
      projectile.move()

    # make monsters walk,  update their health bar and animate them
    for monster in self.all_monsters:
      monster.forward()
      monster.update_health_bar(screen)
      monster.update_animation()

    # make comets fall
    for comet in self.comet_event.all_comets:
      comet.fall()

    # Show the projectile image(s)
    self.player.all_projectiles.draw(screen)

    # show the monster image(s)
    self.all_monsters.draw(screen)

    # show the comet image(s)
    self.comet_event.all_comets.draw(screen)

    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
      self.player.move_right()
    elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
      self.player.move_left()

  def start(self):
    self.has_started = True
    for i in range(2):
      self.spawn_monster(Mummy)
    self.spawn_monster(Alien)

  def game_over(self):
    # reset game and player
    self.all_monsters = pygame.sprite.Group() # reset the all monsters group
    self.comet_event.all_comets = pygame.sprite.Group()
    self.comet_event.percent = 0 # resets the bar advancement
    self.player.health = self.player.max_health
    self.has_started = False
    self.score = 0
    self.sound_manager.play("game_over")

  def spawn_monster(self, monster_class_name):
    self.all_monsters.add(monster_class_name.__call__(self))

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)