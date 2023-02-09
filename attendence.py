"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:

for 5 days: 14/29

for 10 days: 372/773
"""


# dp_n[x] - count of ways we can attend n days such that consecutive x days including the nth day are skipped
n=int(input())
dp_n_minus_one=[1,0,0,0]
dp_n=dp_n_minus_one
for day in range(n):
    dp_n=[None]*4
    for skipped in range(4):
        dp_n[skipped]=dp_n_minus_one[skipped-1] if skipped!=0 else sum([dp_n_minus_one[d] for d in range(4)])
    dp_n_minus_one=dp_n
no_of_ways_for_attendence=sum([dp_n[d] for d in range(4)])
no_of_ways_to_miss_ceremony=sum([dp_n[d] for d in range(1,4)])
print(f"{no_of_ways_to_miss_ceremony}/{no_of_ways_for_attendence}")
