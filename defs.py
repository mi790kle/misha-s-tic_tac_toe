


def first_player_move(_table, row_choice, column_choice, moves_journal):
    print("The first player's symbol is ❌")
    while True:
        while True:
            row_choice = input("Enter the row number: ")
            if row_choice.strip() == "restart":
                return True
            if row_choice.strip() != "1" and row_choice.strip() != "2" and row_choice.strip() != "3":
                print("There is no row like that. Use 1, 2, or 3")
                continue
            else:
                break
        while True:
            column_choice = input("Enter the column number: ")
            if column_choice.strip() == "restart":
                return True
            if column_choice.strip() != "1" and column_choice.strip() != "2" and column_choice.strip() != "3":
                print("There is no column like that. Use 1, 2, or 3")
                continue
            else:
                break
        move = row_choice + column_choice
        if move in moves_journal:
            print("The tile is occupated already, try another one!")
            continue
        else:
            moves_journal.append(move)
            _table[int(row_choice) - 1][int(column_choice) - 1] =  "❌"
            break
    for row in _table:
        print("|".join(row))
        print("-" * 9)
def second_player_move(_table, row_choice, column_choice, moves_journal):
    print("The second player's symbol is ⭕")
    while True:
        while True:
            row_choice = input("Enter the row number: ")
            if row_choice.strip() == "restart":
                return True
            if row_choice.strip() != "1" and row_choice.strip() != "2" and row_choice.strip() != "3":
                print("There is no row like that. Use 1, 2, or 3")
                continue
            else:
                break
        while True:
            column_choice = input("Enter the column number: ")
            if column_choice.strip() == "restart":
                return True
            if column_choice.strip() != "1" and column_choice.strip() != "2" and column_choice.strip() != "3":
                print("There is no column like that. Use 1, 2, or 3")
                continue
            else:
                break
        move = row_choice + column_choice
        if move in moves_journal:
            print("The tile is occupated already, try another one!")
            continue
        else:
            moves_journal.append(move)
            _table[int(row_choice) - 1][int(column_choice) - 1] = "⭕"
            break
    for row in _table:
        print("|".join(row))
        print("-" * 9)
def win_check(_table, draw):
    for row in _table:
        if row == ["❌", "❌", "❌"] or row == ["⭕", "⭕", "⭕"]:
            row[0] += "🏆"
            row[1] += "🏆"
            row[2] += "🏆"
            return True
    if _table[0][0] == _table[1][1] == _table[2][2] and _table[0][0] != "⬜":
        _table[0][0] += "🏆"
        _table[1][1] += "🏆"
        _table[2][2] += "🏆"
        return True
    elif _table[0][0] == _table[1][0] == _table[2][0] and _table[0][0] != "⬜":
        _table[0][0] += "🏆"
        _table[1][0] += "🏆"
        _table[2][0] += "🏆"
        return True
    elif _table[0][1] == _table[1][1] == _table[2][1] and _table[0][1] != "⬜":
        _table[0][1] += "🏆"
        _table[1][1] += "🏆"
        _table[2][1] += "🏆"
        return True
    elif _table[0][2] == _table[1][2] == _table[2][2] and _table[0][2] != "⬜":
        _table[0][2] += "🏆"
        _table[1][2] += "🏆"
        _table[2][2] += "🏆"
        return True
    elif _table[0][2] == _table[1][1] == _table[2][0] and _table[0][2] != "⬜":
        _table[0][2] += "🏆"
        _table[1][1] += "🏆"
        _table[2][0] += "🏆"
        return True
    else:
        return False
def result_present(_table, current_player, first_player_score, second_player_score, moves_counter, draw):
    if moves_counter == 9:
        print("Looks like a draw!")
        print(f"First player score: {first_player_score}")
        print(f"Second player score: {second_player_score}")
    else:
        print("We have a WINNER!")
        for row in _table:
            print("|".join(row))
            print("-" * 9)
        if current_player == "❌":
            print("The first player wins!")
        else:
            print("The second player wins!")
        print(f"First player score: {first_player_score}")
        print(f"Second player score: {second_player_score}")
        print(f"Draws: {draw}")