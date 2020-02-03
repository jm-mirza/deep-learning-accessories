'''
For renaming all the files in a directory
'''
import os
# Function to rename multiple files
def main():


   i = 0
###Add path to your file###
   path="path/to/your/file"

   for filename in os.listdir(path):

###Add phrase with which you want your names to be appended###

      my_dest ="ADD WORD/PHRASE HERE" + str(i) + ".txt"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1

# Driver Code
if __name__ == '__main__':
	main()
