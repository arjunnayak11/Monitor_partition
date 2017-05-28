""" Monitors the partitions on a linux server
and notifies if the partition usage is beyond the set threshold """
import subprocess
# threshold at which we should raise the alarm
partition_usage_threshold = 5
# run the linux command using the subprocess module
df_cmd = subprocess.check_output(['df','-k'])
print df_cmd
# split the output into a list called lines
lines = df_cmd.splitlines()
print lines
# for each line except the first once, since that has the column names
for line in lines[1:]:
# split the line into columns
	columns = line.split()
# get the used percentage val from column 4
	used_percentage = columns[4]
# remove the % sign
	used_percentage = used_percentage.replace('%','')
# check for threshold breach
	if int(used_percentage) >= partition_usage_threshold:
		print "partition %s usage is beyond threshold at %s " % (columns[0], columns[4])
