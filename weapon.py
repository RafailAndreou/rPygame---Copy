import pygame
import math

class gun:
    def __init__(self, player, name, damage, fire_rate, bullets, color=(0, 0, 0)):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.bullets = bullets
        self.bullet_speed = 5
        self.width = 10
        self.height = 10
        self.player = player
        self.color = color
        self.bullet_list = []

    def shoot(self, target_x, target_y):
        if self.bullets > 0:
            self.bullets -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction = math.atan2(mouse_y - self.player.y, mouse_x - self.player.x)
            bullet_dx = self.bullet_speed * math.cos(direction)
            bullet_dy = self.bullet_speed * math.sin(direction)
            self.bullet_list.append([self.player.x, self.player.y, bullet_dx, bullet_dy])

    def draw_bullets(self, canvas):
        for bullet in self.bullet_list:
            pygame.draw.rect(canvas, self.color, (bullet[0], bullet[1], self.width, self.height))

    def update_bullet(self):
        for bullet in self.bullet_list:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]