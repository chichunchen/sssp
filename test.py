import subprocess
import sys

# print(sys.argv)
N = int(sys.argv[1])
d = sys.argv[2] or 10
S = int(sys.argv[3]) or 0
t = sys.argv[4] or 4

for n in range(N, N+60):
    for s in range(S, S+60):
        res = subprocess.run(['java', 'SSSP', '-a', '1', '-t', t, '-n', str(n), '-d', d, '-s', str(s)], stdout = subprocess.PIPE)
        res_t = subprocess.run(['java', 'SSSP', '-a', '1', '-t', t, '-n', str(n), '-d', d, '-t', '4', '-s', str(s)], stdout = subprocess.PIPE)
        if len(str(res.stdout).split('\n')) != len(str(res_t.stdout).split('\n')):
            print("Error at", n, t, s)
        else:
            print("Success at", n, s)
