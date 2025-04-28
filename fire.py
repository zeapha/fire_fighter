# fire.py
import pygame
import random
from assets import load_image, GAME_ZONE_HEIGHT, SCREEN_WIDTH

class Fire:
    def __init__(self):
        # Randomly select fire size
        self.size = random.randint(1, 5)
        
        # Set fire properties based on size
        if self.size == 1:
            self.image = load_image("fire_tiny")
            self.name = "Tiny Fire"
        elif self.size == 2:
            self.image = load_image("fire_small")
            self.name = "Small Fire"
        elif self.size == 3:
            self.image = load_image("fire_medium")
            self.name = "Medium Fire"
        elif self.size == 4:
            self.image = load_image("fire_large")
            self.name = "Large Fire"
        else:
            self.image = load_image("fire_huge")
            self.name = "Huge Fire"
        
        # Position the fire randomly in the game zone
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(0, int(GAME_ZONE_HEIGHT - self.height))
        
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        """Draw the fire on the screen"""
        screen.blit(self.image, (self.x, self.y))
    
    def update(self):
        """Update the fire position and rect"""
        self.rect.x = self.x
        self.rect.y = self.y