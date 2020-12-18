class Solution(object):
    def strWithout3a3b(self, a, b):
        char_a, char_b = 'a', 'b'
        delta = a - b
        if delta < 0:
            a, b = b, a
            delta = -delta
            char_a, char_b = 'b', 'a'
        raw_arr = [char_a + char_b for i in range(b)] 
        print(raw_arr)
        i = 0
        while(delta):
            raw_arr[i] = char_a + raw_arr[i]
            i += 1
            delta -= 1
            if i >= len(raw_arr):
                break
        raw_arr.append(char_a * delta)
        return ''.join(raw_arr)
