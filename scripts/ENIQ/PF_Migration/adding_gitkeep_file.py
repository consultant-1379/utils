import os, sys

def removeEmptyFolders(path, removeRoot=True):
  	'Function to remove empty folders'
	if not os.path.isdir(path):
		return

  # remove empty subfolders
	files = os.listdir(path)
	if len(files):
		for f in files:
			fullpath = os.path.join(path, f)
			if os.path.isdir(fullpath):
				removeEmptyFolders(fullpath)

  # if folder empty, delete it
	files = os.listdir(path)
	if len(files) == 0 and removeRoot:
		print "Removing empty folder:", path
		os.system('touch '+path+'/.gitkeep')
    #os.rmdir(path)

def usageString():
	'Return usage string to be output in error cases'
	return 'Usage: %s directory [removeRoot]' % sys.argv[0]

if __name__ == "__main__":
	removeRoot = True

	if len(sys.argv) < 1:
		print "Not enough arguments"
		sys.exit(usageString())

	if not os.path.isdir(sys.argv[1]):
		print "No such directory %s" % sys.argv[1]
		sys.exit(usageString())

	if len(sys.argv) == 2 and sys.argv[2] != "False":
		print "removeRoot must be 'False' or not set"
		sys.exit(usageString())
	else:
		removeRoot = False

	removeEmptyFolders(sys.argv[1], removeRoot)

	os.chdir('/proj/eiffel013_config_fem6s11/PF_Module_Vobs/')
	for dirpath, dirnames, files in os.walk('.'):
		if not (files or dirnames):
			print dirpath+" is empty\n"
			os.chdir(dirpath)
			os.system('touch .gitkeep')
