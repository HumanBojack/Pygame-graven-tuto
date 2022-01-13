import pygame

class AnimateSprite(pygame.sprite.Sprite):

  def __init__(self, name):
    super().__init__()
    self.image = pygame.image.load(f"pygame/assets/{name}.png")
    self.current_image = 0
    self.images = animations.get(name)
    self.animation = False

  def start_animation(self):
    self.animation = True

  def animate(self, loop=False):
    if self.animation:
      self.current_image += 1

      if self.current_image >= len(self.images):
        self.current_image = 0
        if not loop:
          self.animation = False
      
      self.image = self.images[self.current_image]



# load all animations for a given sprite. Doing it here avoids some lag
def load_animation_images(sprite_name):
  images = []
  path = f"pygame/assets/{sprite_name}/{sprite_name}"

  # loop through images in the folder and add them to the array
  for num in range(1,25):
    images.append(pygame.image.load(path + str(num) + ".png"))

  return images

animations = {
  "mummy": load_animation_images("mummy"),
  "player": load_animation_images("player")
}
