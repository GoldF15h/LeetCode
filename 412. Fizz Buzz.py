class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        op = []
        for i in range(1,n+1) :
            if i%15 == 0 :
                op.append('FizzBuzz')
            elif i%5 == 0 :
                op.append('Buzz')
            elif i%3 == 0 :
                op.append('Fizz')
            else :
                op.append(str(i))
        return op