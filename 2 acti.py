# open file and store file object in a variable
file = open('rrr.txt')
 # red the contents of file
print(file.read())

# close the file
file.close()

# open file in red mode
file_read = open('rrr.txt','r')
print("File ina Read mode")
print(file_read.read())
file_read.close()
# open the file in write mode 
file_write = open('rrr.txt','w')
# write in the file 
file_write.write(" File in write mode.....")
file_write.write("Hi I am mad")
file_write.close()
# open the file in append mode
file_append = open('rrr.txt', 'a')
# append in the file
file_append.write("\n File in append mode ......")
file_append.write("Hi I am mad")
file_append.close()
