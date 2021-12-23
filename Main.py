import pygame

from GameClass.Game import Game

pygame.init()

pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("assets/bg.jpg")
running = True

game = Game()

while running:
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)
    print(game.pressed)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
