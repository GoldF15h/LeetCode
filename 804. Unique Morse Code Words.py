class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l = []
        for cur in words :
            tmp = ''
            for i in cur :
                tmp += morse[ord(i)-ord('a')]
            l.append(tmp)
        l = list(set(l))
        return len(l)