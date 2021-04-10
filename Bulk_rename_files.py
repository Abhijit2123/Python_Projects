import os
class rename_file(object):

    def rename(path):
    
        i = 0
        for file in os.listdir(path):
            filename = "file_"+str(i)+".txt"
            my_source = path + file
            my_dist = path + filename
            os.rename(my_source , my_dist)
            i = i + 1

T = rename_file
T.rename(input("Please enter path: "))
