# **Turtle Crossing (Turtle Graphics)**

A Frogger‑style arcade game built using Python’s Turtle graphics module. The player controls a turtle attempting to cross a busy road while avoiding randomly generated cars. Each successful crossing increases the level and speeds up the cars, raising the difficulty.

---

## 🧩 Game Overview

The game places the player at the bottom of the screen. Cars spawn from the right and move left across the screen at varying speeds. The player moves upward using the Up arrow key. Reaching the top advances the level, resets the player’s position, and increases car speed. A collision with any car ends the game.

The project demonstrates:

- Object‑oriented design  
- Randomized obstacle generation  
- Collision detection  
- Level progression  
- Manual animation control using `screen.tracer(0)`  

---

## 📁 Project Structure

```
turtle-crossing/
│
├── main.py
├── player.py
├── car_manager.py
└── scoreboard.py
```

---

## 🐢 Player Class

The player is a Turtle object positioned at the bottom of the screen.

Key behaviors:

- Moves upward in fixed increments  
- Resets to the starting position after each successful crossing  
- Detects when it reaches the finish line  

Important constants:

- `STARTING_POSITION = (0, -280)`  
- `MOVE_DISTANCE = 10`  
- `FINISH_LINE_Y = 280`  

---

## 🚗 CarManager Class

Cars are generated at random intervals and move horizontally across the screen.

Features:

- Random color selection  
- Random vertical placement  
- Car speed increases with each level  
- Cars are stored in `all_cars` for movement and collision checks  

Important constants:

- `STARTING_MOVE_DISTANCE = 5`  
- `MOVE_INCREMENT = 10`  

Car creation uses a 1‑in‑6 chance each frame to avoid overcrowding.

---

## 🧮 Scoreboard Class

The scoreboard tracks and displays the current level.

Key behaviors:

- Starts at level 1  
- Increases level after each successful crossing  
- Clears and rewrites the level display  
- Shows “GAME OVER” at the center when the player collides with a car  

---

## 🎮 Main Game Loop

The loop controls animation, car movement, collision detection, and level progression.

### Car movement and spawning
```python
car_manager.create_car()
car_manager.move_cars()
```

### Collision detection
A collision occurs when any car is within 20 pixels of the player.

### Level advancement
When the player reaches the finish line:

- Player resets to start  
- Car speed increases  
- Scoreboard updates the level  

---

## 🖥️ Running the Game

### Requirements
- Python 3.10+
- No external libraries required

### Run
```
python main.py
```

---

## 🚀 Possible Enhancements

- Add lanes or traffic patterns  
- Add sound effects  
- Add a high‑score system  
- Add left/right movement  
- Add difficulty scaling based on time survived  

---
