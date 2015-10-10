#assignment 2
#the required modules are imported
import os,sys
from mutagen.easyid3 import EasyID3
import shutil
#the user's inputs are defined using sys
source_path= sys.argv[1]
dest_path= sys.argv[2]



def find_mp3s(path): #the find_mp3 function is defined
	#errors are raised when either the path doesn't exist or is not a string
	if isinstance(path, str)== False:
		raise TypeError('The input you entered is not a string.')	
	if os.path.exists(path)== False:
		raise ValueError('The path you entered does not exist.')
	else:	
		#a list, which would the absolute path to mp3 files, is created
		list_of_mp3s= []
		#the input path scanned using os.walk
		n= os.walk(path)
		for Dir_, SubDir_, Files in n:
			for file in Files:
				#the absolute path of all mp3s in the input path is gotten
				#and appended to the created list
				if file.endswith('.mp3')== True:
					m= os.path.abspath(os.path.join(Dir_, file))
					list_of_mp3s.append(m)
		#the list containing the paths is returned			
		return list_of_mp3s	




def load_id3(path): #the load_id3 function is defined
	#errors are thrown if the input path is not a string or if it doesn't exist
	if isinstance(path, str)== False:
		raise TypeError('The input you entered is not a string.')
	if os.path.exists(path)== False:
		raise ValueError('The path you entered does not exist.')
	else:
		try:
			#the EasyID3 instance is created
			id3 = EasyID3(path)
			return id3
			#a ValueError is thrown if the ID3 initialization fails
		except Exception:
			raise ValueError('Your mp3 file in missing required id3 data.')




def make_filename(id3):
	if isinstance(id3, EasyID3) == False:
	#raising error if id3 is not an instance of EasyID3
		raise TypeError('What you entered is not an EasyID3 instance.')
	#error is artist or title is missing
	try:
		a= id3['artist'][0]+' - '+id3['album'][0]+' - '+ id3['title'][0]+'.mp3'
		return a	
	#catching a key error that occurs when one of the tags are missing 	
	except KeyError:
		#to find out which tags are missing
		b= id3.get('artist', 'no artist tag found')
		c= id3.get('title', 'no title tag found')
		#if artist or title is missing
		if (b == 'no artist tag found') or (c == 'no title tag found'):
			raise ValueError('Your mp3 file is missing required artist/title tag data')
		#if album is missing 	
		else:
			V= id3['artist'][0]+'-'+ 'Unknown' +'-'+ id3['title'][0]+'.mp3'
			return V


	
def rename_mp3(input_mp3_path, output_mp3_path): #the rename_mp3 function is defined
	#throwing error if input_mp3_path does not exist
	if os.path.exists(input_mp3_path)== False:
		raise ValueError('The path you entered does not exist.')
	#get new name for mp3 file with path input_mp3_path
	n= make_filename(load_id3(input_mp3_path))
	#the output_mp3_path and the new name of the file are used to create a new file location
	m= os.path.join(output_mp3_path, n)
	try:
		#the file is copied to the new location
		shutil.copyfile(input_mp3_path, m)
	#IOError is caught and re-raised as ValueError
	except IOError:
		raise ValueError('unknown error')

#the final code is written, so that the program can take a source path
#run through it, find al the mp3 files, rename them, create a new location for them
#using the dest path(destination path) and copying them

#errors are raised if the amount of inputs is not correct or the source path doesn't exist		
if len(sys.argv) != 3:
	raise Exception('An error occured when reading your input')
if not os.path.exists(source_path):
	raise Exception('Invalid path')
try:
		#the mp3 files in the source path are found using find_mp3
	find_mp3s(source_path)
except Exception:
	raise 
c= 0
d= 0
for file_mp3s in find_mp3s(source_path):
	try:
		#the mp3 files are renamed and copied to their new location
		rename_mp3(file_mp3s, dest_path)
	#errors are caught 	
	except ValueError:
		d +=1
		print file_mp3s, 'could not be copied'
	else:
		c +=1
print '\n'
print c, 'files were successfully copied.'		
print 'An error occurred while copying', d, 'files.'