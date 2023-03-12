## Idea
The lecture videos in Udvash Master Course are actually unlisted YouTube video that are embedded in their website. They also disabled right click. So opening dev tools > searching for "youtube.com/embed/" > then copying the value and opening new tab, and then open in youtube to actually work with the video is quite a hassle. Automate the same thing, <b> no optimization.</b>

## How this works
1. `courses.py` scrapps all the lecture links found in the Course and store them in a `.txt` file named "lecture_links.txt". And also prints the number of lectures found. You need cookies here.
2. `get_yt.py` automates your browser (in this case, "FireFox") and scrapps the embed links and Store them in "fresh_links.txt"
3. `open_yt.py` opens all the links in your default browser, 50 at a time, press any key on terminal to open next 50. Because Your PC may struggle to handle this many of links.

## Requirements:
##### PyPi:
```
pip install -U requests, beautifulsoup4, webbrowser, selenium
```
##### Software:
1. FireFox
