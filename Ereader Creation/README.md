Ereader File Formats Overview
Ereader files encompass various formats:

.sav files: These files serve as save files for the ereader, containing injected code.
.raw files: They hold the DOT code information compressed in a format readable by emulators.
.bin files: After decompression, they reveal the information of the header, code, and padding.
.vpk files: These are bin files with the header information and padding code removed, showcasing solely the dot code.
_decompressed.vpk files: Essentially vpk files that have been decompressed into a .z80 file format.
.ect files: These contain the exact bytes necessary for encoding a trainer battle (188 bytes).
.ecb files: They hold the exact bytes essential for encoding a berry (1580 bytes).
Process of Creating .sav Files
The process I utilized to generate these .sav files is straightforward:

Acquire .raw files, commonly available and downloadable from various online archive locations (assembly compilation is an alternate but not discussed here).

Decompilation of .raw files into .bin files using nedcenc.exe, a program by caitsith2. The program is command-line-based. Use this code:
nedcenc.exe -i (filename).raw -d (filename).raw -o (filename).bin
This command instructs the program to input the .raw file, decompress it, and produce a .bin file.

Trim the bin file to a format suitable for decompression by removing the header at the beginning and the padding at the end. Utilize a hex editor like HxD for this task. Identify the 'vpk' indication at byte offset 36. Just before 'vpk', you'll find two bytes representing the vpk file size. Combine these bytes in little-endian format (e.g., 07 followed by 7D becomes 077D). Trim off the padding after the vpk information by locating byte 077D using HxD.

Rename the .bin file to .vpk after ensuring that only the vpk information remains in the file.

Decompress the .vpk file once more using nevpk.exe, another program by caitsith2. The command would be:
nevpk.exe -i (filename).vpk -d (filename).vpk -o (filename)_decompressed.vpk
This produces a file named (filename).vpk_decompressed.vpk, which can then be edited using a hex editor.

Depending on the type of code, you may need to navigate to specific byte offsets to edit English or Japanese trainer and berry information. After editing, save the file as .ect for a trainer or .ecb for a berry.

Next, use the WC3 Tool by Suloku to edit the .ect or .ecb file, enabling a user-friendly GUI for modifications. After editing, save the changes.

Reintegrate the modified code back into the (filename)_decompressed.vpk file using HxD by copying and pasting the information over the original trainer or berry information.

Compress the .vpk file back to the standard vpk format using:
nevpk.exe -i (filename)_decompressed.vpk -c (filename)_decompressed.vpk -o (filename)_compressed.vpk

Save File Creation
Two options for creating save files:

scotteh tool: This simpler method facilitates the creation of 128k saves but doesn't offer as much flexibility.
Poke-Reader 1.1 by Team Fail: More steps involved but allows the creation of both 128k and 64k saves.
For Poke-Reader 1.1: Customize the template.bin file by renaming the word "Template." Then, open Poke-Reader 1.1, import the modified code, and generate the desired save file.

For the scotteh tool: Visit scotteh.me/vpk, import the .vpk file, name the code, and convert it to your save file.

Sources
Ereader Development Tools
Custom Ereader Cards
Gen 3 Mystery Gift Tool
Poke-Ereader
Scotteh Tool
Full Decomplation of Ereader Assets
Extremely Helpful Video for .ASM Compiling
Gameboy Advance Dev Docs
Event Research, Byte Breakdown
Full Breakdown of .ect, .ecb File Structure
