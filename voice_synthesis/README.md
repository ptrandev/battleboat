# Voice Synthesis

This is the voice synthesis engine for the robot.

## Run

Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the voice synthesis engine:

```bash
python3 voice_synthesis.py
```

## Usage

Here is example output:

```bash
Select a voice line to play:
1. Greeting
2. Thanks
3. Hit opponent's ship
4. Ship has been hit
5. Missed shot
6. Opponent missed
7. Won the game
8. Lost the game
9. Call move (row and column)
10. Thankful but focusing on the game
Enter your choice (1-10), or 0 to exit: 1

Selected Voice Line: Welcome aboard! Let's play Battleship.

Do you want to play this voice line? (Y/N): y
Playing: Welcome aboard! Let's play Battleship.

Select a voice line to play:
1. Greeting
2. Thanks
3. Hit opponent's ship
4. Ship has been hit
5. Missed shot
6. Opponent missed
7. Won the game
8. Lost the game
9. Call move (row and column)
10. Thankful but focusing on the game
Enter your choice (1-10), or 0 to exit: 9
Enter row: 3
Enter column: 5

Selected Voice Line: Targeting row 3, column 5.

Do you want to play this voice line? (Y/N): n
Cancelled. Returning to menu.

Select a voice line to play:
1. Greeting
2. Thanks
3. Hit opponent's ship
4. Ship has been hit
5. Missed shot
6. Opponent missed
7. Won the game
8. Lost the game
9. Call move (row and column)
10. Thankful but focusing on the game
Enter your choice (1-10), or 0 to exit: 7

Selected Voice Line: I am the winner!

Do you want to play this voice line? (Y/N): y
Playing: I am the winner!

Select a voice line to play:
1. Greeting
2. Thanks
3. Hit opponent's ship
4. Ship has been hit
5. Missed shot
6. Opponent missed
7. Won the game
8. Lost the game
9. Call move (row and column)
10. Thankful but focusing on the game
Enter your choice (1-10), or 0 to exit: 0
Exiting...
```