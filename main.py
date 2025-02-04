import pygame
import tkinter as tk
from tkinter import ttk
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

class GameOverDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Game Over")
        self.geometry("300x150")
        self.resizable(False, False)

        label = tk.Label(self, text="Game Over! What would you like to do?", font=("Arial", 12))
        label.pack(pady=20)

        self.result = None

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        restart_button = ttk.Button(button_frame, text="Restart", command=self.on_restart)
        restart_button.pack(side=tk.LEFT, padx=10)

        continue_button = ttk.Button(button_frame, text="Continue", command=self.on_continue)
        continue_button.pack(side=tk.LEFT, padx=10)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.on_exit)
        exit_button.pack(side=tk.LEFT, padx=10)

    def on_restart(self):
        self.result = 'restart'
        self.destroy()

    def on_continue(self):
        self.result = 'continue'
        self.destroy()

    def on_exit(self):
        self.result = 'exit'
        self.destroy()

def show_game_over_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    dialog = GameOverDialog(root)
    root.wait_window(dialog)

    return dialog.result

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # New group for shots

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)  # Add Shot to the groups

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  # Create a new AsteroidField object

    while True:
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                result = show_game_over_dialog()
                if result == 'restart':
                    main()  # Restart the game
                elif result == 'exit':
                    return  # Exit the game
                elif result == 'continue':
                    break  # Continue the game

            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        dt = clock.tick(30) / 1000

if __name__ == "__main__":
    main()
