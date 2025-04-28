# game.py
import pygame
import random
from fire import Fire
from tools import Tool
from animation import SplashAnimation
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
        
        # List to track active splash animations
        self.splash_animations = []
            
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
                
                try:
                    # Create splash animation at the fire's location
                    splash = SplashAnimation(fire.x, fire.y, tool_type)
                    self.splash_animations.append(splash)
                except Exception as e:
                    print(f"Error creating splash animation: {e}")
        
        # Remove matching fires and add points
        for fire in fires_to_remove:
            if fire in self.fires:  # Make sure it hasn't been removed already
                self.fires.remove(fire)
                self.score += 1
        
        # Add a new fire of random size
        try:
            self.fires.append(Fire())
        except Exception as e:
            print(f"Error creating new fire: {e}")
    
    def update(self):
        """Update game state"""
        # Update fires
        for fire in self.fires:
            try:
                fire.update()
            except Exception as e:
                print(f"Error updating fire: {e}")
        
        # Update splash animations and remove finished ones
        for splash in self.splash_animations[:]:
            try:
                splash.update()
                if splash.is_finished:
                    self.splash_animations.remove(splash)
            except Exception as e:
                print(f"Error updating splash: {e}")
                # Remove problematic splash animations
                if splash in self.splash_animations:
                    self.splash_animations.remove(splash)
    
    def draw(self):
        """Draw the game"""
        try:
            # Clear the screen
            self.screen.fill(WHITE)
            
            # Draw the toolbar background
            pygame.draw.rect(self.screen, GRAY, (0, GAME_ZONE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GAME_ZONE_HEIGHT))
            
            # Draw fires
            for fire in self.fires:
                try:
                    fire.draw(self.screen)
                except Exception as e:
                    print(f"Error drawing fire: {e}")
            
            # Draw splash animations
            for splash in self.splash_animations:
                try:
                    splash.draw(self.screen)
                except Exception as e:
                    print(f"Error drawing splash: {e}")
            
            # Draw tools
            for tool in self.tools:
                tool.draw(self.screen)
            
            # Draw score
            score_text = self.font.render(f"Score: {self.score}", True, BLACK)
            self.screen.blit(score_text, (10, 10))
            
            # Update the display
            pygame.display.flip()
            
        except Exception as e:
            print(f"Error in draw method: {e}")
    
    def run(self):
        """Run the game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()