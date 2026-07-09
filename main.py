import requests
import random
import os

def clear_screen():
    """Clears the console screen for a cleaner user interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_random_word(difficulty: str)-> str:
    """
    Fetches a random word from a public API based on difficulty (word length).
    """
    print("Fetching a random word from the API... Please wait.")
    
    # Mapping difficulty to specific word lengths
    lengths = {
        'easy': random.choice([3, 4]),
        'medium': random.choice([5, 6]),
        # FIXED: Added the missing list of numbers [7, 8, 9] to fix the TypeError!
        'hard': random.choice([7, 8, 9]) 
    }
    
    word_length = lengths.get(difficulty, 6) # Default to medium length if invalid input
    api_url = f"https://random-word-api.herokuapp.com/word?length={word_length}"
    
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status() 
        
        # FIXED: Added [0] to correctly parse the JSON list before making it uppercase!
        return response.json()[0].upper()
            
    except requests.exceptions.RequestException:
        print("Network or API error. Using fallback word.")
        fallback_words = ["PYTHON", "DEVELOPER", "SOFTWARE", "CODING"]
        return random.choice(fallback_words)

def print_hangman(attempts_left: int) -> None:
    
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[attempts_left])

def play_hangman() -> None:
    clear_screen()
    print("Welcome to the Advanced Interactive Hangman Game!")
    
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower().strip()
    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid choice, defaulting to 'medium'.")
        difficulty = 'medium'
        
    word_to_guess = fetch_random_word(difficulty)
    guessed_letters = set()
    attempts = 6 
    
    while attempts > 0:
        clear_screen() 
        print_hangman(attempts)
        
        status = [char if char in guessed_letters else '_' for char in word_to_guess]
        print("Word: ", " ".join(status))
        print(f"Remaining failure attempts: {attempts}\n")
        
        # Win condition
        if '_' not in status:
            print(f" Congratulations! You successfully guessed the word: {word_to_guess} ")
            return
            
        guess = input("Guess a letter: ").upper().strip()
        
        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            input("Invalid input. Please enter a single alphabetical letter. (Press Enter to continue)")
            continue
            
        if guess in guessed_letters:
            input(f"You already guessed '{guess}'! Try a different one. (Press Enter to continue)")
            continue
            
        guessed_letters.add(guess)
        
        if guess not in word_to_guess:
            attempts -= 1

    # Loss condition
    clear_screen()
    print_hangman(attempts)
    print(f" Game Over! You ran out of attempts. The word was: {word_to_guess} ")

def main() -> None:
    """Main game loop to handle replays."""
    while True:
        play_hangman()
        replay = input("\nWould you like to play again? (y/n): ").lower().strip()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()