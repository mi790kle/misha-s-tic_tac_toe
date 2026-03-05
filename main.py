import defs
another_round: str = ""
_table: list = [str]
row_choice: str = ""
column_choice: str = ""
moves_journal: list = [str]
move: str = ""
current_player: str = ""
first_player_score: int = 0
second_player_score: int = 0
moves_counter: int = 0
reset: bool = False
draw: int = 0
print("-" * 30)
print("Welcome to the great TIC TAC TOE tournament!")
print("❌ ⚔️ ⭕")
print("-" * 30)
print("If you wish to restart the game type in restart, but your scores will be set to 0")
print("-" * 30)
input("To continue, press any key to continue")

while True:
    moves_counter = 0
    moves_journal.clear()
    _table = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    for row in _table:
        print("|".join(row))
        print("-" * 9)
    while True:
        reset = defs.first_player_move(_table, row_choice, column_choice, moves_journal)
        if reset == True:
            break
        if defs.win_check(_table, draw) == True:
            current_player = "❌"
            first_player_score += 1
            break
        moves_counter += 1
        if moves_counter == 9:
            draw += 1
            break
        reset = defs.second_player_move(_table, row_choice, column_choice, moves_journal)
        if reset == True:
            break
        if defs.win_check(_table, draw) == True:
            current_player = "⭕"
            second_player_score += 1
            break
        moves_counter += 1
    if reset == True:
        first_player_score = 0
        second_player_score = 0
        continue
    defs.result_present(_table, current_player, first_player_score, second_player_score, moves_counter, draw)
    another_round = input("If you wish to go for another round, press any key to continue, if not, type in -999")
    if another_round == "-999":
        break
    else:
        continue