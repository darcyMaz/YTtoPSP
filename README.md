# YTtoPSP
A project which allows the user to download audio from YouTube videos in a format playable on PSP, sorted by track number, which includes neccesary metadata.

<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A project which allows the user to download audio from YouTube videos in a format playable on PSP, sorted by track number, which includes inputted metadata.

Here's a blank template to get started. To avoid retyping too much info, do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`, `project_license`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Node][nodejs.org]][Next-url]
* [![Python][python.org]][React-url]

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
  
<a href="https://www.python.org/downloads/"> Download Python here. </a>  
<a href="https://www.digitalocean.com/community/tutorials/install-python-windows-10"> Python download guide </a> 
  
2. Nodejs
* Nodejs is another really useful tool that you will have to download. Go to the download guide below to get started downloading it and make sure to add it to path!  
  
<a href="https://nodejs.org/en/download"> Download NodeJS here. </a>  
<a href="https://www.digitalocean.com/community/tutorials/node-js-environment-setup-node-js-installation"> Nodejs download guide </a>  
  
3. ffmpeg
* ffmpeg is a collaborative project that allows users to handle the conversion of music. The submodule uses it, so you'll need it! The following tutorial shows how you can download it on Windows and add it to path. Although it uses Windows 10 in the tutorial, the same process will work on Windows 11.  
  
<a href="https://phoenixnap.com/kb/ffmpeg-windows"> ffmpeg download guide </a>  
  
4. Git
* And of course, you will need Git installed on your computer to download the project. Below is the link to a download guide of Git Bash and how to add it to your enviornment variables so that you can use git commands in any terminal on your computer.  
  
<a href="https://www.w3schools.com/git/git_install.asp?remote=github"> Git Bash download guide </a>  

### Installation

1. Clone the repo
* Create a workspace in your computer where you can have your local coding projects. Open that folder in the terminal, in VSCode, or whatever IDE you use for Python and type this command into the terminal.

It is critical that you have the recursive tag so that the submodule can be downloaded.

   ```sh
   git clone --recursive https://github.com/darcyMaz/YTtoPSP
   ```

2. A) Create the Python environment for this project.
* Creating your Python environment can be done in different ways. I link two guides below, one that does it via the terminal and one that does it from VSCode. If you want or need to do it a different way, there are plenty of guides to choose from on the internet.  
<a href="https://www.w3schools.com/python/python_virtualenv.asp"> Python Environment: Terminal </a>  
<a href="https://code.visualstudio.com/docs/python/environments"> Python Environment: VSCode </a>  
  
2. B) Use the global environment.
* You don't need to create an environment for your project, especially since this project has only two packages (for now). What you would do instead is, after cloning the repo, type these two commands into the terminal. You will have the packages in the global environment from now on.
    ```sh
    pip install mutagen
    pip install pytubefix
    ```

3. Install packages for the podhnologic submodule.
* The submodule needs to have some packages installed. Go to the terminal, change directories to podhnologic, then type npm install. That's it! Then change directories back to YTtoPSP.  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>  



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

As this project has only been tested on Windows 11, testing on Linux and Mac would be greatly appreciated!

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Attribution-NonCommercial-ShareAlike 4.0 International. See `LICENSE.txt` for more information or the link below for a more concise explanation.

<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Darcy Mazloum - darcy.mazloum@gmail.com

Project Link: [https://github.com/darcyMaz/YTtoPSP](https://github.com/darcyMaz/YTtoPSP)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

jmonster's podhnologic project for a conversion to the correct frequency for the M4A files: [https://github.com/jmonster/podhnologic/tree/ba7279581ced07b4f9a55d6289fc605e8e9525ea](https://github.com/jmonster/podhnologic/tree/ba7279581ced07b4f9a55d6289fc605e8e9525ea)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 