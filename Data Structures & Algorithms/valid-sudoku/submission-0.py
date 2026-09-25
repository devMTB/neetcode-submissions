class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {}
        cols = {}
        boxes = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }

        ctri = 0
        ctrj = 0

        for i in board:
            for j in board[ctri]:
                #print("this is j")
                #print(j)
                if j != '.':
                    rows.setdefault(ctri, set())

                    if j in rows[ctri]:
                        return False

                    rows[ctri].add(j)

                    cols.setdefault(ctrj, set())

                    if j in cols[ctrj]:
                        return False

                    cols[ctrj].add(j)

                    if ctri < 3:
                        if ctrj < 3:
                            if j in boxes[0]:
                                return False
                            else:
                                boxes[0].add(j)
                        if ctrj < 6 and ctrj >2:
                            if j in boxes[1]:
                                return False
                            else:
                                boxes[1].add(j)
                        if ctrj < 9 and ctrj > 5:
                            if j in boxes[2]:
                                return False
                            else:
                                boxes[2].add(j)
                    if ctri < 6 and ctri >2:
                        if ctrj < 3:
                            if j in boxes[3]:
                                return False
                            else:
                                boxes[3].add(j)
                        if ctrj < 6 and ctrj >2:
                            if j in boxes[4]:
                                return False
                            else:
                                boxes[4].add(j)
                        if ctrj < 9 and ctrj > 5:
                            if j in boxes[5]:
                                return False
                            else:
                                boxes[5].add(j)
                    if ctri < 9 and ctri > 5:
                        if ctrj < 3:
                            if j in boxes[6]:
                                return False
                            else:
                                boxes[6].add(j)
                        if ctrj < 6 and ctrj >2:
                            if j in boxes[7]:
                                return False
                            else:
                                boxes[7].add(j)
                        if ctrj < 9 and ctrj > 5:
                            if j in boxes[8]:
                                return False
                            else:
                                boxes[8].add(j)



               
                
                ctrj += 1
            ctrj = 0
            ctri += 1
        print(rows)
        print(cols)
        print(boxes)
        return True

        

