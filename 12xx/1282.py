class Solution(object):
    def groupThePeople(self, groupSizes):
        processed_arr = [[groupSizes[member], member] for member in range(len(groupSizes))]
        processed_arr.sort(key=lambda x: x[0])
        groups = []
        current_group = []
        for member in processed_arr:
            if len(current_group) == 0:
                current_group = [member]
            else:
                current_group.append(member)
            if len(current_group) == current_group[-1][0]:
                groups.append(current_group)
                current_group = []
        return [[member[1] for member in j] for j in groups]
        