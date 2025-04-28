# animation.py
import pygame
import random

class Animation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frames = []
        self.current_frame = 0
        self.is_finished = False
        self.frame_delay = 5  # Update every 5 game ticks
        self.frame_counter = 0
        self.loop = False  # By default, animations don't loop
    
    def update(self):
        """Update the animation"""
        self.frame_counter += 1
        
        # Change frame every frame_delay ticks
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.current_frame += 1
            
            # Check if animation is finished
            if self.current_frame >= len(self.frames):
                if self.loop:
                    # If looping, go back to the first frame
                    self.current_frame = 0
                else:
                    # If not looping, stay on last frame and mark as finished
                    self.is_finished = True
                    self.current_frame = len(self.frames) - 1  # Stay on last frame
    
    def draw(self, screen):
        """Draw the current frame"""
        if not self.is_finished and self.frames:
            screen.blit(self.frames[self.current_frame], (self.x, self.y))

class FireAnimation(Animation):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size
        self.frame_delay = 8
        self.loop = True  # Fire animations should loop continuously
        
        # Create fire frames
        self.create_fire_frames()
    
    def create_fire_frames(self):
        """Create frames for fire animation"""
        base_size = 30 + (self.size * 10)  # Size increases with fire size
        
        # Create 4 slightly different frames for fire animation
        for i in range(4):
            surface = pygame.Surface((base_size, base_size), pygame.SRCALPHA)
            
            # Use pre-defined flicker values instead of random for stability
            flicker_values = [(-2, -3), (1, 2), (-1, 1), (2, -2)]
            flicker, top_flicker = flicker_values[i]
            
            # Draw the base of the fire (yellow/orange)
            pygame.draw.ellipse(surface, (255, 165, 0), (0, base_size//3, base_size, base_size//1.5))
            
            # Draw the middle of the fire (orange/red)
            pygame.draw.ellipse(surface, (255, 100, 0), 
                               (base_size//6, base_size//4 + flicker, base_size - base_size//3, base_size//1.8))
            
            # Draw the top of the fire (red)
            pygame.draw.ellipse(surface, (255, 0, 0), 
                               (base_size//4, base_size//8 + top_flicker, base_size//2, base_size//2))
            
            self.frames.append(surface)

class SplashAnimation(Animation):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size
        self.frame_delay = 3  # Faster animation
        
        # Create splash frames
        self.create_splash_frames()
    
    def create_splash_frames(self):
        """Create frames for splash animation"""
        base_size = 40 + (self.size * 10)  # Size based on tool size
        
        # Create 6 frames for splash animation
        for i in range(6):
            surface = pygame.Surface((base_size, base_size), pygame.SRCALPHA)
            
            # Draw expanding splash
            splash_size = (i + 1) * (base_size / 6)
            splash_alpha = 255 - (i * 40)  # Fade out as animation progresses
            
            # Create water color with alpha
            water_color = (0, 100, 255, int(splash_alpha))
            
            # Use pre-defined positions instead of random for stability
            # Create a simple expanding circle pattern
            center_x, center_y = base_size/2, base_size/2
            
            # Draw a main water splash circle
            pygame.draw.circle(surface, water_color, (int(center_x), int(center_y)), int(splash_size/2))
            
            # Draw a few droplets around it (fixed positions)
            droplet_positions = [
                (0.7, 0.7), (0.7, -0.7), (-0.7, 0.7), (-0.7, -0.7),
                (1, 0), (0, 1), (-1, 0), (0, -1)
            ]
            
            for pos_x, pos_y in droplet_positions:
                # Calculate droplet position
                drop_x = center_x + (pos_x * splash_size/2)
                drop_y = center_y + (pos_y * splash_size/2)
                
                # Draw droplet (smaller than main splash)
                droplet_size = max(3, int(base_size / 10 * (1 - i/6)))  # Size decreases over time
                pygame.draw.circle(surface, water_color, 
                                  (int(drop_x), int(drop_y)), droplet_size)
            
            self.frames.append(surface)