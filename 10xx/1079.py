class Solution(object):
    def numTilePossibilities(self, tiles):
        import itertools
        total_combinations = 0
        for length in range(1, len(tiles) + 1):
            total_combinations += len(set(itertools.permutations(tiles, length)))
        return total_combinations