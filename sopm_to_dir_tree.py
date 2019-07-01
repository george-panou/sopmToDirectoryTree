# A python 2 script to aid with OTRS development
# To convert to pytohn 3 simply comment the 19th line and uncomment the 20th line
import sys
import shutil
import errno
import os


if __name__ == "__main__":

    fileDir = '/opt/otrs/DEV/Contracts.sopm'


    if len(sys.argv) == 3:
        fileDir = str(sys.argv[1])
        OutDir = str(sys.argv[2])

    else:
        print "Correct usage is : <./sopmt_to_dir_tree.py> <Path to sopm> <Path for output dir>"
        #print ("Correct usage is : <./sopmt_to_dir_tree.py> <Path to sopm> <Path for output dir>")
        sys.exit()


file = open(fileDir, 'r')
lines=file.readlines()
for e in lines:
    if "Location" in e:
        splited=e.split("Location=\"")
        splited=splited[1].split("\"")
        sourcefile="/opt/otrs/"+splited[0]
        print sourcefile

        try:
            shutil.copy(sourcefile, OutDir+splited[0])
        except IOError as e:
            # ENOENT(2): file does not exist, raised also on missing dest parent dir
            if e.errno != errno.ENOENT:
            	raise
            # try creating parent directories
            os.makedirs(os.path.dirname(OutDir+splited[0]))
            shutil.copy(sourcefile, OutDir+splited[0])



