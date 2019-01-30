import time

def run(rows):
    tiles = "..^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.." #Additional safe tiles appended to start and end
    #tiles = "..^^.^.^^^^."
    count = tiles.count(".") - 2

    #print(tiles, tiles.count("^"))
    for _ in range(rows-1):
        nextRow = "."
        for i in range(1,len(tiles)-1):
            preTiles = tiles[i-1:i+2]
            if preTiles in ["^^.","^..","..^",".^^"]:
                nextRow += "^"
            else:
                nextRow += "."

        nextRow += "."
        tiles = nextRow
        #print(tiles, tiles.count("^"))
        count += tiles.count(".") - 2
    return count

now = time.time()
print("Part 1:", run(40))
print("Part 2:", run(400000))
print("Time taken: " + str(time.time() - now))