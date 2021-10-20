class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        ans = 4
        for i in range(1971,year+1) :
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) :
                ans += 2
            else :
                ans += 1
            ans %= 7
        
        # print('first day of the year',dayOfWeek[ans])
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
            
            mSet = [31,29,31,30,31,30,31,31,30,31,30,31]
        else :
            mSet = [31,28,31,30,31,30,31,31,30,31,30,31]
            
        for i in range(month-1) :
            ans += mSet[i]
            ans %= 7
        # print('first day of the mounth',dayOfWeek[ans])
        
        ans += day - 1
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
            ans -= 1
        ans %= 7
        
        return dayOfWeek[ans]
            