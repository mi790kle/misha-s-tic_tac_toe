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

print("-" * 30)
print("Welcome to the great TIC TAC TOE tournament!")
print("❌ ⚔️ ⭕")
print("-" * 30)
input("To continue, press any key to continue")

while True:
    _table = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    for row in _table:
        print("|".join(row))
        print("-" * 9)
    while True:
        defs.first_player_move(_table, row_choice, column_choice, moves_journal)
        if defs.win_check(_table) == True:
            current_player = "❌"
            break
        defs.second_player_move(_table, row_choice, column_choice, moves_journal)
        if defs.win_check(_table) == True:
            current_player = "⭕"
            break
    defs.result_present(_table, current_player, first_player_score, second_player_score)
    another_round = input("If you wish to go for another round, press any key to continue, if not, type in -999")
    if another_round == "-999":
        break
    else:
        continue