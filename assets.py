# assets.py
import pygame
import os

# Colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_ZONE_HEIGHT = SCREEN_HEIGHT * 0.8  # Top 80% for fires
TOOLBAR_HEIGHT = SCREEN_HEIGHT * 0.2     # Bottom 20% for toolbar

def load_image(name, scale=1.0):
    """Load an image and return the image object"""
    # Create a simple shape for now (we'll replace with images later)
    if name == "squirt_toy":
        surface = pygame.Surface((30, 30))
        surface.fill(BLUE)
    elif name == "glass":
        surface = pygame.Surface((40, 40))
        surface.fill(BLUE)
    elif name == "bucket":
        surface = pygame.Surface((50, 50))
        surface.fill(BLUE)
    elif name == "hose":
        surface = pygame.Surface((60, 60))
        surface.fill(BLUE)
    elif name == "power_washer":
        surface = pygame.Surface((70, 70))
        surface.fill(BLUE)
    else:
        # Default empty surface
        surface = pygame.Surface((50, 50))
        surface.fill(WHITE)
    
    if scale != 1.0:
        new_width = int(surface.get_width() * scale)
        new_height = int(surface.get_height() * scale)
        surface = pygame.transform.scale(surface, (new_width, new_height))
    
    return surface