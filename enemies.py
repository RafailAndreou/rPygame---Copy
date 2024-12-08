import pygame

class Enemy:
    def __init__(self, name, hp, damage, height, width):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.height = height
        self.width = width
        self.x = 500
        self.y = 500
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0, 0, 255), self.rect)
        
    def attack(self, player):
        player.hp -= self.damage
    
    def move_to_player(self, player):
        if self.x > player.x:
            self.x -= 5
        else:
            self.x += 5
        self.rect.x = self.x
        
    def collision(self, player):
        if self.rect.colliderect(player.rect):
            self.attack(player)