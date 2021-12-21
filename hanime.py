from bs4 import BeautifulSoup
import requests

base_url = "https://hanime.tv"

"""
def check(url: str):
    if url.startswith("https://hanime.tv"):
        status = requests.get(url).status_code
        if status == 200:
            pass
        elif status == 404:
            raise Exception("URL returned 404, please check network connection.")
    else:
        raise Exception("URL Parameter may be invalid, please verify.")
"""


def info(url: str) -> dict:
    """
    Returns a dictionary with the amount of brand uploads, views, date of release and upload.

    Output (example):
    {
        'brand': 'Mary Jane'
        'branduploads': '118'
        'releasedate': 'February 6, 2020',
        'uploaddate': 'February 11, 2020',
        'views', '3,669,440 views',
        'censored' True
        'alternatetitles': ['Lovely Heart', 'らぶりー♡', '러블리 하트', 'Lovely', 'Lovely ♡', 'Lovely Heart']
    }
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    info = soup.find_all('div', attrs=['class', 'hvpimbc-text grey--text'])
    brand = soup.find('a', attrs=['class', 'hvpimbc-text'])
    branduploads = None
    releasedate = None
    uploaddate = None
    alternatetitles = []
    views = soup.find('div', attrs=['class', 'tv-views grey--text']).text
    censorship = soup.find('a', attrs=['class', 'hvpimbc-censorship-btn'])
    status = bool
    if censorship.text == "CENSORED":
        status = True
    else:
        status = False

    for alttitle in soup.find_all('span', attrs=['class', 'mr-3 grey--text']):
        alternatetitles.append(alttitle.text)

    for count, info in enumerate(info):
        if count == 0:
            branduploads = info.text
        if count == 1:
            releasedate = info.text
        if count == 2:
            uploaddate = info.text
        if count == 3:
            break

    return {
        'brand': brand.text,
        'branduploads': branduploads,
        'releasedate': releasedate,
        'uploaddate': uploaddate,
        'views': views,
        'censored': status,
        'alternatetitles': alternatetitles
    }

def description(url: str) -> str:
    """
    Returns a string with the description

    Output (example):
    A sudden rainstorm forced them to take shelter in a nearby gym building. Although it was only for a little bit he still felt awkward sitting next to her, as she was soaked and he could see through her clothes...After trying his best to get any kind of reaction from her it escalated to the point where she was on her back and completely undressed... ready and waiting for him.
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    description = soup.find('div', attrs=['class', 'mt-3 mb-0 hvpist-description'])
    fulldesc = []

    for desc in description.findChildren():
        f1 = str(desc).replace('<p>', '')
        f2 = f1.replace('</p>', '')
        fulldesc.append(f2)

    return ''.join(fulldesc)

def thumbnail(url: str) -> str:
    """
    Returns a string with the thumbnail URL

    Output (example):
    https://git-covers.pages.dev/images/lovely-heart-2-cv1.png
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    cover = soup.find('img', attrs=['class', 'hvpi-cover'])
    return cover['src']

def download(url: str) -> str:
    """
    Returns a string with the download URL

    Output (example):
    https://hanime.tv/downloads/bG92ZWx5LWhlYXJ0LTI=
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    download = soup.find('a', attrs=['class', 'hvpab-btn flex align-center primary-color-hover'])
    return base_url + download['href']

def tags(url: str) -> list:
    """
    Returns a list with all the tags

    Output (example):
    ['school girl', 'creampie', 'pov', 'vanilla', 'x-ray', 'censored', 'hd', 'toys']
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    tags = soup.find('div', attrs=['class', 'hvpis-text grey--text text--lighten-1']).findChildren("a")
    fulltags = []

    for tag in tags:
        fulltags.append(tag['href'].replace('/browse/tags/', ''))

    return fulltags