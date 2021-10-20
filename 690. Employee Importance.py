"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

def sumEmployee(emList,_len,id) :
    _sum = 0 
    subList = []
    for i in range(_len) :
        if emList[i].id == id :
            _sum += emList[i].importance
            subList = emList[i].subordinates
    for i in range(len(subList)) :
        _sum += sumEmployee(emList,_len,subList[i])
    return _sum

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        return sumEmployee(employees,len(employees),id)