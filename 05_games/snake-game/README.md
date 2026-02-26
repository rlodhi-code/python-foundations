# **Snake Game (Turtle Graphics)**

A classic Snake game implemented using Python’s Turtle graphics module. The project demonstrates object‑oriented design, keyboard event handling, collision detection, score tracking, and frame‑based animation using manual screen updates.

---

## 🧩 Game Overview

The game places a snake on a 600×600 black screen. The snake moves continuously, grows when it eats food, and ends the game when it collides with a wall or its own tail. A scoreboard at the top tracks the current score.

The program is organized into four classes:

- **Snake** — manages movement, growth, and direction  
- **Food** — randomly positions food on the screen  
- **Scoreboard** — displays and updates the score  
- **Main loop** — handles animation, collisions, and keyboard input  

---

## 📁 Project Structure

```
snake-game/
│
├── main.py
├── snake.py
├── food.py
└── scoreboard.py
```

---

## 🐍 Snake Class

The snake is composed of square Turtle segments stored in a list. It starts with three segments and grows by adding a new segment at the tail’s last position.

Key behaviors:

- **Movement** — each segment moves to the position of the one in front of it  
- **Direction control** — prevents reversing into itself  
- **Growth** — adds a new segment when food is eaten  

Important constants:

- `MOVE_DISTANCE = 20`  
- Head direction angles: `UP`, `DOWN`, `LEFT`, `RIGHT`

---

## 🍎 Food Class

The food is a small blue circle that appears at random positions on the screen.

Features:

- Inherits from `Turtle`  
- Uses `shapesize(0.5, 0.5)` to make it small  
- Moves instantly to a new random location when eaten  
- Stays within a safe boundary (`FOOD_LIMIT = 270`)  

---

## 🧮 Scoreboard Class

The scoreboard displays the current score at the top of the screen.

Key behaviors:

- Starts at zero  
- Increases by one when food is eaten  
- Clears and rewrites the score  
- Displays “GAME OVER” at the center when the game ends  

---

## 🎮 Main Game Loop

The loop controls animation and game logic:

- Uses `screen.tracer(0)` and `screen.update()` for smooth movement  
- Sleeps briefly (`time.sleep(0.1)`) to control speed  
- Moves the snake each frame  
- Detects collisions:

### Collision with food
```python
if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
```

### Collision with wall
The snake dies if its head crosses ±290 on either axis.

### Collision with tail
If the head touches any segment in `snake.segments[1:]`, the game ends.

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

- Add high‑score persistence  
- Add increasing speed as the snake grows  
- Add sound effects  
- Add a start screen and restart option  
- Add obstacles or levels  

---

