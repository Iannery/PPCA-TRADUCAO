import os

name = []
# check every folder of the cic folder
for folder in os.listdir('toparse'):
    # check every file of the folder if it has a file named en_US.html, if not, copy the pt_BR.html file to en_US.html
    if not os.path.exists('toparse/' + folder + '/en_US.html'):
        # print(folder)
        os.system(
            f'cp toparse/{folder}/pt_BR.html toparse/{folder}/en_US.html')
