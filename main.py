import pygame
from game import Game

pygame.init() # Initialise pygame

pygame.display.set_caption("Test oui oui")
# pygame.display Permet de nommer la fenetre, voir ses dimensions, parametres d'initialisation
screen = pygame.display.set_mode((1080,720))

# import the background
background = pygame.image.load("pygame/assets/bg.jpg")

# load game
game = Game()

# Une boucle permet de laisser le jeu tourner
running = True
while running :
  # set background
  screen.blit(background, (0,-200))

  # Import banner
  banner = pygame.image.load("pygame/assets/banner.png")
  banner = pygame.transform.scale(banner, (500, 500))
  banner_rect = banner.get_rect()
  banner_rect.x = (screen.get_width() / 2) - (banner.get_width() / 2) - 10

  # Import play button
  play_button = pygame.image.load("pygame/assets/button.png")
  play_button = pygame.transform.scale(play_button, (400, 150))
  play_button_rect = play_button.get_rect()
  play_button_rect.x = (screen.get_width() / 2) - (banner.get_width() / 2) + 50
  play_button_rect.y = (screen.get_height() / 2)

  # Either start the game or display the menu
  if game.has_started:
    game.update(screen)
  else:
    screen.blit(play_button, play_button_rect)
    screen.blit(banner, banner_rect)

  # update screen
  pygame.display.flip()

  for event in pygame.event.get():
    # Handle the closing
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      running = False
    # Handle de movements
    elif event.type == pygame.KEYDOWN:
      game.pressed[event.key] = True

      # See if key is pressed in order to launch projectile
      if event.key == pygame.K_SPACE:
        game.player.launch_projectile()

      if event.key == pygame.K_RETURN and game.has_started == False:
        game.start()

    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False

    # Start the game if user clicks on the play button
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if play_button_rect.collidepoint(event.pos):
        game.start()

pygame.quit()