import subprocess
gen_data_p = subprocess.Popen(['./gen_data'], stdout = subprocess.PIPE)

for i in range(10000):
    line_raw = next(gen_data_p.stdout)
    print(line_raw.decode('utf-8'))

gen_data_p.terminate()
print("Finished subprocess call")

