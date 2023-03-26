import re


def get_url(url):
    # We can make all lower since url is case insensitive
    url = url.lower()

    # Removing url tag
    url = re.sub("<url>", "", url)
    # Removing Prothocol part
    url = url.replace("https://", "").replace("http://", "")

    # define regular expression for allowed characters
    pattern = re.compile("[a-zA-Z0-9_./]+")
    # Check whether there is unwanted chars or not.
    url_bin = re.sub(pattern, "", url)
    if url_bin == "":
        return url
    else:
        return "not a valid url"
    return url


code = input("Please enter your 'Device Code': ")
# df is our database
try:
    url = df[df["Device_Code"] == code].Stats_Access_Link[0]
except KeyError:
    url = "NaN"  # Not a valid Device Code

get_url(url)