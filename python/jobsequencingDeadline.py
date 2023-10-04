class Job:
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit

def jobSequencing(jobs):
   
    jobs.sort(key=lambda x: x.profit, reverse=True)


    max_deadline = max(jobs, key=lambda x: x.deadline).deadline
    result = [None] * max_deadline
    total_profit = 0
    for job in jobs:
        for i in range(job.deadline - 1, -1, -1):
            if result[i] is None:
                result[i] = job.name
                total_profit += job.profit
                break

    return result, total_profit

# Example usage
jobs = [Job("J1", 2, 60), Job("J2", 1, 100), Job("J3", 3, 20), Job("J4", 2, 40),Job('J5',1,20)]
sequence, profit = jobSequencing(jobs)
print("Job sequence:", sequence)
print("Total profit:", profit)

