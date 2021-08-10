class Solution:
    def pp(self, costs:List[List[int]]):
        for lists in costs:
            print(lists)
        
    def minCostUtil(self, costs: List[List[int]], indexOfCurrent ,colorOfLastHouse, memoisation):
        #if no more houses to be colored return 0
        if(indexOfCurrent >= len(costs)):
            return 0
        if(colorOfLastHouse != -1 and memoisation[indexOfCurrent][colorOfLastHouse] != -1):
            return memoisation[indexOfCurrent][colorOfLastHouse]
        
        indices_eligible = [0,1,2]
        if(colorOfLastHouse != -1):
            indices_eligible.pop(colorOfLastHouse)
        
        resultsAr = [100000,100000,1000000]
        for i in indices_eligible:
            resultsAr[i] = costs[indexOfCurrent][i] + self.minCostUtil(costs,indexOfCurrent+1 ,i,memoisation)
        memoisation[indexOfCurrent][colorOfLastHouse] = min(resultsAr)
        return min(resultsAr)
        
    def minCost(self, costs: List[List[int]]) -> int:
        memoisation = [[-1 for i in range(3)] for j in range(len(costs))]
        compute = self.minCostUtil(costs,0,-1,memoisation)
        return compute
        
        
