# 🧩 Day 06 - Escaping the Maze

## 📌 Project Description

This project is an **Escaping the Maze** challenge built in [Reeborg’s World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).  
The goal is to help **Reeborg** escape a dark maze where the flashlight battery has run out.  

The robot follows the **right-hand rule**:
- Turn **right** if possible
- Else, move forward if possible
- Else, turn left

This logic ensures the robot eventually reaches the goal, no matter how complex the maze is.

This is the sixth project from the **100 Days of Code: Python Bootcamp by Angela Yu**, focusing on **loops**, **conditionals**, and **logical thinking**.

---

## 🎯 What I Learned

- Using `while` loops to repeat actions until a goal is reached
- Creating helper functions like `turn_right()` from existing ones
- Applying **if / elif / else** decision making in navigation
- Using maze-specific functions:
  - `move()`
  - `turn_left()`
  - `front_is_clear()`, `right_is_clear()`
  - `at_goal()`
- Understanding and applying the **right-hand rule** for maze solving

---

## 🗺️ Maze Link

You can run the maze here:  
🌐 **[Reeborg’s World - Maze Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)**

---

## 🛠 How to Run

Since this project is built on **Reeborg’s World**, it does not run locally in Python.  
To test it:

1. Open the [Maze Challenge link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
2. Paste the **main.py** code into the editor
3. Click the **Run** button to watch Reeborg escape