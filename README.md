# Asteroids

Asteroids is a classic arcade-style game where the player controls a spaceship and must destroy asteroids while avoiding collisions. This project is implemented using Python and Pygame.

## Features

- Player spaceship that can rotate, move, and shoot
- Asteroids that split into smaller pieces when destroyed
- Collision detection between the player, asteroids, and bullets
- Simple game loop with update and draw methods

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Mashon8945/asteroids.git
   cd asteroids
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the game:
    ```sh
   python main.py
   ```

## Controls

 - W: Move forward
 - S: Move backward
 - A: Rotate left
 - D: Rotate right
 - Space: Shoot

## Code Structure

 - main.py: The main game loop and initialization code
 - player.py: The Player class, which handles the spaceship's behavior
 - asteroid.py: The Asteroid class, which handles the asteroids' behavior
 - shot.py: The Shot class, which handles the bullets' behavior
 - circleshape.py: The CircleShape class, a base class for circular objects
 - constants.py: Constants used throughout the game

## Contributing

 - Contributions are welcome! Please feel free to submit a Pull Request.

## License

 - This project is licensed under the MIT License.