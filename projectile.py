import pygame

class Projectile(pygame.sprite.Sprite):

  def __init__(self, player):
    super().__init__()
    self.velocity = 1
    self.image = pygame.image.load("pygame/assets/projectile.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.player = player
    self.rect.x = player.rect.x + 130
    self.rect.y = player.rect.y + 90
    self.origin_image = self.image
    self.angle = 0

  def move(self):
    self.rect.x += self.velocity
    self.rotate()

    # check for collision with monster, remove the projectile and deal damage
    for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
      self.remove()
      monster.damage(self.player.attack)


    # destroy projectile if not on the screen
    if self.rect.x > 1080:
      self.remove()

  def remove(self):
    self.player.all_projectiles.remove(self)


  def rotate(self):
    self.angle += 12
    self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
    self.rect = self.image.get_rect(center=self.rect.center)
