from mutagen.mp4 import MP4
from pytubefix import YouTube
import subprocess
import argparse
import shutil

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

def rm_temp_folder(temp_folder_path):
    try:
        shutil.rmtree(temp_folder_path)
    except:
        print("Temp directory could not be removed.\nThere is no danger if you delete it on your own. The audio file in this folder won't play on your PSP (at least not mine) but they still work.")


def main():
    
    parser = argparse.ArgumentParser()

    # -link LINK -dest DESTINATION -arti ARTIST -albu ALBUM -exls EXLUDE_LIST
    parser.add_argument("-lk", "--ytlink", help="YouTube Video Link.")
    parser.add_argument("-dt", "--destination", help="Destination Folder.")
    parser.add_argument("-tn", "--track_number", help="Track number in its respective playlist or album")
    parser.add_argument("-tt", "--track_total", help="Number of tracks in this album or a playlist")
    parser.add_argument("-ar", "--artist", help="Artist. The individual, group, band, etc.")
    parser.add_argument("-al", "--album", help="Title of the album.")

    args = parser.parse_args()

    if args.ytlink==None or args.destination == None:
        parser.print_usage()
        print("The YouTube Link and the Destination folder are required arguments.")
        return 1

    link = args.ytlink
    video = YouTube(link.strip())

    # If there is an error here, then the 
    try:
        len(link)
    except:
        print("The playlist link is in the wrong format or it cannot find a playlist at the link.")
        return 1
    
    destination = args.destination

    # If these arguments are not given then set them to the empty string.
    if args.artist == None:
        artist = ""
    else:
        artist = args.artist
    
    if args.album == None:
        album = ""
    else:
        album = args.album

    # These values, in addition, must be of type int.
    if args.track_number == None:
        track_number = 0
    else:
        try:
            track_number = int(args.track_number)
        except ValueError:
            print("Track number has an invalid input. It must be an integer.")
            return 1

    if args.track_total == None:
        track_total = 0
    else:
        try:
            track_total = int(args.track_total)
        except ValueError:
            print("Total tracks has an invalid input. It must be an integer.")
            return 1

    temp_destination = destination + "_temp"

    # extract only audio
    audio = video.streams.filter(only_audio=True).first()

    # download the file
    out_file = audio.download(output_path=temp_destination)

    # update m4a tags
    update_m4a_tags(path=out_file, track_tuple=(track_number, track_total), album=album, artist=artist, title=video.title)  

    sys_command_list = ['node', './podhnologic/index.js', '--input', temp_destination, '--output', destination, '--codec', 'aac']
    output = subprocess.run(sys_command_list, capture_output=True)

    if output.returncode == 0:
        print("Track created successfully in the destination folder {}".format(destination))
        rm_temp_folder(temp_destination)
        return 0
    else:
        print("Error running the pudhnologic subdirectory.")
        print(output.stdout)
        print(output.stderr)
        rm_temp_folder(temp_destination)
        return 1
    

if __name__ == "__main__":
    main()