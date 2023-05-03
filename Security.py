import os
os.mkdir("C:\Users\qaidj\Desktop\Qaidjohar\Computer_Science")
os.chdir("C:\Users\qaidj\Desktop\Qaidjohar\Computer_Science")
for i in range(10):     #layer 1
    os.mkdir(str(i))
    os.chdir(str(i))
    for j in range(10):     #layer 2
        os.mkdir(str(j))
        os.chdir(str(j))
        for k in range(10):     #layer 3
            os.mkdir(str(k))
            os.chdir(str(k))
            for l in range(10):     #layer 4
                os.mkdir(str(l))
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')
