dynamic = ( [-1]* ((5 * (10**6)) + 1) )

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0

    for i in range(2,n) :
        # print(i,end='')
        if dynamic[i] == -1 :
            # print(' check stat : ',end='')
            # if is_prime(i) :
                # print(' prime ! ')
                dynamic[i] = 1
                # for j in range(i+i, 50 + 1 ,i) :
                for j in range(i+i, 5 * (10**6) + 1 ,i) :
                    # print('set {} to 0'.format(j))
                    dynamic[j] = 0
                count += 1
            # else :
            #     # print(' not prime ')
            #     dynamic[i] = 0

        elif dynamic[i] == 0 :
            # print(' dynamic : not prime ')
            continue

        elif dynamic[i] == 1 :
            # print(' dynamic : check prime')
            count += 1

    return count