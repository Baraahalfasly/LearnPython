import re

def youtube_id(url):
    # Define a regular expression to capture the video ID
    pattern = r"(?:v=|\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# Test cases
print(youtube_id("https://www.youtube.com/watch?v=XPEr1cArWRg"))  # ➞ "XPEr1cArWRg"
print(youtube_id("https://youtu.be/BCDEDi5gDPo"))                 # ➞ "BCDEDi5gDPo"
print(youtube_id("https://youtube.com/watch?t=4m40s&v=vxP3bY-XxY4"))  # ➞ "vxP3bY-XxY4"
