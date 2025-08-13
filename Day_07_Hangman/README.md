# 🔤 Day 07 – Hangman

## 📌 Project Description

This project is a **Python implementation of the Hangman game**, enhanced with multiple features and modular code using separate files for artwork and word lists.

The player guesses letters to uncover a hidden word. Wrong guesses reduce lives and advance the hangman stage; correct guesses reveal letters. The game also prevents penalties for repeat guesses and shows remaining lives each turn.

This is the **seventh** project from the **100 Days of Code: Python Bootcamp by Angela Yu**, focusing on **loops**, **conditionals**, and **logical thinking**.

**Features included:**
- Random word selection from `hangman_words.py`
- ASCII art stages and logo from `hangman_art.py`
- Tracks guessed letters and prevents penalties for repeated guesses
- Displays lives remaining each round
- Reveals the correct answer upon losing

---

## 🗺️ Game Flowchart

The game's logic follows this flowchart:

![Hangman Flowchart](Amended Hangman Flowchart.png)

---

## 🎯 What I Learned

- Importing lists and variables from separate Python files
- Using lists to store game states and track progress
- Implementing **`if/elif/else`** conditions for different scenarios
- Detecting repeated inputs and avoiding unnecessary penalties
- String concatenation and list-to-string conversion for display
- Using ASCII art for game visuals
- Applying loops (`while`) for continuous gameplay

---

## 🛠 How to Run

Make sure you have Python installed. Then run the script in your terminal:

```bash
python main.py