import webbrowser, time

vid_codes = []
with open("fresh_links.txt", "r") as f:
    links = f.read().splitlines()
    for line in links:
        vid_codes.append(line.split("/")[-1])

i = 0
for code in vid_codes:
    if i < 50:
        i += 1
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=" + code)
    else:
        wait = input("Press Enter to continue...")
        i = 0
