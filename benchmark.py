import subprocess
import sys

d = str(20)
s = str(10)

N = [1000000, 2500000]
T = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

for n in N:
    for t in T:
        res = subprocess.run(['java', 'SSSP', '-a', '0', '-t', str(t), '-n', str(n), '-d', d, '-s', s], stdout = subprocess.PIPE)
        print("Vertices:", n, "Thread:", t, res.stdout.splitlines()[1])
