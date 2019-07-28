# player name followed by score in individual lines
fp = open('1.player_high_scores.txt', 'r')

# read all the contents of the file and split them by newlines
content = fp.read().splitlines()


iterator = 0

while iterator < len(content):
    print(f"Player Name:- {content[iterator]}")
    print(f"Player Score:- {content[iterator + 1]}")
    # Increment iterator by 2 so that we skip to the next set
    iterator += 2


fp.close()
