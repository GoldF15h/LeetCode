class Solution:
    def reformatDate(self, date: str) -> str:
        monthDict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        d,m,y = date.split()
        m = monthDict[m]
        tmp = ''
        for i in range(len(d)) :
            if d[i].isnumeric() :
                tmp += d[i]
        d = tmp
        
        if m < 10 :
            m = '0' + str(m)
        else :
            m = str(m)
        
        if len(d) == 1 :
            d = '0' + d
        
        return y + '-' + m + '-' + d
        
        