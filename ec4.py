import subprocess
import sys

# run 1, 48
d = sys.argv[1]
t = sys.argv[2]
s = sys.argv[3]

N = [200000, 300000, 400000, 600000, 700000, 800000, 900000]

for n in N:
	res = subprocess.run(['java', 'SSSP', '-a', '0', '-t', t, '-n', str(n), '-d', d], stdout = subprocess.PIPE)
	res_t = subprocess.run(['java', 'SSSP', '-a', '0', '-t', t, '-n', str(n), '-d', d, '-t', '4'], stdout = subprocess.PIPE)
	if len(str(res.stdout).split('\n')) != len(str(res_t.stdout).split('\n')):
		print("Error at", n, t, s)
	else:
		print("Success at", n, s, res.stdout.splitlines()[1])
