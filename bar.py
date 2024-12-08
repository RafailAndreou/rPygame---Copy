import pygame

class PlayerHealthBar:
    def __init__(self, player):
        self.player = player
        self.x = 20
        self.y = 20
        self.width = 100
        self.height = 20

    def draw(self, canvas):
        health_ratio = self.player.hp / self.player.max_hp
        bar_width = self.width * health_ratio
        bar = pygame.Rect(self.x, self.y, bar_width, self.height)
        pygame.draw.rect(canvas, (255, 0, 0), bar)
