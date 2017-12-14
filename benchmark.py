import subprocess
import sys

d = sys.argv[1]
s = sys.argv[2]

N = [100000, 500000, 1000000, 5000000]
T = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

for n in N:
	for t in T:
		res = subprocess.run(['java', 'SSSP', '-a', '0', '-t', str(t), '-n', str(n), '-d', d, '-s', s], stdout = subprocess.PIPE)
		res_t = subprocess.run(['java', 'SSSP', '-a', '0', '-t', str(t), '-n', str(n), '-d', d, '-t', '4', '-s', s], stdout = subprocess.PIPE)
		if len(str(res.stdout).split('\n')) != len(str(res_t.stdout).split('\n')):
			print("Error at", n, t)
		else:
			print("Vertices:", n, "Thread:", t, res.stdout.splitlines()[1])
