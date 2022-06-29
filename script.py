import os

# System call
os.system("")

# Class of different styles
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

def init_table(n):
    table = []
    counter = 0
    for i in range(n):
        row = []
        for j in range(n):
            counter += 1
            row.append(str(counter))
        table.append(row)
    return table

def get_player(table, player):
    n = len(table)
    while True:
        try:
            answer = int(input("Where do we put " + player + "? "))
        except:
            print("Incorrect input. Are you sure you entered a number?")
            continue

        if answer >= 1 and answer <= n**2:
            row = (answer-1) // n
            column = (answer-1) % n
            if (str(table[row][column]) not in "X0"):
                table[row][column] = player
                break
            else:
                print("This cell is already taken")
        else:
            print(f'Invalid input. Enter a number from 1 to {n**2}.')


def draw_table(table):
    for row in table:
        for column in row:
            if(column == 'X'):
                print(style.RED + column, end=" ")
            elif (column == '0'):
                print(style.GREEN + column, end=" ")
            else:
                print(style.RESET + column, end=" ")
        print()

def check_winner(table, player):

    n = len(table)

    winner = player*n

    has_winner = False

    left_diagonal = ''
    right_diagonal = ''

    for i in range(n):
        if not has_winner:
            # checking rows
            has_winner = ''.join(table[i]) == winner

            if not has_winner:
                left_diagonal += table[i][i]
                right_diagonal += table[i][n - 1 - i]
                column = ''
                for j in range(n):
                    column += table[j][i]

                # checking columns
                has_winner = column == winner

    if not has_winner:
        # checking left diagonal
        has_winner = left_diagonal == winner

    if not has_winner:
        # checking right diagonal
        has_winner = right_diagonal == winner

    return has_winner

def main():
    step = 0
    table = init_table(3)
    has_winner = False
    while not has_winner:
        draw_table(table)
        if step % 2 == 0:
            player = 'X'
        else:
            player = '0'

        step += 1

        get_player(table, player)

        has_winner = check_winner(table, player)

        if has_winner:
            print(player, "wins!")
            draw_table(table)
            break
main()
