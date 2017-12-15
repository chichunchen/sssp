import subprocess
import sys

# run 1, 48
d = sys.argv[1]
t = sys.argv[2]
s = sys.argv[3]

# N = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 2000000]
N = [11000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 11000000]
# N = [10000000, 5000000]
Vertices = range(4, 5)
Base = 10
Scale = 1000000

for v in Vertices:
    n = v * Scale
    # Base = n
    res = subprocess.run(['java', 'SSSP', '-a', '0', '-t', t, '-n', str(n), '-d', d], stdout = subprocess.PIPE)
    print("Success at", n, s, res.stdout.splitlines()[1])
