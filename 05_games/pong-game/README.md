# **Pong Game (Turtle Graphics)**

A simple recreation of the classic Pong arcade game built using Python’s Turtle graphics module. The project demonstrates object‑oriented design, keyboard event handling, collision detection, and frame‑by‑frame animation using `screen.tracer()`.

---

## 🎮 Overview

The game features two paddles controlled by the keyboard and a ball that moves continuously across the screen. When the ball hits the top or bottom wall, it bounces. The game loop updates the screen manually to create smooth animation.

This version includes the core mechanics of movement and bouncing, forming the foundation for a full Pong game.

---

## 📁 Project Structure

```
pong-game/
│
├── main.py
├── paddle.py
└── ball.py
```

---

## 🧱 Components

### **Paddle**
Defined in `paddle.py`, each paddle:

- Inherits from `Turtle`
- Uses a stretched square shape (`stretch_wid=5`, `stretch_len=1`)
- Moves vertically in increments of 20 pixels
- Is positioned using coordinates passed during initialization

Key methods:
- `go_up()`
- `go_down()`

---

### **Ball**
Defined in `ball.py`, the ball:

- Inherits from `Turtle`
- Moves diagonally using `x_move` and `y_move` values
- Updates its position each frame using the `move()` method
- Reverses vertical direction when hitting the top or bottom wall using `bounce()`

---

### **Main Game Loop**
`main.py` sets up:

- A black game window (`800x600`)
- Left and right paddles
- The ball
- Keyboard bindings:
  - Right paddle: **Up / Down**
  - Left paddle: **W / S**

The loop:

- Sleeps briefly to control speed
- Calls `screen.update()` to manually refresh the frame
- Moves the ball
- Detects wall collisions and triggers `ball.bounce()`

---

## 🖥️ Running the Game

### Requirements
- Python 3.10+
- No external libraries required (Turtle is included with Python)

### Run
```
python main.py
```

---

## 🧩 How It Works

### Manual animation control
The game uses:

```python
screen.tracer(0)
```

This disables automatic drawing, allowing the loop to control when the screen updates. Combined with:

```python
screen.update()
sleep(0.1)
```

This produces smooth animation.

### Collision detection
The ball checks its vertical position:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()
```

This reverses the vertical direction by multiplying `y_move` by `-1`.

---

## 🚀 Possible Enhancements

- Add paddle collision detection  
- Add scoring system  
- Add ball speed increase after each hit  
- Add sound effects  
- Add game‑over conditions  
- Add center line and scoreboard class  

---

