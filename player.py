import pygame

class Player:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 10
        self.gravity = 1
        self.jump_strength = 15
        self.is_jumping = False
        self.y_velocity = 0
        self.hp = 100
        self.jump_cooldown = 0
        self.max_hp = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_right(self):
        self.x += self.vel
        self.rect.x = self.x

    def move_left(self):
        self.x -= self.vel
        self.rect.x = self.x

    def jump(self):
        if self.is_jumping < 2 and self.jump_cooldown == 0:
            self.is_jumping += 1
            self.y_velocity = -self.jump_strength
            self.jump_cooldown = 15

    def apply_gravity(self):
        self.y_velocity += self.gravity
        self.y += self.y_velocity
        self.rect.y = self.y
        if self.y >= 450:
            self.y = 450
            self.y_velocity = 0
            self.is_jumping = 0
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0, 0, 0), self.rect)