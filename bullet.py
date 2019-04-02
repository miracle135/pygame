import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, positon):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = positon
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False
    
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, positon):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = positon
        self.speed = 14
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False
    
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
        
class Bullet3(pygame.sprite.Sprite):
    def __init__(self, positon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.image=pygame.transform.scale2x(self.image)
        self.image=pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = positon
        self.speed = 6
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top += self.speed

        if self.rect.top > 700:#屏幕height
            self.active = False
    
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
