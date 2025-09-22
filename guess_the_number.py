#!/usr/bin/env python3
"""
Guess the Number Game
A simple Python game where the player tries to guess a randomly generated number.
"""

import random
import sys

class GuessTheNumberGame:
    def __init__(self):
        self.score = 0
        self.games_played = 0
        
    def display_welcome(self):
        """Display welcome message and game instructions."""
        print("=" * 50)
        print("🎯 WELCOME TO GUESS THE NUMBER GAME! 🎯")
        print("=" * 50)
        print("I'm thinking of a number between 1 and 100.")
        print("Try to guess it in as few attempts as possible!")
        print("I'll give you hints: 'Too high!' or 'Too low!'")
        print("-" * 50)
    
    def get_difficulty(self):
        """Get difficulty level from user."""
        while True:
            print("\nChoose difficulty level:")
            print("1. Easy (1-50, 10 attempts)")
            print("2. Medium (1-100, 7 attempts)")
            print("3. Hard (1-200, 5 attempts)")
            
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice == 1:
                    return 50, 10
                elif choice == 2:
                    return 100, 7
                elif choice == 3:
                    return 200, 5
                else:
                    print("❌ Please enter 1, 2, or 3!")
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def play_game(self):
        """Main game logic."""
        max_number, max_attempts = self.get_difficulty()
        secret_number = random.randint(1, max_number)
        attempts = 0
        
        print(f"\n🎮 Game started! Guess a number between 1 and {max_number}")
        print(f"You have {max_attempts} attempts to guess the number.")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
                attempts += 1
                
                if guess == secret_number:
                    print(f"\n🎉 CONGRATULATIONS! You guessed it right!")
                    print(f"The number was {secret_number}")
                    print(f"You took {attempts} attempt{'s' if attempts > 1 else ''} to guess it!")
                    
                    # Calculate score based on attempts and difficulty
                    if max_number == 50:
                        points = max(1, 10 - attempts + 1)
                    elif max_number == 100:
                        points = max(1, 7 - attempts + 1)
                    else:  # max_number == 200
                        points = max(1, 5 - attempts + 1)
                    
                    self.score += points
                    print(f"🏆 You earned {points} points! Total score: {self.score}")
                    return True
                    
                elif guess < secret_number:
                    print("📈 Too low! Try a higher number.")
                else:
                    print("📉 Too high! Try a lower number.")
                
                if attempts < max_attempts:
                    remaining = max_attempts - attempts
                    print(f"💡 {remaining} attempt{'s' if remaining > 1 else ''} remaining.")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
                attempts -= 1  # Don't count invalid input as an attempt
        
        print(f"\n😞 Game Over! You've used all {max_attempts} attempts.")
        print(f"The secret number was {secret_number}")
        return False
    
    def display_stats(self):
        """Display game statistics."""
        if self.games_played > 0:
            print(f"\n📊 GAME STATISTICS:")
            print(f"Games played: {self.games_played}")
            print(f"Total score: {self.score}")
            if self.games_played > 0:
                avg_score = self.score / self.games_played
                print(f"Average score: {avg_score:.1f}")
    
    def play_again(self):
        """Ask if player wants to play again."""
        while True:
            choice = input("\n🔄 Would you like to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("❌ Please enter 'y' for yes or 'n' for no!")
    
    def run(self):
        """Main game loop."""
        self.display_welcome()
        
        while True:
            self.games_played += 1
            won = self.play_game()
            
            if not won:
                self.games_played -= 1  # Don't count lost games in statistics
            
            self.display_stats()
            
            if not self.play_again():
                break
        
        print("\n👋 Thanks for playing Guess the Number Game!")
        print("🎯 Hope you had fun!")
        sys.exit(0)

def main():
    """Entry point of the program."""
    try:
        game = GuessTheNumberGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
