# Autonomous-Drone-based-on-Facial-Recognition-and-Tracking

<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email
-->
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project
With the escalation of Deep Learning and Computer Vision, comes forth the ability to develop better autonomous vehicles. One such potential vehicular means is Drones. It's application ranges from surveillance, delivery, precision agriculture, weather forecasting, etc. This project has one such application.

Embedded with Python-based Convolutional Neural Network for Face Recognition and Tracking, the application gives autonomous flight abilities to the Drone. There are two modes: Manual and Autonomous mode. 
Additional Features included are Normal, Sports, and Berserk mode for Faster Flight Speeds, Flips(Forward, Backward, Left and Right), Patrolling and Live Video Streaming, and autonomous Snapshots. 
The Drones supported for my project are DJI Tello and Tello Edu. Both of these drones have several fascinating features which makes it the perfect candidate for the drone. Such as:
* Affordability
* Relatively Smaller Size
* Programmable with Python and Swift
* Embedded Camera
* Intel Processor for stable flight and turbulence reduction

![DJI Tello and Tello EDU](https://1.bp.blogspot.com/-uh6ayIHEvvc/Xs2aRHWty2I/AAAAAAAAAa0/IJNhe2XVxu0jkveAf7n_CYkjrmoxQq5vACK4BGAsYHg/IMG_1025.jpg)

fig 2. DJI Tello (on the right) and DJI Tello Edu (on the left)

NOTE: The Entire project methodolgy can be found in my portfolio here: https://akbexpo.blogspot.com/2020/05/autonomous-drone-with-face-tracking.html

So the drone uses a Facial Recongnition and Tracking algorithm, leveraging the Haar-Cascade xml file, embedded with OpenCV 4.0. It looks something like this:

![Graph Grid](https://1.bp.blogspot.com/-NK7wm-F79Tw/Xs2_peCMcFI/AAAAAAAAAdQ/A62LF7tZHgg5iDCVt5RgwRDSCkDEM32IgCK4BGAsYHg/DJI%2BFace%2BTracking.png)
and 
![Back-end](https://1.bp.blogspot.com/--kx-CM1qGdo/Xs2p8gZu2WI/AAAAAAAAAcg/XZ8tR_zIE4Ukm9P3c38LYpHGJQ5aXe6mwCK4BGAsYHg/s320/Face%2BTracking%2BBackground.gif)

### Results

* Take-off: 
![Launch](https://drive.google.com/file/d/1q1Ct_qJmBsVYRbxRuFKV-sfnvwUfxeaO/view?usp=sharing)
* Following to the Right :
![Right](https://drive.google.com/file/d/1G91mjWlO7OJNwInVoWx1EXlkLVT9OlXr/view?usp=sharing)
* Following to the Left :
![Left](https://drive.google.com/file/d/1BEJsWOPNdVgvIyK3EBY1hqmoVewKIx9X/view?usp=sharing)

### Built Using the following:

* []() Python 3.7
* []() Python Libraries: OpenCV 4, PyDrone, FFMPEG, Sys, time, Thread, logging, numpy
* []() Flask Web-framework for Python
* []() Haar-Cascade-xml file for Facial Recognition
* []() DJI-Tello or DJI-Tello Edu


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
```sh
git clone https://github.com/Akbonline/Autonomous-Drone-based-on-Facial-Recognition-and-Tracking.git
```
2. Installing all the requirements
```sh
pip install -r requirements.txt
```
3. Running the Application
For running the application, just hook-up teh main.py with PyCharm IDE or use the following command in the directory that has main.py file: 
```sh
python main.py
```
And press the local IP Address that you see in the Output, to launch the Remote Controller UI.

<!-- CONTRIBUTING -->
## Contributing

Feel Free to contact me at akshatbajpai.biz@gmail.com (Or just comment on my blogpost at: https://akbexpo.blogspot.com/2020/05/data-structures-and-algorithms.html) for any kind of comments, feedback, queries, explanations, critics, etc. Do checkout my other projects at http://akbexpo.blogspot.com/ I would love to hear from y'all!

## TODO:
* Improve the video streaming Pipeline's Latency issue
* Add a Drone Battery Indicator and Emergency Landing Mechanism
* Implement Pose Estimation based Drone Control


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



## TODO:
* Improve the Latency: Packaging through pyinstaller is kinda sucky...
* Make a better OOP model
* Fix Switching Issues
* Adding more algorithms to it: Binary & Linear Search/ Sorting Algorithms

## Author

* **Akshat Bajpai** - [Akbonline](https://github.com/Akbonline)
* **Email** - akshatbajpai.biz@gmail.com
* **Portfolio** - http://akbexpo.blogspot.com/
* **LinkedIn** - https://www.linkedin.com/in/akshat-bajpai-09/


## Acknowledgments

* To my Parents and Guardians for bringing me to planet Earth
* To all the amazing opensource library contributers, who have a huge hand in driving the technology innovation force forward
* Almighty Google and Lord Quora, Stackoverflow and Reddit
* I would also like to thank the awesome developers of the online video editors: EZGif and Kapwing. 



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=flat-square
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=flat-square
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=flat-square
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=flat-square
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: images/screenshot.png
