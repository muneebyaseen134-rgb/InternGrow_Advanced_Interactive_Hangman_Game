# Advanced Interactive Hangman Game

A professional, production-ready, text-based implementation of the classic Hangman game built using Python. This project was developed as part of the **InternGrow Python Programming Track (Task 1)**

This application goes beyond a basic terminal game by incorporating real-world software engineering practices, including live data integration via an external public REST API, dynamic difficulty scaling, robust exception handling, and an optimized command-line user interface.

## 🚀 Key Features

- **Live API Integration:** Dynamically fetches random words in real-time from an external public word API (`https://random-word-api.herokuapp.com`).
- **Dynamic Difficulty Tiers:** Features an interactive difficulty setup that maps word complexity directly to specific character lengths:
  - **Easy:** 3–4 letter words
  - **Medium:** 5–6 letter words
  - **Hard:** 7–9 letter words
- **Visual State Tracking:** Implements an interactive ASCII art renderer that visually updates the gallows structure based on the user's remaining failure attempts (6-stage threshold).
- **Input Sanitization & Validation:** Fully guards against runtime crashes by strictly validating user inputs against blank strings, numbers, multi-character entries, and duplicate guesses.
- **Seamless Game Loop:** Features an infinite replay system allowing users to instantly spin up consecutive rounds without manual script execution.

## 🛠️ Tech Stack

- **Language:** Python 
- **Libraries:** - `requests` (Standard HTTP library for external API communication)
  - `random` (Standard library for pseudo-random choices)
  - `os` (Standard utility for system-level screen clearing operations)

## 📦 Installation & Setup

Follow these simple steps to run the game locally on your machine:

1. **Clone the Repository:**
   Create a local clone of this repository. Ensure you match the official repository naming convention:
   ```bash
   git clone [https://github.com/muneebyaseen134-rgb/InternGrow_Advanced_Interactive_Hangman_Game.git]
