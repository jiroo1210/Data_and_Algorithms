class WordFinder:
    def set_grid(self, grid):
        
        self.grid_row = grid
        self.grid_column = []
        for i in range(len(grid[0])):
            self.grid_column.append("".join(grid[j][i] for j in range(len(grid))))
        # list comprehension for shorter

    def count(self, word):
        if not self.grid_row:
            return 0
        if len(word) == 1:
            return round(self.in_string(word,self.grid_row))
        count = 0
        # row
        count += self.in_string(word, self.grid_row)
        # grid[::-1] did not work
        # try word[:-1]?
        count += self.in_string(word[::-1], self.grid_row)
        # column
        count += self.in_string(word, self.grid_column)
        count += self.in_string(word[::-1], self.grid_column)
        # diagonal
        count += self.in_string(word, self.diagonal())
        count += self.in_string(word[::-1], self.diagonal())

        # palindrome
        if word == word[::-1]:
            count = count//2
        return count

    def diagonal(self):
        new_grid =[]
        grid = self.grid_row
        rn = len(grid)
        cn = len(grid[0])
        # / direction, counting from top left
        # numbers on same diagonal has equal row.no + col.no
        # main diagonal has (r.n+c.m)= len(grid) or len(grid[0]), whichever is shorter
        # using while & temp string added a lot of redundant '' on list
         # \ direction, coounting from top right has (r.n - c.n) and vice versa

        diagonal ={}
        anti_dia = {}
        for r in range(rn):
            for c in range(cn):
                # use .get() for first term
                diagonal[r + c] = diagonal.get(r + c,"") + grid[r][c]
                anti_dia[r - c] = anti_dia.get(r - c, "") + grid[r][c]

        new_grid.extend(diagonal.values())        
        new_grid.extend(anti_dia.values())
            
        return new_grid

    def in_string(self, word, grid):
            count = 0
            wl = len(word)
            for row in grid:
                while len(row)>= len(word):
                    if word == row[:len(word)]:
                        count += 1
                    row = row[1:]
            return count

if __name__ == "__main__":
    grid = ["AAA",
            "AAA",
            "AAA",
            "AAA"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("A"))
    print(finder.count("AAAA"))
    print(finder.count("AAAA"))
    print(finder.count("A"))
    print(finder.count("AA"))