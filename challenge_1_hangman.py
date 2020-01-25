import random

def hangman():
    word_list = ["cat", "dog", "hat", "sun", "blue", "red", "fox", "one", "box", "camp"]
    random_nmber = random.randint(0, 4)
    word = word_list[random_nmber]
    wrong = 0
    stages = ["",
    "_____     ",
    "|         ",
    "|    |    ",
    "|    o    ",
    "|   /|\   ",
    "|   / \   ",
    "|         "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンにようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字を予想してね：[]"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}。".format(word))

hangman()
