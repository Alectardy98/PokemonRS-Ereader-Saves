Ereader files come in various formats
.sav files are in this context, save files for the ereader, with injected code
.raw files are the DOT code information that is compressed in a format that can be read by emulators
.bin files are decompressed raw files that show the information of the header, code, and padding
.vpk files are bin files that have had the header information and padding code removed, leaving only the dot code
_decompressed.vpk files are excactly that, vpk files that have been decompressed into a .z80 file format
.ect files are the exact bytes necessary for encoding a trainer battle (188 bytes)
.ecb files are the exact bytes necessary for encoding a berry (1580 bytes)

The process that I used to make these .sav files is pretty straight forward
1. .raw files are pretty redily aviable, and can be downloaded from various archive locaitons on the internet. (they can also be compiled from assimbly but I wont go there now)

2. Decompile .raw file into .bin file using nedcenc.exe, This is a program made by caitsith2 and can be downloaded from there website
https://www.caitsith2.com/ereader/devtools.htm

3.The program is comand line baised, cd into the directy with the program and use this code 

nedcenc.exe -i (filename).raw -d (filename).raw -o (filename).bin 

Bacialy what your asking this program to do is "hey nedcenc, im -i(inputting) this .raw file and please -d(decompress) it and make it a .bin file.

4.Now that you have the bin file your going to need to get it into a format tha can be decompressed again, to do this we must remove the header at the begining of the file and the padding at the end of the file. To do this you will need a hex editor like HxD. Open the file and you will see a larg sting of bytes. In the beging you will see the word vpk written at ofset(byte) number 36. The byts for vpk are written as 76 70 6B. Right before that you will see two other bytes, and those two bytes indacate how large the actual vpk file is. In my template bin you will see that the two bytes right before vpk are 7D at (ofset 34) and 07 at (ofset 35). These are written in little endian, maning that we must reverse them and combine them to get the information we want to know. On a seporate notepad or in your head, look at byte 35 first and then put byte 34 right after it. In out case that would make it look like 077D. This tells us that 0x077D is that last inportant byte for this .vpk file, and any information after that is padding.(NOTE, this is in refrence to the start of the vpk file, so delete everything before the words vpk(76 70 6B) before the next step. Now that that is done we can remove the padding. For people using HxD you can use Ctrl+G to input 077D to jump to that byte. You will see that this padding is pretty clear to see, going from 00, 01, 02 and onward, you can just delet all of that. 

5.Now your file only has the .vpk information, so we can close HxD and rename the file extension from .bin to .vpk.

6.Now we have to decompress the .vpk file one more time to acess the trainer or berry infomration. This is done with the tool nevpk.exe also made by caitsith2. This is also a comonad line program, and use the code

nevpk.exe -i (filename).vpk -d (filename).vpk -o (filename)_decompressed.vpk

This will leave you with a file called (filename).vpk_decompressed.vpk, Which we will yet again open with HxD. From here the steps varry depeding on what type of code your edditing.

English Trainer card battle dot codes have there battle information located at ofset D50 and go untill E0B (188 bytes in total)
Japanese Trainer card battle dot codes (NORMALLY) have there battle information located at ofset C08 and goes until CC3 (188 bytes in total)
English Berry card dot codes have there berry infomation at ofset ECB and go untill 
Japanese Berry card dot codes have there berry infmation located at 4EA and go untill A19 (530 bytes in total)

Notice that I said Normally for Japanese Trainers, this is inportant and one of the dificulties that I ran into, below you will need to further investage the structure of trainer .ecb files to understand exactly what code you will need. You will see that at the vary end with the source to glitch city, and a full breakdown of the .etc file scture

From here copy the code and paste it into a new folder, you can just open a new file in HxD. Then save the file with the extension .ect for a trainer or .ecb for a berry. From here the procees gets pretty fun. You can actually edit these files in a cool program made by Suloku called WC3 Tool. The Applacation can do many more things like injecting wondercards to various save files, but we are going to use the Ect editor and Ecb editor. Just select what edidtor you want and import the .ect or .ecb file you just made. Now you have a GUI to do what ever it is that you would like. Once your done just hit save and your custom file will be made. 

Now we just need to do most of these steps but in reverse. We are going to take your .ect or .ecb file and open it in HxD and copy all of the infomation and past it over the berry or trainer information that was located in your (filename)_decompredded.vpk make sure you are overighting the exact same number of bytes, from exactly the spot you took the infmation in the first place. Any deviation will result in your card not working.

Now you need to recompress your .vpk file back up, In the comand line use this command 

nevpk.exe -i (filename)_decompressed.vpk -c (filename)_decompressed.vpk -o (filename)_compressed.vpk

This will compress your .vpk file back into the standerd vpk format that we can use to inject into our save file.

Now we have two difernt options to make our save file, If you just want to use your save file on an emulator, or real ereader you can use the scotteh tool. The benifit is that its much easier, but you can only get 128k saves from it. The other option is Poke-Reader 1.1 by Team Fail, which takes a few more steps but allows you to create both 128k saves and 64k saves. 

(Steps for Poke-Reader 1.1)
Now we are going to open the template.bin file that I provided in a HxD and at the vary top you will seed the words "Template". These are the words that will show up on the ereader when you boot up the save. You can rename this to what ever you like, but make sure its not too long or else you will get an error. I dont know the exact length that it can be, but you have quite a lot of space before this happens. To rename, go to the right side of HxD where the word template is and you can directly type over the word that is currently written. DO NOTE, you want to OVERIGHT what is currently written, and not add to the file. The file size should NOT change when you change the name. Once done you can save the file and close HxD. Now we are on the last step. Nomrally there would be a lot of calucations that we would have to do to correct checksums, or math that the ereader uses to varify if the file had been read properly. Thanfully the Program that we will use will do all of this for us. Open Poke-Reader 1.1 and inport Template.bin, and you will see that the new name you gave the bin file will be properly loaded. Then you can go to the import .vpk file option and select the (filename)_compressed.vpk with your modified code. From here you can save the file to either 64k.sav files or 128k.save files. You will first need to select the blank save located in the blank save folder, and then the program will allow you to create your new save file. Then thats it, you have your custom ereader save!

(Steps for the scotteh tool)
Go to https://scotteh.me/vpk/ and inport your .vpk file. It will then ask you to write what you would like the ereader to recgonise the code to be called. Name it what ever you would like, this will not effect anything in game, and will only effect what is shown on the ereader. THen you hit convert and you have your save!


Sources
Erereader Devopment tools - https://www.caitsith2.com/ereader/devtools.htm
Custom Ereader cards - https://projectpokemon.org/home/forums/topic/58692-tutorial-creating-custom-trainerberry-e-cards/
Gen 3 Myster Gift Tool - https://digiex.net/threads/pokemon-gen-3-mystery-gift-tool-download-inject-nintendo-events-wondercards-more.14863/
Poke-Ereader - https://projectpokemon.org/home/forums/topic/35340-gen-3-e-reader-event-injection/
scotteh tool - https://scotteh.me/vpk/
Full Decomplation of ereader assets - https://www.pokecommunity.com/showthread.php?t=455241
Extramly helpful video for .ASM compileing - https://www.youtube.com/watch?v=N_-xc0A7dSM
Gameboy Advance Dev Docs - https://www.devrs.com/gba/docs.php#tutor
Event Reaserch, Byte breakdown - https://projectpokemon.org/home/forums/topic/35903-gen-3-mystery-eventgift-research/
THE MOST USEFUL- Full breadown of ect, ecb file structre - https://archives.glitchcity.info/forums/board-76/thread-7114/page-0.html


