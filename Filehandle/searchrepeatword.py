import os
class Dataextractor:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, "r")
    def search(self):
        # Edge case 1: if file is empty
        # path = os.path.realpath(self.f.name)
        # self.f is file descriptor
        try:
            fsize = os.path.getsize(self.f.name)
        except FileNotFoundError:
            print("File not found")
        except FileExistsError:
            print("File exist error")
        except OSError:
            print("OS error")
        
        words_dict = {}
        for line in self.f:
            for word in line.split():
                if word in words_dict:
                    words_dict[word] +=1
                else:
                    words_dict[word] = 1
        return [k for k,v in words_dict.items() if v==max(words_dict.values())][0]

        
