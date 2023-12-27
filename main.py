import pygame


class Cursor(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('data/arrow.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        pygame.mouse.set_visible(False)
        x, y = pygame.mouse.get_pos()
        screen.blit(self.image, (x, y))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Свой курсор мыши')
    group = pygame.sprite.Group()
    cursor = Cursor(group)
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_focused():
            cursor.update()
        pygame.display.flip()
