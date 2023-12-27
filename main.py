import pygame

FPS = 30


class Creature(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('data/creature.png').convert()
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Герой двигается!')
    group = pygame.sprite.Group()
    creature = Creature(group)
    x, y = 0, 0
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            creature.rect.y -= 10
        elif keys_pressed[pygame.K_DOWN]:
            creature.rect.y += 10
        elif keys_pressed[pygame.K_LEFT]:
            creature.rect.x -= 10
        elif keys_pressed[pygame.K_RIGHT]:
            creature.rect.x += 10
        screen.fill((255, 255, 255))
        screen.blit(creature.image, creature.rect)
        pygame.display.flip()
