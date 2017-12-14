import subprocess


for n in range(8, 20):
    for d in [10]:
        for s in range(100):
            res = subprocess.run(['java', 'SSSP', '-a', '1', '-t', '4', '-n', str(n), '-d', str(d), '-s', str(s)], stdout = subprocess.PIPE)
            res_t = subprocess.run(['java', 'SSSP', '-a', '1', '-t', '4', '-n', str(n), '-d', str(d), '-t', '4', '-s', str(s)], stdout = subprocess.PIPE)
            if len(str(res.stdout).split('\n')) != len(str(res_t.stdout).split('\n')):
                print("Error at", n, t, s)
            else:
                print("Success at", n, s)
