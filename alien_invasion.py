import sys, pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (255,0,0)
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((255,0,0))
            # Make the most recently drawn screen visible.
            # This will create the illusion of movement by constantly redrawing the screen
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

