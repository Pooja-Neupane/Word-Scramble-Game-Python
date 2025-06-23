import random
import time

class WordScrambleGame:
    def __init__(self, rounds=5, time_limit=30):
        """
        Initialize the Word Scramble game with a list of words,
        score counter, number of rounds, and time limit per round.
        """
        self.word_list = ["python", "developer", "coding", "terminal", "function", "keyboard", "laptop", "program"]
        self.score = 0
        self.rounds = rounds
        self.time_limit = time_limit

    def scramble_word(self, word):
        """
        Shuffle the letters of the given word to create a scrambled version.
        Ensures the scrambled word is different from the original.
        """
        word_letters = list(word)
        scrambled = word
        while scrambled == word:
            random.shuffle(word_letters)
            scrambled = ''.join(word_letters)
        return scrambled

    def play_round(self, round_number):
        """
        Play a single round: present a scrambled word, take user guess,
        validate and check correctness, update score.
        """
        original_word = random.choice(self.word_list)
        scrambled_word = self.scramble_word(original_word)
        print(f"\nRound {round_number} of {self.rounds}")
        print(f"🔀 Scrambled word: {scrambled_word}")
        start_time = time.time()

        guess = input(f"💡 Your guess (within {self.time_limit} seconds): ").lower().strip()

        # Check if time exceeded
        time_taken = time.time() - start_time
        if time_taken > self.time_limit:
            print(f"⏰ Time's up! You took {int(time_taken)} seconds.")
            print(f"❌ The correct word was '{original_word}'.")
            return

        # Validate input
        if not guess:
            print("⚠️ You didn't enter a guess.")
            print(f"❌ The correct word was '{original_word}'.")
            return

        if guess == original_word:
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct word was '{original_word}'.")

        print(f"Current Score: {self.score}/{round_number}")

    def start_game(self):
        """
        Start the Word Scramble game and play through all rounds.
        """
        print("🔤 Welcome to the OOP Word Scramble Game!")
        print(f"You have {self.time_limit} seconds to guess each word.")
        self.score = 0  # Reset score before starting

        for round_number in range(1, self.rounds + 1):
            self.play_round(round_number)

        print(f"\n🏁 Game Over! Your final score is: {self.score}/{self.rounds}")

    def play_again(self):
        """
        Ask the user if they want to play again.
        """
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower().strip()
            if choice in ('y', 'yes'):
                self.start_game()
            elif choice in ('n', 'no'):
                print("Thank you for playing! Keep sharpening your skills!")
                break
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    game = WordScrambleGame()
    game.start_game()
    game.play_again()
