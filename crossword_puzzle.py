board = []

#record the board and list of words
for i in range(10):
    board.append(input())
lis = input().split(";")
#find empty tiles
blank_tiles=[]
for i in range(10):
    row_lis = []
    col_lis = []
    for j in range(10):
        if board[i][j]=="-":
            row_lis.append((i,j))
        elif len(row_lis)==1:
            row_lis=[]
        elif len(row_lis)>1:
            blank_tiles.append(row_lis)
            row_lis=[]
        if j==9 and len(row_lis)>1:
            blank_tiles.append(row_lis)
            row_lis=[]
        if board[j][i]=="-":
            col_lis.append((j,i))
        elif len(col_lis)==1:
            col_lis=[]
        elif len(col_lis)>1:
            blank_tiles.append(col_lis)
            col_lis=[]
        if j==9 and len(col_lis)>1:
            blank_tiles.append(col_lis)
            col_lis=[]
#recursively put words in the blank tiles and see if they work or not
target_board = []
def find_match(board,blank_tiles,lis):
    global target_board
    # if no tiles left, copy the board to target board
    if len(blank_tiles)==0:
        target_board=board
    else:
        for tile in blank_tiles:
            for word in lis:
                if len(word)==len(tile) and all(board[tile[i][0]][tile[i][1]]=="-" or board[tile[i][0]][tile[i][1]]==word[i] for i in range(len(tile))):
                    new_board=board[:]
                    for i in range(len(tile)):
                        new_lis1 = list(new_board[tile[i][0]])
                        new_lis1[tile[i][1]]=word[i]
                        new_board[tile[i][0]] = "".join(new_lis1)
                    new_blank_tiles = blank_tiles[:]
                    new_blank_tiles.remove(tile)
                    new_lis2=lis[:]
                    new_lis2.remove(word)
                    find_match(new_board,new_blank_tiles,new_lis2)
find_match(board,blank_tiles,lis)

#print target board
for row in target_board:
    print("".join(row))

# https://www.hackerrank.com/challenges/crossword-puzzle?h_r=next-challenge&h_v=zen
# this code is highly inefficient still. I'm working on making it faster.