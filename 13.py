def load_messages():
    with open("words.txt", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def draw_board(board):
    print("\nТекущее поле:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]):  
            return True
        if all(board[j][i] == symbol for j in range(3)):  
            return True
    if all(board[i][i] == symbol for i in range(3)): 
        return True
    if all(board[i][2 - i] == symbol for i in range(3)): 
        return True
    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player_symbol, board, error_message):
    while True:
        try:
            coords = input(f"Игрок {player_symbol}, введите координаты (ряд и столбец от 1 до 3): ")
            row, col = map(int, coords.strip().split())
            row -= 1
            col -= 1

            if row not in range(3) or col not in range(3):
                print(error_message)
                continue
            if board[row][col] != " ":
                print("❌ Клетка занята. Попробуйте снова.")
                continue
            return row, col
        except ValueError:
            print(error_message)


def main():
    try:
        messages = load_messages()
    except FileNotFoundError:
        print("Файл words.txt не найден. Пожалуйста, добавьте его в ту же папку.")
        return

    print(messages[0]) 
    print(messages[1]) 

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_symbol = "X"
    draw_board(board)

    while True:
        row, col = get_move(current_symbol, board, messages[4])
        board[row][col] = current_symbol
        draw_board(board)

        if check_winner(board, current_symbol):
            print(f"{messages[2]} Игрок {current_symbol} выиграл!")
            break
        if is_draw(board):
            print(messages[3])
            break

        current_symbol = "O" if current_symbol == "X" else "X"


if __name__ == "__main__":
    main()
