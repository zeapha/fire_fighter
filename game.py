# game.py
import pygame
import random
from fire import Fire
from tools import Tool
from assets import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_ZONE_HEIGHT, WHITE, GRAY, BLACK

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Set up the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fire Fighter")
        
        # Create clock for controlling game speed
        self.clock = pygame.time.Clock()
        
        # Game state
        self.running = True
        self.score = 0
        
        # Create fires (start with 5)
        self.fires = []
        for _ in range(5):
            self.fires.append(Fire())
        
        # Create tools
        self.tools = []
        for i in range(5):
            self.tools.append(Tool(i + 1, i))
            
        # Create font for score display
        self.font = pygame.font.SysFont('Arial', 24)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a tool was clicked
                for tool in self.tools:
                    if tool.is_clicked(event.pos):
                        self.use_tool(tool.tool_type)
    
    def use_tool(self, tool_type):
        """Use the selected tool"""
        # Check if any fires match the tool size
        fires_to_remove = []
        
        for fire in self.fires:
            if fire.size == tool_type:
                fires_to_remove.append(fire)
        
        # Remove matching fires and add points
        for fire in fires_to_remove:
            self.fires.remove(fire)
            self.score += 1
        
        # Add a new fire of random size
        self.fires.append(Fire())
    
    def update(self):
        """Update game state"""
        for fire in self.fires:
            fire.update()
    
    def draw(self):
        """Draw the game"""
        # Clear the screen
        self.screen.fill(WHITE)
        
        # Draw the toolbar background
        pygame.draw.rect(self.screen, GRAY, (0, GAME_ZONE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GAME_ZONE_HEIGHT))
        
        # Draw fires
        for fire in self.fires:
            fire.draw(self.screen)
        
        # Draw tools
        for tool in self.tools:
            tool.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        # Update the display
        pygame.display.flip()
    
    def run(self):
        """Run the game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()