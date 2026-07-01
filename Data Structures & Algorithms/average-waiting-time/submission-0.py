class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        cur_time = customers[0][0]
        for s, t in customers:
            if cur_time > s:
                time += cur_time - s
            else:
                cur_time = s
            time += t
            cur_time += t 

        return time / len(customers)