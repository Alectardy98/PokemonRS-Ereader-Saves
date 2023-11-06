"E-reader files come in various formats:

- .sav files serve as save files for the e-reader with injected code.
- .raw files contain DOT code information, compressed in a format readable by emulators.
- .bin files are decompressed raw files displaying header, code, and padding information.
- .vpk files are bin files with the removed header information and padding code, leaving only the DOT code.
- _decompressed.vpk files are exactly that—vpk files decompressed into .z80 file format.
- .ect files contain the exact bytes necessary for encoding a trainer battle (188 bytes).
- .ecb files contain the exact bytes necessary for encoding a berry (1580 bytes).

The process used to create these .sav files is pretty straightforward:
1. .raw files are readily available and can be downloaded from various archive locations on the internet. (They can also be compiled from assembly, but I won't go into that now.)

2. Decompile the .raw file into a .bin file using nedcenc.exe. This program, created by caitsith2, can be downloaded from their website: https://www.caitsith2.com/ereader/devtools.htm.

3. The program operates via command line. Navigate to the directory with the program and use the following code:

   `nedcenc.exe -i (filename).raw -d (filename).raw -o (filename).bin`

   Essentially, this command asks the program to "input" this .raw file and "decompress" it into a .bin file.

4. Now that you have the bin file, you'll need to convert it to a format that can be decompressed again. Remove the header at the beginning of the file and the padding at the end of the file. For this, a hex editor like HxD is necessary. Open the file, and you'll see a long string of bytes. Near the beginning, the word 'vpk' is written at offset (byte) number 36. Just before 'vpk,' you'll see two other bytes that indicate the actual vpk file's size. In our template bin, these two bytes before 'vpk' are 7D at offset 34 and 07 at offset 35. These are in little-endian format, meaning they need to be reversed and combined. For instance, 077D represents the last important byte for this .vpk file, and any information after that is padding. After removing the padding, change the file extension from .bin to .vpk.

5. Decompress the .vpk file once more to access the trainer or berry information. This is done with the tool nevpk.exe, also created by caitsith2. It's a command-line program:

   `nevpk.exe -i (filename).vpk -d (filename).vpk -o (filename)_decompressed.vpk`

   This leaves you with a file called (filename).vpk_decompressed.vpk, which can be opened in HxD. Further steps depend on the type of code you're editing.

   - For English Trainer card battle DOT codes, the battle information is located at offset D50 and extends to E0B (188 bytes in total).
   - Japanese Trainer card battle DOT codes typically have their battle information located at offset C08 and go until CC3 (188 bytes in total).
   - English Berry card DOT codes place their information at offset ECB.
   - Japanese Berry card DOT codes locate their information at 4EA and go until A19 (530 bytes in total).

   Note: Japanese Trainer cards might differ in structure; further investigation is needed to understand the necessary code. Source: Glitch City with a full breakdown of the .etc file structure.

6. Copy the code and paste it into a new file, which can be opened in HxD. Save the file with the extension .ect for a trainer or .ecb for a berry. The process gets engaging from here. You can edit these files in a program called WC3 Tool, created by Suloku. The application allows various edits, including injecting wonder cards into various save files. Choose the Ect editor or Ecb editor, import the .ect or .ecb file, make your edits through the GUI, and save the custom file.

7. Now, reverse most of these steps. Open your .ect or .ecb file in HxD, copy all the information, and paste it over the berry or trainer information located in your (filename)_decompressed.vpk file, making sure to overwrite the same number of bytes from the exact spot where you took the information initially. Any deviation will result in the card not working.

8. Recompress your .vpk file using this command in the command line:

   `nevpk.exe -i (filename)_decompressed.vpk -c (filename)_decompressed.vpk -o (filename)_compressed.vpk`

   This will compress your .vpk file back into the standard vpk format for injecting into the save file.

9. Two options exist to create your save file. The scotteh tool is more straightforward, allowing 128k saves. Another option is Poke-Reader 1.1 by Team Fail, enabling both 128k and 64k saves.

   For Poke-Reader 1.1:

   - Open the template.bin file in HxD, where you'll find the word "Template." This will be displayed on the e-reader when you boot up the save. Rename this as desired, ensuring it's not excessively long. Then save the file and proceed. Open Poke-Reader 1.1, import Template.bin, import the (filename)_compressed.vpk file with your modified code, and follow the steps to create your new save file.

   For the scotteh tool:

   - Go to https://scotteh.me/vpk/ and import your .vpk file. Name it as desired, then hit convert to create your save.

Sources:
**Helpful Links:**

- [E-reader Development tools](https://www.caitsith2.com/ereader/devtools.htm)
- [Custom E-reader cards](https://projectpokemon.org/home/forums/topic/58692-tutorial-creating-custom-trainerberry-e-cards/)
- [Gen 3 Mystery Gift Tool](https://digiex.net/threads/pokemon-gen-3-mystery-gift-tool-download-inject-nintendo-events-wondercards-more.14863/)
- [Poke-Ereader](https://projectpokemon.org/home/forums/topic/35340-gen-3-e-reader-event-injection/)
- [scotteh tool](https://scotteh.me/vpk/)
- [Full Decompilation of e-reader assets](https://www.pokecommunity.com/showthread.php?t=455241)
- [Extremely helpful video for .ASM compiling](https://www.youtube.com/watch?v=N_-xc0A7dSM)
- [Gameboy Advance Dev Docs](https://www.devrs.com/gba/docs.php#tutor)
- [Event Research, Byte breakdown](https://projectpokemon.org/home/forums/topic/35903-gen-3-mystery-eventgift-research/)
- [Detailed breakdown of .etc, .ecb file structure](https://archives.glitchcity.info/forums/board-76/thread-7114/page-0.html)

The tools listed here are NOT my own, and I do not intend to caim as such, I do not know copyright law and if I am in any violation please let me know, I do not intend to harm or steal the work of another person
