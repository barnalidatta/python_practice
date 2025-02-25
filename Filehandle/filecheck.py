import os
def search():
        # Edge case 1: if file is empty
        # path = os.path.realpath(self.f.name)
        # self.f is file descriptor
        f = open("testfile.txt", 'r')
        try:
            fsize = os.path.getsize(f.name)
        except FileNotFoundError:
            print("File not found")
        except FileExistsError:
            print("File exist error")
        except OSError:
            print("OS error")
        
        words_dict = {}
        for line in f:
            for word in line.split():
                if word in words_dict:
                    words_dict[word] +=1
                else:
                    words_dict[word] = 1
        #print(words_dict)
        return [k for k,v in words_dict.items() if v==max(words_dict.values())][0]

v = search()
print(v)
