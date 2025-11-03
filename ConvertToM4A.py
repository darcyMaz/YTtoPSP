import subprocess
import argparse
import os
from mutagen.mp4 import MP4

def update_m4a_tags(path, track_tuple, album, artist, title):

    audio = MP4(path)

    # Delete all previous tags.
    if audio.tags != None:

        # Can't dynamically remove the tags.
        # So, add the tags to a list and then remove them.
        tag_list = []
        for tag in audio.tags.keys():
            tag_list.append(tag)
        for tag in tag_list:
            audio.tags.pop(tag)
    else:
        audio.add_tags()

    tags = audio.tags

    if not track_tuple[0] < 0:
        # This is a tuple of track number and total tracks: (trkn, total_tracks)
        tags["trkn"] = [track_tuple]

    # If the album and artist are not given, they will be the empty string.
    # In this case, just don't add the tags.
    if not album == "":
        tags["\xa9alb"] = album

    if not artist == "":
        tags["\xa9ART"] = artist

    tags["\xa9nam"] = title

    tags.save(path)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="The input audio file of any format.")
    parser.add_argument("-o", "--output_folder", help="The folder to send the output audio file which will be compatible with a PSP.")
    parser.add_argument("-tn", "--track_number", help="Track number in its respective playlist or album")
    parser.add_argument("-tt", "--track_total", help="Number of tracks in this album or a playlist")
    parser.add_argument("-ar", "--artist", help="Artist. The individual, group, band, etc.")
    parser.add_argument("-al", "--album", help="Title of the album.")
    parser.add_argument("-ti", "--title", help="The title of the song.")

    args = parser.parse_args()

    if args.input == None:
        parser.print_usage()
        print("The input file is a required argument for this script.")
        return 1
    if args.output_folder == None:
        parser.print_usage()
        print("The output destination is a required argument for this script.")
        return 1

    len_1_list = os.listdir(args.input)    
    if len(len_1_list) != 1:
        print("There must be only one song in the input folder for this script.")
        return 1
    
    track_number_int = int(args.track_number)
    track_number = ""
    if track_number_int < 1:
        print("Invalid track number.")
        return 1
    if track_number_int < 10:
        track_number = "0" + args.track_number
    else:
        track_number = args.track_number

    # Convert to the correct format for my PSP.
    sys_command_list = ['node', './podhnologic/index.js', '--input', args.input, '--output', args.output_folder, '--codec', 'aac']
    output = subprocess.run(sys_command_list, capture_output=True)    

    if output.returncode == 0:

        # Update the tags, get the proper filepath.
        filename = args.output_folder + "/" + os.path.basename(len_1_list[0])[:-4] + ".m4a"
        update_m4a_tags(filename, (  int(args.track_number) ,  int(args.track_total) ), args.album, args.artist, args.title)
        
        # Add the track number to the front of the filename
        filename_renamed = args.output_folder + "/" + track_number + " - " + os.path.basename(filename)
        os.rename(filename, filename_renamed)

        print("Track created successfully in the destination folder {}".format(args.output_folder))
        return 0
    else:
        print("Error running the pudhnologic subdirectory.")
        print(output.stdout)
        print(output.stderr)
        return 1

if __name__ == "__main__":
    main()
    
