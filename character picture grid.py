#! Python

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
          #x1,  x2 , x3,  x4,  x5,  x6
#print(grid[0][0],
#     grid[1][0],
#      grid[2][0],
#      grid[3][0],
#      grid[4][0],
#      grid[5][0],
#      grid[6][0],
#      grid[7][0],
#      grid[8][0],
#       end = "")


for i in range(len(grid[0])):
    print()
    for j in range(len(grid)):
        print(grid[j][i], end = "")

print()
