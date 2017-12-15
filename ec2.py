import subprocess
import sys

# run 1, 48
t = 16
n = 10000

#D = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000, 2000000000, 300000000]
D = [2000000000, 300000000]

for delta in D:
    res = subprocess.run(['java', 'SSSP', '-a', '0', '-t', str(t), '-n', str(n), '-D', str(delta)], stdout = subprocess.PIPE)
    print("Success at", n, t, delta, res.stdout.splitlines()[1])
