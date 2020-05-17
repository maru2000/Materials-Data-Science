import os
from subprocess import Popen, PIPE, run
import re

def get_data_files(path):
	os.chdir(path)

	current = os.getcwd()
	print(current)

	flist = sorted(os.listdir())

	return flist

#for f in os.listdir():
#	print(f)

def run_gnuplot(commands, persist = True):
	args = ["/usr/bin/gnuplot", ]
	if persist:
		args.append("-persist")
	args.append("-e")
	args.append("; ".join([str(c) for c in commands]))
	in_pipe, out_pipe, err_pipe = PIPE, PIPE, PIPE
	cmd = ' '.join(args)
	gnuplot = Popen(cmd, stdin = in_pipe, stdout = out_pipe, stderr = err_pipe, shell=True)
	# gnuplot = run(args, stdin = in_pipe, stdout = out_pipe, stderr = err_pipe)
	
	out, err = gnuplot.communicate()
	# if err:
    #  	raise NameError('There was a problem with the gnuplot commands or data: ' + err.decode('ascii'))
	return out

def gnuplot_scope(context):
	commands = [
	"\"set term postscript eps enh col solid ",
	"set ou '{file1}'",
	"set pm3d map",
	"set xrange [0:2000]",
	"set yrange [0:2000]",
	"unset xtics",
	"unset ytics",
	"unset colorbox",
	"splot '{file2}' us 1:2:4 notitle",
	"set out\""
	]
	commands = [cmd.format(**context) for cmd in commands]
	return commands

# gnuplot = "/usr/bin/gnuplot"
# gp = subprocess.Popen(gnuplot, stdin=subprocess.PIPE)

if __name__ == "__main__":
	# context = {}

	# context['file2'] = 'prof_gp.0031000'
	# context['file1'] = 'prof0031000.eps'

	# commands = gnuplot_scope(context)
	# out = run_gnuplot(commands)

	flist = get_data_files('/home/maruthi/Data_ML/prof_gp.all')
	
	for file in flist:
		context = {}

		context['file2'] = file
		num = re.findall('\d+', file)
		out_file = 'prof' + str(num[0]) + '.eps'
		context['file1'] = out_file

		commands = gnuplot_scope(context)
		out = run_gnuplot(commands)

		# save_path = '/home/maruthi/Data_ML/EPS'
		# os.path.join(save_path, out_file)







	# for file2 in flist:
	# 	commands = gnuplot_scope(context)
	# 	# print(commands)
	# 	gnuplot_output = run_gnuplot(commands, persist = False)
	# 	print(gnuplot_output)




	# commands = gnuplot_scope(context)
	# print(commands)