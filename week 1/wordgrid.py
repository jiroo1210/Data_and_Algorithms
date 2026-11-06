class WordFinder:
    def set_grid(self, grid):
        
        self.grid_row = grid
        self.grid_column = []
        for i in range(len(grid[0])):
            self.grid_column.append("".join(grid[j][i] for j in range(len(grid))))
        # list comprehension for shorter
        self.grid_diagonal = self.diagonal() # this line added by recommendation

    def count(self, word):
        if not self.grid_row:
            return 0
        if len(word) == 1:
            return self.in_string(word,self.grid_row)
        count = 0
        # row
        count += self.in_string(word, self.grid_row)
        # grid[::-1] for reversed grid 
        count += self.in_string(word[::-1], self.grid_row)
        # column
        count += self.in_string(word, self.grid_column)
        count += self.in_string(word[::-1], self.grid_column)
        # diagonal
        count += self.in_string(word, self.grid_diagonal) # using stored diagonal attribute
        count += self.in_string(word[::-1], self.grid_diagonal) # also fix recommended by AI

        # palindrome 
        if word == word[::-1]: # can be optimized to check only once for palindrome as below ex.
            count = count//2
        return count

    def diagonal(self):
        new_grid =[]
        grid = self.grid_row
        rn = len(grid) # row number
        cn = len(grid[0]) # column number
        # / diagonal, counting from top left
        # numbers on same diagonal has equal row.no + col.no
        # main diagonal has (rn+cn)= len(grid) or len(grid[0]), whichever is shorter
        # using while & temp string added a lot of redundant '' on list
         # \ diagonal, coounting from top right has (r.n - c.n) and vice versa

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
            for row in grid:
                while len(row)>= len(word):
                    if word == row[:len(word)]:
                        count += 1
                    row = row[1:]
            return count
"""AI corrected version 
This one uses more ram for faster response time.
Storing information as attributes

class WordFinder:
    def set_grid(self, grid):
        self.grid_row = grid
        self.grid_column = ["".join(col) for col in zip(*grid)]
        self.grid_diagonal = self._build_diagonals(grid)
        
        # Combine all 4 directions once so count() is super clean
        self.all_lines = self.grid_row + self.grid_column + self.grid_diagonal

    def _build_diagonals(self, grid):
        diagonal = {}   # / direction (r + c is constant)
        anti_dia = {}   # \ direction (r - c is constant)
        
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                diagonal[r + c] = diagonal.get(r + c, "") + char
                anti_dia[r - c] = anti_dia.get(r - c, "") + char

        return list(diagonal.values()) + list(anti_dia.values())

    def count(self, word):
        if not self.grid_row:
            return 0
        if len(word) == 1:
            return sum(row.count(word) for row in self.grid_row)

        total = self.in_string(word, self.all_lines)
        
        # Only search the reverse if the word is NOT a palindrome
        if word != word[::-1]:
            total += self.in_string(word[::-1], self.all_lines)
            
        return total

    def in_string(self, word, lines):
        count = 0
        for line in lines:
            start = line.find(word)
            while start != -1:
                count += 1
                start = line.find(word, start + 1)
        return count
"""
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

    
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0 