import pygame, sys, random

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

the_sound = pygame.mixer.Sound("assets/bang.wav")

screen = pygame.display.set_mode((500, 500))


levelMusic = pygame.mixer.Sound("assets/loop.wav")

# levelMusic.play(-1)

while True:
    screen.fill((random.randint(100,150), 0, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        levelMusic.play()
    else:
        pygame.mixer.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
