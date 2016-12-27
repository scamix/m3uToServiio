import glob, os
from urllib.parse import quote
os.chdir(os.getcwd())

for file in glob.glob("*.m3u"):
    nomefile = str(file).rsplit(".")[0]+".serviio"
    text_file = open(nomefile, "w")
    text_file.write('<?xml version="1.0" encoding="UTF-8" ?>\n<onlineRepositoriesBackup>\n<items>\n')
    with open(file) as f:
        count=1
        for linea in f:

            #line = f.readline()
            if linea != "#EXTM3U\n":
                text_file.write('<backupItem enabled="true" order="' +str(count)+'">\n')
                text_file.write('<serviioLink>serviio://video:live?url=')
                nomeCanale = linea.split(",")[1].replace("\n","").replace("&", "e")
                linkCanale = f.readline().replace("\n","")
                linkCanaleEncoded = quote(linkCanale , safe="")
                text_file.write(linkCanaleEncoded)
                text_file.write('&amp;name='+nomeCanale+'</serviioLink>\n<accessGroupIds>\n<id>1</id>\n</accessGroupIds>\n</backupItem>\n')
                count=count+1
        text_file.write('</items>\n</onlineRepositoriesBackup>')
        text_file.close()



