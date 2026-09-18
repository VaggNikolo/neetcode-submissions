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
    return (x//3)*3 + y//3