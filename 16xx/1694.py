class Solution(object):
    def reformatNumber(self, number):
        def merge_groups(num, group_size):
            num2 = ''.join(num)
            return ['-'.join([num2[i : i + group_size] for i in range(0, len(num2), group_size)])]
        
        raw_number = []
        for i in number:
            if i.isdigit():
                raw_number.append(i)
        l = len(raw_number)
        if l % 3 == 0:
            return merge_groups(raw_number, 3)[0]
        elif (l - 2) % 3 == 0:
            res = '-'.join(merge_groups(raw_number[:-2], 3) + merge_groups(raw_number[-2:], 2))
            if res[0] == '-':
                return res[1:]
            return res
        else:
            res = '-'.join(merge_groups(raw_number[:-4], 3) + merge_groups(raw_number[-4:], 2))
            if res[0] == '-':
                return res[1:]
            return res