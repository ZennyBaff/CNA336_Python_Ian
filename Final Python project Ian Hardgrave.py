#Automatically updates a Minecraft Server
#CNA336 , 6/19/2018
#Ian Hardgrave , theholyboots@gmail.com


#Citations:
#For downloading the Minecraft.Jar: https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un
#Cahnging directories: https://www.youtube.com/watch?v=yEiejQk3Imc&t=163s
#File Size: https://www.w3resource.com/python-exercises/file/python-io-exercise-11.php
#Checking if a file exists: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists
#Provides the current directory: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
#Press any key to continue command: https://www.sololearn.com/Discuss/76445/how-to-make-python-3-5-press-any-key-to-continue

import os
import requests
import shutil

OV = input("Please input the current(old) Minecraft server version (example:#.##.#): ")                          #Variable that requests input for the old server version/location.
V = input("Please input the new Minecraft server version (example:#.##.#): ")                                    #Variable that requests input for the new server version/location

SourceFiles = os.path.dirname(os.path.realpath(__file__)) + "\Minecraft Server " + OV
DestFiles = os.path.dirname(os.path.realpath(__file__)) + "\Minecraft Server " + V

if os.path.exists(DestFiles):                                                                                    #Safetynet for creating another server that is already created
    print("This version of the server is already created.")                                                      #Found another server folder with the same name
    input('Press Enter to continue')
    quit()
else:
    print("Creating your new server!")                                                                           #Continues to creating the new server folder after checking the current server folder names.

print("Downloading Latest Minecraft Server Jar...")
url = 'https://launcher.mojang.com/mc/game/' + V + '/server/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar' #Downloads the minecraft server.jar file
r = requests.get(url, allow_redirects=True)                                                                      #Downloads the minecraft server.jar file
open('minecraft_server.' + V + '.jar', 'wb').write(r.content)                                                    #Downloads the minecraft server.jar file

if os.stat('minecraft_server.' + V + '.jar').st_size >= 2000:                                                    #Saftynet for downloading blank Jar files
    print("Minecraft Server Jars downloaded")                                                                    #Checked the new Jar file is over 2000 bytes
else:
    print("That server version is not available.")                                                               #Stop the process and delete the created Jar file if it is blank
    os.remove("minecraft_server." + V + ".jar")
    input('Press Enter to continue')
    quit()

shutil.copytree(SourceFiles , DestFiles)                                                                        #Copies OV server folder to V server folder
print("Server files copied")

os.remove(DestFiles + "\minecraft_server." + OV + ".jar")                                                       #Removes old Jar file from new server folder
shutil.copy(os.path.dirname(os.path.realpath(__file__)) + "\minecraft_server." + V + ".jar" , DestFiles)        #Copies new Jar file from director to new server folder
os.remove(os.path.dirname(os.path.realpath(__file__)) + "\minecraft_server." + V + ".jar")                      #Removes new Jar file from directory
print("Removed extra remaining files")

edit_eula_txt = open("eula.txt", "w")                                                                           #Creates an acceptable EULA.txt file when launching the Start.bat
edit_eula_txt.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
edit_eula_txt.write("#Thu Jun 07 18:46:38 PDT 2018\n")
edit_eula_txt.write("eula=true")
edit_eula_txt.close()
print("Created new Eula")

edit_start_bat = open("Start.bat", "w")                                                                          #Creates a batch file for starting the minecraft server. Start.bat
edit_start_bat.write("java -Xmx1024M -Xms1024M -jar ./minecraft_server." + V + ".jar nogui\n")
edit_start_bat.write("pause")
edit_start_bat.close()
print("Created new Start.bat")

shutil.copy(os.path.dirname(os.path.realpath(__file__)) + "\Start.bat" , DestFiles)                              #Copies the Start.bat batch file to the correct server verison folder that was labeled in "SourcesFiles" input
os.remove(os.path.dirname(os.path.realpath(__file__)) + "\Start.bat")                                            #Removes the Start.bat batch file that was left behind after the copy

shutil.copy(os.path.dirname(os.path.realpath(__file__)) + "\eula.txt" , DestFiles)                               #Copies the eula.txt text file to the correct server version folder that was labeled in "SourceFiles" input
os.remove(os.path.dirname(os.path.realpath(__file__)) + "\eula.txt")                                             #Removes the eula.txt text file that was left behind after the copy

os.chdir(DestFiles)                                                                                              #Changes the directory to the new server version folder.
os.system("Start.bat")                                                                                           #Starts the server for the first time. (Runs Start.bat)
print("Starting up your Minecraft " + V + "Server")

key = input('Server was Stopped! Press Enter to continue')
quit()

