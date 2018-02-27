class SublistFinder:

    def __init__(self, sequence):
        self.sequence = sequence
        self.size = len(sequence)

    """
        Find the sublist [1,2,3] in a list
    """
    def seq_check(self):
        n = 3
        sublist = [1,2,3]

        if len(self.sequence) / 3 >= 1:
            for i in range(0, len(self.sequence), n):
                temp = self.sequence[i:i + n]
                if len(temp) == 3:
                    if temp[0] == sublist[0] and temp[1] == sublist[1] and temp[2] == sublist[2]:
                        return True
                else:
                    break
            return False
        else:
            return False


    def __repr__(self):
        return 'list: {} size: {}'.format(self.sequence, self.size)