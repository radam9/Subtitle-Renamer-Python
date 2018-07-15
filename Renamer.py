import os, shutil

#Request Drama directory location from the user
ddir = input('Enter the Drama Directory: ')
#Defining the subtitle directory location with respect to the drama directory
sdir = ddir + '\sub'
#Creating lists with the names of the dramas and subtitles
dx = [i[2] for i in os.walk(ddir)]
sx = [i[2] for i in os.walk(sdir)]
#adding the directory to the location to the file names in the lists
dlist = dx[0]
dlist = [ddir + "\\" + d for d in dlist]
slist = sx[0]
slist = [sdir + "\\" + s for s in slist]
#Replacing the extension in the drama list from mkv to srt
nlist = dlist
nlist = [li.replace('.mkv','.srt') for li in nlist]

#defining the subtitle directory
s = os.listdir(sdir)
#creating a counter
i=0
#The loop that renames and moves the subtitles to the drama directory
for f in s:
    shutil.move(slist[i], nlist[i])
    i = i + 1
#Delete the empty subtitle folder
shutil.rmtree(sdir)
#The End
print('Subtitle Renaming Complete!')
z=input('Press any key to exit')
