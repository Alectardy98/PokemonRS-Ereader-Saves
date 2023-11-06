## Ereader File Formats Overview

- **.sav files**: These files serve as save files for the ereader, containing injected code.
- **.raw files**: They hold the DOT code information compressed in a format readable by emulators.
- **.bin files**: After decompression, they reveal the information of the header, code, and padding.
- **.vpk files**: These are bin files with the header information and padding code removed, showcasing solely the dot code.
- **_decompressed.vpk files**: Essentially vpk files that have been decompressed into a .z80 file format.
- **.ect files**: These contain the exact bytes necessary for encoding a trainer battle (188 bytes).
- **.ecb files**: They hold the exact bytes essential for encoding a berry (1580 bytes).

### Process of Creating .sav Files

1. Obtain .raw files from archive locations or through assembly compilation.
2. Use nedcenc.exe to decompile .raw into .bin files.
3. Trim bin files to remove header and padding using HxD.
4. Rename .bin to .vpk after removing padding.
5. Decompress .vpk using nevpk.exe and edit with HxD.
6. Edit and save the file as .ect for trainers or .ecb for berries.
7. Use WC3 Tool to further edit .ect or .ecb files and save changes.
8. Reintegrate modified code into (filename)_decompressed.vpk.
9. Recompress .vpk file using nevpk.exe.

### Save File Creation

Two options:
- **scotteh tool**: Simplified method, supports 128k saves.
- **Poke-Reader 1.1 by Team Fail**: Allows 128k and 64k saves.

**For Poke-Reader 1.1**:
- Customize the template.bin file by renaming "Template."
- Open Poke-Reader 1.1, import the modified code, and generate the desired save file.

**For the scotteh tool**:
- Visit [scotteh.me/vpk](https://scotteh.me/vpk).
- Import the .vpk file, name the code, and convert to your save file.

### Sources

- [Ereader Development Tools](https://www.caitsith2.com/ereader/devtools.htm)
- [Custom Ereader Cards](https://projectpokemon.org/home/forums/topic/58692-tutorial-creating-custom-trainerberry-e-cards/)
- [Gen 3 Mystery Gift Tool](https://digiex.net/threads/pokemon-gen-3-mystery-gift-tool-download-inject-nintendo-events-wondercards-more.14863/)
- [Poke-Ereader](https://projectpokemon.org/home/forums/topic/35340-gen-3-e-reader-event-injection/)
- [Scotteh Tool](https://scotteh.me/vpk/)
- [Full Decomplation of Ereader Assets](https://www.pokecommunity.com/showthread.php?t=455241)
- [Extremely Helpful Video for .ASM Compiling](https://www.youtube.com/watch?v=N_-xc0A7dSM)
- [Gameboy Advance Dev Docs](https://www.devrs.com/gba/docs.php#tutor)
- [Event Research, Byte Breakdown](https://projectpokemon.org/home/forums/topic/35903-gen-3-mystery-eventgift-research/)
- [Full Breakdown of .ect, .ecb File Structure](https://archives.glitchcity.info/forums/board-76/thread-7114/page-0.html)
