import pygame

pygame.init()

class Game(pygame.sprite.Sprite):
   def __init__(self, mine, x, y):
      if mine == True:
         pygame.sprite.Sprite.__init__(self)
         
         self.image = pygame.Surface([25,25])
         self.image.fill("red")
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         
      if mine == False:
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.Surface([25,25])
         self.image.fill("White")   
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         

      
def CreateGrid():
   sprite_group.add(Game(False,10,10))
   sprite_group.add(Game(True,50,10))

   
     
   

   


screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("MineSwipper")

sprite_group = pygame.sprite.Group()

CreateGrid()

running = True
screen.fill("Grey") 

while running:
   sprite_group.draw(screen)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      


   pygame.display.update()

