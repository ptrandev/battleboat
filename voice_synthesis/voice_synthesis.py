from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import random

# Pre-made voice lines with variations
voice_lines = {
    1: [
        "Hello, welcome to Battleship!",
        "Greetings! Ready to play Battleship?",
        "Hi there! Let's start the game.",
        "Welcome aboard! Let's play Battleship.",
        "Hey! Time to battle on the high seas!"
    ],
    2: [
        "Thank you for playing.",
        "Thanks for joining us in this game.",
        "Appreciate your participation.",
        "Grateful for your company in this match.",
        "Thanks for being part of the game."
    ],
    3: [
        "Direct hit! I've sunk your ship!",
        "Bullseye! Your ship is going down.",
        "I got you! Another ship sunk.",
        "That's a hit! Your ship is sinking.",
        "Nailed it! One more ship down."
    ],
    4: [
        "Oh no, you've hit my ship!",
        "You've struck my ship!",
        "My ship's been hit!",
        "Yikes, that's a hit on my ship.",
        "Ouch, my ship has been damaged!"
    ],
    5: [
        "Missed my shot!",
        "Oops, that was a miss.",
        "I didn't hit anything that time.",
        "No contact, I missed.",
        "It seems I missed my target."
    ],
    6: [
        "Haha, you missed!",
        "Your shot missed!",
        "Nope, you didn't hit anything.",
        "Missed me!",
        "Better luck next time, you missed."
    ],
    7: [
        "I've won the game!",
        "Victory is mine!",
        "I am the winner!",
        "I've triumphed in this game!",
        "Game over, I win!"
    ],
    8: [
        "I've lost the game...",
        "Defeat is mine, well played.",
        "You've won, congratulations.",
        "I lost, but it was a good game.",
        "Defeated this time, but I'll be back!"
    ],
    9: lambda row, col: [
        f"I'm calling move at row {row}, column {col}.",
        f"Targeting row {row}, column {col}.",
        f"Engaging row {row}, column {col} with my move.",
        f"My move is at row {row}, column {col}.",
        f"Let's try row {row}, column {col}."
    ],
    10: [
        "Thank you for your question, but let's focus on the game.",
        "I appreciate your curiosity, but let's concentrate on playing.",
        "Good question, but let's keep our eyes on the game.",
        "Thanks for asking, but let's focus on winning.",
        "Interesting question, but I'd like to focus on the game."
    ]
}

def synthesize_voice(text, lang='en', tld='us'):
    tts = gTTS(text=text, lang=lang, tld=tld)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio = AudioSegment.from_file(fp, format="mp3")
    play(audio)

def display_menu():
    print("Select a voice line to play:")
    print("1. Greeting")
    print("2. Thanks")
    print("3. Hit opponent's ship")
    print("4. Ship has been hit")
    print("5. Missed shot")
    print("6. Opponent missed")
    print("7. Won the game")
    print("8. Lost the game")
    print("9. Call move (row and column)")
    print("10. Thankful but focusing on the game")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-10), or 0 to exit: "))
            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= 10:
                if choice == 9:
                    row = input("Enter row: ")
                    col = input("Enter column: ")
                    text = random.choice(voice_lines[choice](row, col))
                else:
                    text = random.choice(voice_lines[choice])

                print('\n')
                print(f"Selected Voice Line: {text}")
                print('\n')

                confirmation = input("Do you want to play this voice line? (Y/N): ").strip().lower()

                if confirmation == 'y':
                    print(f"Playing: {text}")
                    synthesize_voice(text)
                else:
                    print("Cancelled. Returning to menu.")
            else:
                print("Invalid choice. Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
