from mutagen.mp4 import MP4
from pytubefix import Playlist
import os
import sys
import shutil


def update_m4a_tags(path, track_number, total_tracks, album, artist, title):
    
    audio = MP4(path)

    # Delete all previous tags.
    # To-do: Let the user choose whether they'd like to do this or not.
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
    tags["\xa9alb"] = album
    tags["\xa9ART"] = artist
    tags["\xa9nam"] = title

    tags.save(path)

def main():
    if len(sys.argv) != 3:
        print("Usage: py grabmp3playlist.py playlist_link destination")
        return
    
    link = sys.argv[1]
    destination = (sys.argv[2]).replace(" ", "_")
    playlist = Playlist(link.strip())
    track_number = 0
    total_tracks = len(playlist)

    artist = input("Who is the artist/group for this album? ")
    album = input("What is the name of the album? ")

    temp_destination = destination + "_temp"

    for video in playlist.videos:

        # incrememnt track number
        track_number += 1

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
    # The codec at this point is AAC 0 kbps but should be AAC 256 kbps
    system_command = "node ./podhnologic/index.js --input " + temp_destination + " --output " + destination + " --codec aac"
    os.system(system_command)

    # line to delete temp folder
    try:
        shutil.rmtree(temp_destination)
    except:
        print("Temp directory could not be removed.\nThere is no danger if you delete it on your own. Those audio files will not play on your PSP (at least not mine).")

if __name__ == '__main__':
    main()