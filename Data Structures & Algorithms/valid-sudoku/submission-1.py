class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_elements = defaultdict(set)
        col_elements = defaultdict(set)
        sq_elements = defaultdict(set)
        for row_ind,row in enumerate(board):
            for col_ind,col in enumerate(row):
                print(f"Row: {row_ind}, Col: {col_ind}")
                if col=='.':
                    continue
                if (col in row_elements[row_ind]) or (col in col_elements[col_ind]) or (col in sq_elements[returnSqIndex(row_ind,col_ind)]):
                    print(f"Row elements: {row_elements} \n Col elements: {col_elements} \n sq elements: {sq_elements}")
                    return False
                else:
                    row_elements[row_ind].add(col)
                    col_elements[col_ind].add(col)
                    sq_elements[returnSqIndex(row_ind,col_ind)].add(col)

        print(f"Row elements: {row_elements} \n Col elements: {col_elements} \n sq elements: {sq_elements}")
        return True

def returnSqIndex(x:int, y:int) -> int:
    a,b=0,0
    if x <= 2 and y<=2:
        return 0
    elif x <= 2 and 2<y<=5:
        return 1
    elif x <= 2 and 5<y<=8:
        return 2
    elif 2<x<=5 and y<=2:
        return 3
    elif 2<x<=5 and 2<y<=5:
        return 4
    elif 2<x<=5 and 5<y<=8:
        return 5
    elif 5<x<=8 and y<=2:
        return 6
    elif 5<x<=8 and 2<y<=5:
        return 7
    elif 5<x<=8 and 5<y<=8:
        return 8