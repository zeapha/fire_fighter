# tools.py
import pygame
from assets import load_image, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_ZONE_HEIGHT, TOOLBAR_HEIGHT, BLACK, WHITE

class Tool:
    def __init__(self, tool_type, position):
        self.tool_type = tool_type
        self.position = position
        
        # Set tool properties based on type
        if tool_type == 1:
            self.image = load_image("squirt_toy")
            self.name = "Squirt Toy"
        elif tool_type == 2:
            self.image = load_image("glass")
            self.name = "Glass of Water"
        elif tool_type == 3:
            self.image = load_image("bucket")
            self.name = "Bucket of Water"
        elif tool_type == 4:
            self.image = load_image("hose")
            self.name = "Hose"
        elif tool_type == 5:
            self.image = load_image("power_washer")
            self.name = "Power Washer"
        
        # Position and size
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = position * (SCREEN_WIDTH / 5) + (SCREEN_WIDTH / 10) - self.width / 2
        self.y = GAME_ZONE_HEIGHT + (TOOLBAR_HEIGHT / 2) - self.height / 2
        
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        """Draw the tool on the screen"""
        screen.blit(self.image, (self.x, self.y))
        
        # Draw the tool name underneath
        font = pygame.font.SysFont('Arial', 15)
        text = font.render(self.name, True, BLACK)
        text_rect = text.get_rect(center=(self.x + self.width/2, self.y + self.height + 20))
        screen.blit(text, text_rect)
    
    def is_clicked(self, pos):
        """Check if the tool was clicked"""
        return self.rect.collidepoint(pos)