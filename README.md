subtitles_offset
================

split one subtitles file (.srt) in two (useful if your movie is contained in two files)

This is a very ad-hoc python code. It basically creates a second subtitles file starting from your imput mark (your splitting time point).
It is a common issue to have two video files and only one entire_movie subtitles file. This program only adjusts the subtitles by substracting the duration of the first part of the video (so subtitles of second part start at 0 time).
If you want to make it adaptable to more situations (ie. video splitted in N files) feel free to fork the project or ask me to do it.

Usage:

0) Place your original subtitles file (.srt) in the source code folder (I know, just got lazy to check for paths! :-P )

1) Edit the config.cfg file with your own parameters
1.1) file_name = <your_file_name_placed_in_your_code_folder> (example: file_name = No Maps For These Territories.srt) <-- no quotes used
1.2) set your partition mark, search for the time mark that comes after the first video part (example: partition_mark = 00:44:23,280)
1.3) the offset to substract is the duration of the first part of the video in seconds (offset_to_substract_in_seconds = 2660, first part ends at 44:20, 44 minutes 20 seconds = 44*60 + 20 = 2660 seconds)

2) run the subtitles_offset: python subtitles_offset.py

3) that's it, you'll see your brand new second_part.srt subtitles file!
