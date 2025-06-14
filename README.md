<a id="readme-top"></a>

<!-- PROJECT LOGO -->
  
<div align="center">

<h1 align="center"> YTtoPSP </h1>


A project which allows the user to download audio from YouTube videos in a format playable on PSP, sorted by track number, which includes user inputted metadata.

Audio downloaded from YouTube is of the M4A filetype. The PSP is able to play (among other file types) M4A with the codec AAC 266kbps and sampling frequency 44.100 kHz. So, this is what I have chosen for this project.


</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li> <a href="#PlaylisTtoM4A"> PlaylistToM4A.py </a> 
      <ul>
        <li><a href="#usage-playlisttom4a">Usage</a></li>
        <li><a href="#examples-playlisttom4a">Examples</a></li>
      </ul>
    </li>
    <li> <a href="#TrackToM4A"> TrackToM4A.py </a> 
      <ul>
        <li><a href="#usage-tracktom4a">Usage</a></li>
        <li><a href="#examples-tracktom4a">Examples</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



### Built With

[![Python][python-img]][python-url]
  
  
[![Mutagen][mutagen-img]][mutagen-link]
[![PyTube][pytubefix-img]][pytubefix-link]
  
Submodule created by <a href="https://github.com/jmonster">jmonster</a>:
  
[![podhnologic][podhnologic-img]][podhnologic-link]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This project is built in Python and uses a submodule (someone else's free to use project, credits to jmonster) in Javascript. So you will need Python 3 and Node.js in order to use this project.

But don't worry! If you have limited coding experience, it's not too complicated to get running.

Be warned, at this stage I haven't tested this project on Mac or Linux. This is because I'm just one person and don't have access to those! So proceed with caution, try to setup the project, and report any issues either through GitHub or just by emailing me (darcy.mazloum@gmail.com).

Let's get started then.

### Prerequisites

1. Python 3
* You will need to have Python 3 downloaded on your computer. There are many installation guides including the one at python.org so if you have no coding experience, this is a great place to start getting familiar with Python and your computer. And make sure to add it to path (environement variables) when downloading!  
  
* <a href="https://www.python.org/downloads/"> Download Python here. </a>  
* <a href="https://www.digitalocean.com/community/tutorials/install-python-windows-10"> Python Windows download guide </a> 
* <a href="https://www.dataquest.io/blog/installing-python-on-mac/"> Python Mac download guide </a>
  
2. Nodejs
* Nodejs is another really useful tool that you will have to download. Go to the download guide below to get started downloading it and make sure to add it to path!  
  
* <a href="https://nodejs.org/en/download"> Download NodeJS here. </a>  
* <a href="https://www.digitalocean.com/community/tutorials/node-js-environment-setup-node-js-installation"> Nodejs download guide, both Windows and Mac </a>  
  
3. ffmpeg
* ffmpeg is a collaborative project that allows users to handle the conversion of music. The submodule uses it, so you'll need it! The following tutorial shows how you can download it on Windows and add it to path. Although it uses Windows 10 in the tutorial, the same process will work on Windows 11.  
  
* <a href="https://phoenixnap.com/kb/ffmpeg-windows"> ffmpeg windows download guide </a>  
* <a href="https://phoenixnap.com/kb/ffmpeg-mac"> ffmpeg mac download guide </a>
  
4. Git
* And of course, you will need Git installed on your computer to download the project. Below is the link to a download guide of Git Bash and how to add it to your enviornment variables so that you can use git commands in any terminal on your computer.  
  
* <a href="https://www.w3schools.com/git/git_install.asp?remote=github"> Git Bash download guide </a>  

### Installation

1. Clone the repo
* Create a workspace in your computer where you can have your local coding projects. Open that folder in the terminal, in VSCode, or whatever IDE you use for Python and type this command into the terminal.

* It is critical that you have the recursive tag so that the submodule can be downloaded.

   ```sh
   git clone --recursive https://github.com/darcyMaz/YTtoPSP
   ```

2. Create the Python environment for this project.
* Creating your Python environment can be done in different ways. I link two guides below, one that does it via the terminal and one that does it from VSCode. If you want or need to do it a different way, there are plenty of guides to choose from on the internet.  
* <a href="https://www.w3schools.com/python/python_virtualenv.asp"> Python Environment: Terminal </a>  
* <a href="https://code.visualstudio.com/docs/python/environments"> Python Environment: VSCode </a>  
  

3. Install packages for the podhnologic submodule.
* The submodule needs to have some packages installed. Go to the terminal, change directories to podhnologic, then type the line below. That's it! Then change directories back to YTtoPSP.  
    ```sh
    npm install
    ```
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>  


# PlaylistToM4A

### Track Number Note

* Tracks are numbered by their position in the playlist. They are given track numbers in the metadata and numbers at the start of their song titles.

### Usage PlaylistToM4A

usage: PlaylistToM4A.py [-h] [-lk YTLINK] [-dt DESTINATION] [-ar ARTIST] [-al ALBUM] [-ex EXCLUDE_LIST]

options:
  -h, --help            show this help message and exit
  -lk, --ytlink YTLINK  YouTube Playlist Link
  -dt, --destination DESTINATION
                        Destination Folder
  -ar, --artist ARTIST  Artist. The individual, group, band, etc.
  -al, --album ALBUM    Title of the album.
  -ex, --exclude_list EXCLUDE_LIST
                        List of integers of any songs you would like to exclude from being downloaded. Useful for playlists that include an extra video that     
                        includes every song.

### Examples PlaylistToM4a

This example runs PlaylistToM4A.py which downloads the audio from a whole copyright free lofi beats playlist into a folder on user1's computer.
* ```sh
    & "C:/path_to_folder/YTtoPSP/.venv/Scripts/python.exe" "C:path_to_folder/YTtoPSP/PlaylistToM4A.py" -lk "https://www.youtube.com/watch?v=BH-SnQ8J1VU&list=PLfP6i5T0-DkIMLNRwmJpRBs4PJvxfgwBg" -dt "C:/.../Music/Lofi_No_Copyright"
  ```

This example runs PlaylistToM4A.py which downloads an album and adds as metadata, the album and artist, to each song.
* ```sh
    & "C:/path_to_folder/YTtoPSP/.venv/Scripts/python.exe" "C:path_to_folder/YTtoPSP/PlaylistToM4A.py" -lk "https://www.youtube.com/watch?v=-JhdxgV99Mc&list=PL0FzNhLuNz_VKTfiKrOUL5jsCE_5WBK7J" -dt "C:/.../Music/Duke Ellington Greatest Hits" -ar "Duke Ellington" -al "Duke Elington Greatest Hits"
  ```

This example runs PlayListToM4A.py which downloads an album, adds artist as metadata, and excludes a few songs based on the exclusion list.
* ```sh
    & "C:/path_to_folder/YTtoPSP/.venv/Scripts/python.exe" "C:/path_to_folder/YTtoPSP/PlaylistToM4A.py" -lk "https://www.youtube.com/watch?v=UPNUp9DwFR0&list=PL45A72A0B85AA8247&pp=0gcJCWMEOCosWNin" -dt "C:/.../Music/Beethoven" -ar "Beethoven" -ex "[3,12,30]"
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

# TrackToM4A.py

Downloads the audio from a single YouTube video to the destination folder. Metadata can also be added to the file.

### Usage TrackToM4A

usage: TrackToM4A.py [-h] [-lk YTLINK] [-dt DESTINATION] [-tn TRACK_NUMBER] [-tt TRACK_TOTAL] [-ar ARTIST] [-al ALBUM]

options:
  -h, --help            show this help message and exit
  -lk, --ytlink YTLINK  YouTube Video Link.
  -dt, --destination DESTINATION
                        Destination Folder.
  -tn, --track_number TRACK_NUMBER
                        Track number in its respective playlist or album
  -tt, --track_total TRACK_TOTAL
                        Number of tracks in this album or a playlist
  -ar, --artist ARTIST  Artist. The individual, group, band, etc.
  -al, --album ALBUM    Title of the album.

### Examples TrackToM4A

This example runs TrackToM4A.py which downloads the audio from a public domain YouTube video and adds the artist's name and the title of the song into the metadata.
* ```sh
    & c:/path_to_folder/YTtoPSP/.venv/Scripts/python.exe c:/path_to_folder/YTtoPSP/TrackToM4A.py -lk "https://youtu.be/zCrtErmipXE" -dt "C:/.../Music" -ar "Bessie Smith"
  ```






<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

As this project has only been tested on Windows 11, testing on Linux and Mac would be greatly appreciated!

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Attribution-NonCommercial-ShareAlike 4.0 International. See `LICENSE.txt` for more information or the link below for a more concise explanation.  

Basically, you can use and remix this project with credit to the author, but you can't use it for commercial purposes.  

<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en"> View the concise explanation of the license here. </a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Darcy Mazloum - darcy.mazloum@gmail.com

Project Link: [https://github.com/darcyMaz/YTtoPSP](https://github.com/darcyMaz/YTtoPSP)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

jmonster's podhnologic project: [https://github.com/jmonster/podhnologic/tree/ba7279581ced07b4f9a55d6289fc605e8e9525ea](https://github.com/jmonster/podhnologic/tree/ba7279581ced07b4f9a55d6289fc605e8e9525ea)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[python-img]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://python.org
[mutagen-link]: https://pypi.org/project/mutagen/
[mutagen-img]: https://pypi-camo.freetls.fastly.net/b1c76ddde4aec66388fb18b99e7029731bbf1aec/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f71756f646c696265742f6d75746167656e2f6d61737465722f646f63732f696d616765732f6c6f676f2e737667
[pytubefix-link]: https://pypi.org/project/pytubefix
[pytubefix-img]: https://pypi-camo.freetls.fastly.net/42d43def1c8634a6c158def4846894bc2afd542b/68747470733a2f2f6173736574732e6e69636b666963616e6f2e636f6d2f67682d7079747562652e6d696e2e737667
[podhnologic-link]: https://github.com/jmonster/podhnologic/tree/ba7279581ced07b4f9a55d6289fc605e8e9525ea
[podhnologic-img]: https://private-user-images.githubusercontent.com/368767/352676369-a9383166-c1e6-432e-9658-9044b13725bc.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDk1ODgzODIsIm5iZiI6MTc0OTU4ODA4MiwicGF0aCI6Ii8zNjg3NjcvMzUyNjc2MzY5LWE5MzgzMTY2LWMxZTYtNDMyZS05NjU4LTkwNDRiMTM3MjViYy5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYxMFQyMDQxMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMGY2ZmVlZjk0ZTAyOTFhOWUyYzYwYzdhNGM2Zjc5NmU0ZjM4Mzg2YmU3MDBjNzg4NmIyZDlmOTY2OWQ3NTMxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.BTtwnMLHs9pV_L4SjlSiMjeoTLLtVLdcUyDs3Ys7oXA

