import os
SourcePath = '/Users/pavan/Desktop/GitHub/Python/AutomateBoringStuffWithPython'

'''for filename in os.listdir(SourcePath):
    print(filename)
'''

NewFile = os.path.join(SourcePath, 'WriteFile.txt')
nf = open(NewFile, 'a')

if os.path.exists(SourcePath):
    for filename in os.listdir(SourcePath):
        f = os.path.join(SourcePath, filename)
        print(f)

        fo = open(f,'r')

        #print(fo.read())
        for line in fo.read():
            nf.write(line)


nf.close()