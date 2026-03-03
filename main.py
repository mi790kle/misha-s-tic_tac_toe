import defs
from defs import first_player_move
another_round: str = ""
_table: list = [str]
row_choice: str = ""
column_choice: str = ""
moves_journal: list = [str]
move: str = ""
current_player: str = ""
first_player_score: int = 0
second_player_score: int = 0
# # 1) надо сделать главный экран
# 1.1) принт текста с декоративными полосками и кнопкой запуска игры
print("-" * 30)
print("Welcome to the great TIC TAC TOE tournament!")
print("❌ ⚔️ ⭕")
print("-" * 30)
input("To continue, press any key to continue")
# # 2)нужно сделать табличку 3х3
# 2.1) сделаю список
# # 3)ходы игроков
# 3.1) инпут требует номер строки и столба
# 3.2) проверка инпута
# 3.3) внесение в таблицу и печать

# 3.4) проверка на выигрыш
# 3.5) ход следующего игрока


# # 4)результат
# 4.1) если было найдено 3 подряд - представить таблицу с обведённой тройкой
# 4.2) спросить продолжать ли ещё
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