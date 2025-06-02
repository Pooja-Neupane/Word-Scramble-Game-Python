import random

class WordScrambleGame:
    def __init__(self):
        self.word_list = ["python", "developer", "coding", "terminal", "function", "keyboard", "laptop", "program"]
        self.score = 0
        self.rounds = 5

    def scramble_word(self, word):
        word_letters = list(word)
        random.shuffle(word_letters)
        return ''.join(word_letters)

    def play_round(self):
        original_word = random.choice(self.word_list)
        scrambled_word = self.scramble_word(original_word)
        print(f"\n🔀 Scrambled word: {scrambled_word}")
        guess = input("💡 Your guess: ").lower()

        if guess == original_word:
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct word was '{original_word}'.")

    def start_game(self):
        print("🔤 Welcome to the OOP Word Scramble Game!\n")
        for _ in range(self.rounds):
            self.play_round()
        print(f"\n🏁 Game Over! Your final score is: {self.score}/{self.rounds}")

# Start the game
if __name__ == "__main__":
    game = WordScrambleGame()
    game.start_game()
