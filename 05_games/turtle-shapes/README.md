# **Turtle Shapes (Turtle Graphics)**

A collection of Turtle‑graphics drawing exercises that generate geometric shapes, polygons with varying numbers of sides, and spirograph‑style circular patterns. The scripts demonstrate color handling using RGB tuples, helper functions for random color selection, and structured drawing logic using loops and angles.

---

## 🧩 Project Overview

The folder contains two drawing programs:

- **drawshapes_param_sides.py** — draws polygons from triangle to decagon using a shared drawing function.
- **turtle_shapes_and_spirograph.py** — draws a full set of polygons and a spirograph pattern using a color palette inspired by Angela Yu’s Day 18 Turtle module exercises.

Both scripts use:

- `turtle.Screen()` for window setup  
- `colormode(255)` for RGB colors  
- A shared color palette  
- A helper function to select random colors  
- Loop‑based drawing logic  

---

## 📁 Project Structure

```
turtle-shapes/
│
├── drawshapes_param_sides.py
└── turtle_shapes_and_spirograph.py
```

---

## 🎨 drawshapes_param_sides.py

This script draws polygons with 3 to 10 sides using a single function.

### Key elements

- **Color palette** defined as RGB tuples  
- **random_color()** helper to pick a color  
- **draw_shape(num_sides)** function:
  - Calculates the turning angle as `360 / num_sides`
  - Draws each side using a loop
  - Applies a random color for each shape  

### Shapes drawn

- Triangle (3 sides)  
- Square (4)  
- Pentagon (5)  
- Hexagon (6)  
- Heptagon (7)  
- Octagon (8)  
- Nonagon (9)  
- Decagon (10)  

Each shape is drawn sequentially with a consistent size of 100 units.

---

## 🌀 turtle_shapes_and_spirograph.py

This script expands on the first by adding:

- A larger color palette  
- A function to draw polygons of any size  
- A function to draw all polygons from triangle to decagon  
- A spirograph generator  

### Key functions

- **draw_shape(num_sides, size)**  
  Draws a polygon with the given number of sides and side length.

- **draw_all_shapes()**  
  Loops from 3 to 10 sides and draws each shape.

- **draw_spirograph(radius, gap)**  
  Creates a circular spirograph pattern by:
  - Drawing a circle  
  - Rotating the turtle by `gap` degrees  
  - Repeating until a full rotation is complete  

### Layout

- Shapes are drawn on the left side of the screen  
- Spirograph is drawn on the right side  

---

## 🖥️ Running the Scripts

### Requirements
- Python 3.10+
- No external libraries required

### Run
```
python drawshapes_param_sides.py
```

or

```
python turtle_shapes_and_spirograph.py
```

A Turtle graphics window will open and display the drawings.

---

## 🚀 Possible Enhancements

- Add user input to choose number of sides or spirograph gap  
- Add animation speed controls  
- Add color‑cycling or gradient effects  
- Add random walk or pattern‑generation modes  
- Save drawings as images using `getcanvas().postscript()`  

---

