from mutagen.mp4 import MP4
from pytubefix import Playlist
import os
import shutil
import argparse
import subprocess

def update_m4a_tags(path, track_number, total_tracks, album, artist, title):
    
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
    
    tags["trkn"] = [(track_number,total_tracks)] 
    tags["\xa9nam"] = title

    # If the album and artist are not given, they will be the empty string.
    # In this case, just don't add the tags.
    if not album == "":
        tags["\xa9alb"] = album

    if not artist == "":
        tags["\xa9ART"] = artist

    tags.save(path)

def rm_temp_folder(temp_folder_path):
    try:
        shutil.rmtree(temp_folder_path)
    except:
        print("Temp directory could not be removed.\nThere is no danger if you delete it on your own. The audio file in this folder won't play on your PSP (at least not mine) but they still work.")

# Function which builds the exclusion list, checking if the input is invalid.
# Returns [] for invalid inputs.
# Returns a list of integers for valid inputs.
def build_exclusion_list(ex_str, total_tracks):

    if not (ex_str[0]=='[' and ex_str[-1] == ']'):
        print("The exclusion list is not the right format (  eg. [1,2,3]  ).")
        return []
    ex_str = ex_str[1:-1]
    ex_items_str = ex_str.split(",")

    if len(ex_items_str) > total_tracks:
        print('There are more tracks in your exclusion list than there are tracks in the playlist.')
        return []

    tracks_to_exclude = []

    for trkn_str in ex_items_str:
        if trkn_str == '':
            print("One of your tracks to exclude was the empty string. Possibly because the exclusion list was empty")
            return []
        if trkn_str[0] == "-" and trkn_str[1:].isnumeric() or trkn_str == "0":
            print('The track {} on the exclusion list is less than 1'.format(trkn_str))
            return []
        if not trkn_str.isnumeric():
            print('One of your tracks to exclude is not a number or is a decimal number. The track is {}'.format(trkn_str))
            return []
        trkn = int(trkn_str)
        if trkn > total_tracks:
            print('One of your tracks to exclude is greater than the total number of tracks in the playlist. The track is {} out of {} songs'.format(trkn_str, total_tracks))
            return []
        tracks_to_exclude.append( trkn )
    return tracks_to_exclude


def main():

    parser = argparse.ArgumentParser()

    # -link LINK -dest DESTINATION -arti ARTIST -albu ALBUM -exls EXLUDE_LIST
    parser.add_argument("-lk", "--ytlink", help="YouTube Playlist Link")
    parser.add_argument("-dt", "--destination", help="Destination Folder")
    parser.add_argument("-ar", "--artist", help="Artist. The individual, group, band, etc.")
    parser.add_argument("-al", "--album", help="Title of the album.")
    parser.add_argument("-ex", "--exclude_list", help="List of integers of any songs you would like to exclude from being downloaded. Useful for playlists that include an extra video that includes every song.")

    args = parser.parse_args()

    if args.ytlink==None or args.destination == None:
        parser.print_usage()
        print("The YouTube Link and the Destination folder are required arguments.")
        return 1

    link = args.ytlink
    playlist = Playlist(link.strip())

    # Checking the length of the playlist, when the link was invalid, creates an error.
    # Catch this error, tell the user the link is invalid, then end the program.
    try:
        len(playlist)
    except:
        print("The playlist link is in the wrong format or it cannot find a playlist at the link.")
        return 1

    # This doesn't make any sense right? The output folder will be genuinely different right?
    # Get rid of the replace.
    destination = args.destination # ) .replace(" ", "_")

    # If these arguments are not given then set them to the empty string.
    if args.artist == None:
        artist = ""
    else:
        artist = args.artist
    
    if args.album == None:
        album = ""
    else:
        album = args.album

    track_number = 0
    total_tracks = len(playlist)

    exclusion_list = []
    exclusions = False
    # If there is an argument for the exclusion list.
    if not args.exclude_list == None:
        # Check the validity of the list, and return it as a list from a string.
        exclusion_list = build_exclusion_list(args.exclude_list, total_tracks)
        # If [] is returned then an empty list or invalid input was given.
        if not len(exclusion_list) == 0:
            exclusions = True

    temp_destination = destination + "_temp"

    for video in playlist.videos:

        # incrememnt track number
        track_number += 1

        # Skips a track number if it appears on the exclusion list.
        if exclusions and not exclusion_list.count(track_number) == 0:
            continue

        # Change track title to have the track number at the start
        str_trkn = str(track_number)
        if len(str_trkn) == 1:
            # If trkn is a single digit add a zero
            video.title = "0" + str(track_number) + " - " + video.title
        else:
            # Else just add it w/o a leading zero
            video.title = str(track_number) + " - " + video.title

        # extract only audio
        audio = video.streams.filter(only_audio=True).first()

        # download the file
        out_file = audio.download(output_path=temp_destination)

        # update m4a tags
        update_m4a_tags(path=out_file, track_number=track_number, total_tracks=total_tracks, album=album, artist=artist, title=video.title)  

        
    # Fix the codec for all audio files.
    # The codec at this point is M4A AAC 0 kbps but should be M4A AAC 256 kbps
    sys_command_list = ['node', './podhnologic/index.js', '--input', temp_destination, '--output', destination, '--codec', 'aac']
    output = subprocess.run(sys_command_list, capture_output=True)

    if output.returncode == 0:
        print("Tracks downloaded successfully in the destination folder {}".format(destination))
        rm_temp_folder(temp_destination)
        return 0
    else:
        print("Error running the pudhnologic subdirectory.")
        print(output.stdout)
        print(output.stderr)
        rm_temp_folder(temp_destination)
        return 1

if __name__ == '__main__':
    main()