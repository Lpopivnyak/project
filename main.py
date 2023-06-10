import pygame


class Character():
    def __init__(self, x, y, w, h, filename, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, window):
        # pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])


class Enemy():
    def __init__(self, x, y, w, h, filename, speed, startX, finishX):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed = speed
        self.startX = startX
        self.finishX = finishX

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > self.startX:
            self.speed *= -1
        if self.rect.x < self.finishX:
            self.speed *= -1

    def draw(self, window):
        # pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])


class Goal():
    def __init__(self, x, y, w, h, filename):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)

    def draw(self, window):
        # pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])


class Barrier():
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)


pygame.init()
screen = pygame.display.set_mode(500, 500)
fps = pygame.time.Clock()

player = Character(230, 390, 50, 50, "pixil-frame-0.png", 0, 0)
enemy1 = Enemy(70, 270, 50, 50, "pixil-frame-0 (1).png", 3, 70, 350)
enemy2 = Enemy(350, 150, 50, 50, "pixil-frame-0 (1).png", 3, 350, 70)
crystal = Goal(230, 10, 50, 50, "pixil-frame-0 (2).png")

winText = pygame.font.Font(None, 56).render("Молодець!", True, (0, 0, 0))
loseText = pygame.font.Font(None, 56).render("Спробуй іще раз", True, (0, 0, 0))
while True:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed_y = -3
            elif event.key == pygame.K_DOWN:
                player.speed_y = 3
            elif event.key == pygame.K_LEFT:
                player.speed_x = -3
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 3
        elif event.type == pygame.KEYUP:
            player.speed_x = 0
            player.speed_y = 0

    # оновлення
    player.rect.x += player.speed_x
    player.rect.y += player.speed_y

    enemy1.update()
    enemy2.update()

    if player.rect.colliderect(enemy1.rect):
        screen.fill((255, 0, 0))
        screen.blit(loseText, [120, 200])
        pygame.display.flip()
        break

    elif player.rect.colliderect(enemy2.rect):
        screen.fill((255, 0, 0))
        screen.blit(loseText, [120, 200])
        pygame.display.flip()
        break

    elif player.rect.colliderect(crystal.rect):
        screen.fill((0, 255, 0))
        screen.blit(winText, [180, 200])
        pygame.display.flip()
        break

    # рендер
    screen.fill((255, 255, 255))
    player.draw(screen)
    enemy1.draw(screen)
    enemy2.draw(screen)
    crystal.draw(screen)

    pygame.display.flip()
    fps.tick(60)