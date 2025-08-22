import pygame

pygame.init()

class game(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      self.x = 0
      self.y = 0
      self.image = pygame.Surface([10,10])
      self.image.fill("red")

      self.rect = self.image.get_rect()
   

   def update(self):
      pass


screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("MineSwipper")

block = pygame.sprite.Group()

block.add(game())

running = True

while running:
   block.draw(screen)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      screen.fill("White")


   pygame.display.update()

