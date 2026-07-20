# python-game-project

An arcade-style implementation of the classic **Tetris** game, developed in **Python** using the **Pygame** library. This project demonstrates the use of object-oriented programming principles, event-driven programming, collision detection, scoring systems, and graphical user interface design.

The game features a custom arcade-inspired interface, a start menu, score tracking, next-piece preview, sound effects, background music, and game-over/restart functionality.

---

## Features

- Arcade-style start screen
- Classic Tetris gameplay
- Seven unique Tetromino pieces
- Piece rotation and movement
- Collision detection
- Automatic line clearing
- Live score tracking
- Next piece preview
- Sound effects and background music
- Game over screen with restart option
- Custom arcade-themed user interface

---

## Controls

| Key | Action |
|-----|--------|
| **Space** | Start the game |
| **← Left Arrow** | Move piece left |
| **→ Right Arrow** | Move piece right |
| **↓ Down Arrow** | Move piece down faster |
| **↑ Up Arrow** | Rotate piece |
| **R** | Restart after Game Over |
| **Esc** | Return to the main menu |
| **Close Window** | Exit the game |

---

## Technologies Used

- Python 3
- Pygame
- Object-Oriented Programming (OOP)
- Git & GitHub

---

## Object-Oriented Design

The project follows an object-oriented approach by separating the game into multiple classes:

- **Game** – manages the game logic, scoring, collision detection, and gameplay.
- **Grid** – stores and manages the playing field.
- **Block** – parent class containing shared behaviour for all Tetromino pieces.
- **Tetromino Classes** – individual block types that inherit from the `Block` class.
- **Position** – stores row and column coordinates for each block.

This modular design improves readability, maintainability, and code reuse.

---

## Future Improvements

Potential future enhancements include:

- Increasing game difficulty over time
- High score saving system
- Pause menu
- Additional animations and visual effects
- Hold-piece functionality
- Improved sound settings

---

## Author

Developed by **Nick Belemet** as part of a Python programming project.
