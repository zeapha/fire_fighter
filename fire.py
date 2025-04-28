# fire.py
import pygame
import random
from assets import GAME_ZONE_HEIGHT, SCREEN_WIDTH
from animation import FireAnimation

class Fire:
    def __init__(self):
        # Randomly select fire size
        self.size = random.randint(1, 5)
        
        # Set fire properties based on size
        if self.size == 1:
            self.name = "Tiny Fire"
        elif self.size == 2:
            self.name = "Small Fire"
        elif self.size == 3:
            self.name = "Medium Fire"
        elif self.size == 4:
            self.name = "Large Fire"
        else:
            self.name = "Huge Fire"
        
        # Position the fire randomly in the game zone
        # Base size calculation must match animation size
        base_size = 30 + (self.size * 10)
        self.width = base_size
        self.height = base_size
        
        # Make sure the fire is fully within the screen boundaries
        max_x = max(0, SCREEN_WIDTH - self.width)
        max_y = max(0, int(GAME_ZONE_HEIGHT - self.height))
        
        self.x = random.randint(0, max_x)
        self.y = random.randint(0, max_y)
        
        # Create the fire animation
        self.animation = FireAnimation(self.x, self.y, self.size)
        
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        """Draw the fire animation on the screen"""
        self.animation.draw(screen)
    
    def update(self):
        """Update the fire animation"""
        self.animation.update()
        # Don't need to update rect position since fires don't move