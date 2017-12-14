import subprocess
import sys

d = sys.argv[1]
t = sys.argv[2]
s = sys.argv[3]

N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]

for n in N:
	res = subprocess.run(['java', 'SSSP', '-a', '0', '-t', t, '-n', str(n), '-d', d], stdout = subprocess.PIPE)
	res_t = subprocess.run(['java', 'SSSP', '-a', '0', '-t', t, '-n', str(n), '-d', d, '-t', '4'], stdout = subprocess.PIPE)
	if len(str(res.stdout).split('\n')) != len(str(res_t.stdout).split('\n')):
		print("Error at", n, t, s)
	else:
		print("Success at", n, s, res.stdout.splitlines()[1])
