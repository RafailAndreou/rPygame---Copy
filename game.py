import pygame
from player import Player
from bar import PlayerHealthBar
from enemies import Enemy
from weapon import gun

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class Game:
    def __init__(self):
        self.canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My First Game")
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("assets/bgtest.png")
        self.bg_x = 0
        self.player = Player(100, 450, 100, 50)
        self.healthbar = PlayerHealthBar(self.player)
        self.exit = False
        self.goblin = Enemy("Goblin", 100, 1, 50, 50)
        self.pistol = gun(self.player, "Pistol", 10, 1, 100000)
        
    def run(self):
        while not self.exit:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def update(self):
        self.handle_keys()
        self.update_background()
        self.player.apply_gravity()
        self.goblin.collision(self.player)
        self.pistol.update_bullet()
        # self.pistol.collision(self.goblin)
        
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_right()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player.jump()
        
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.pistol.shoot(mouse_x, mouse_y)

    def update_background(self):
        if self.player.x > 600:
            self.bg_x -= self.player.vel
            self.player.x = 600
            self.goblin.x -= self.player.vel
        if self.player.x < 200:
            self.bg_x += self.player.vel
            self.player.x = 200
            self.goblin.x += self.player.vel

    def draw(self):
        self.canvas.fill((255, 255, 255))
        self.canvas.blit(self.bg, (self.bg_x, 0))
        self.player.draw(self.canvas)
        self.goblin.draw(self.canvas)
        self.goblin.move_to_player(self.player)
        self.healthbar.draw(self.canvas)
        self.pistol.draw_bullets(self.canvas)
        pygame.display.update()