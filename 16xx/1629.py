class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        pressed_delta = [releaseTimes[0]] + [releaseTimes[i] -
                    releaseTimes[i - 1] for i in range(1, len(releaseTimes))]
        max_indice = 0
        for i in range(len(pressed_delta)):
            print(keysPressed[i])
            if pressed_delta[i] > pressed_delta[max_indice]:
                max_indice = i
            elif pressed_delta[i] == pressed_delta[max_indice]:
                if keysPressed[i] > keysPressed[max_indice]:
                    max_indice = i
        return keysPressed[max_indice]