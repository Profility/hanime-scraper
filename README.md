# H-Anime Scraper
A simple hanime.tv scraper that scrapes release information using BeautifulSoup4.

## Getting Started

### Prerequisites

Before we start, we need to install some modules first. You will need to install the following:
* [bs4](https://pypi.org/project/bs4/) - `pip install bs4`
* [requests](https://pypi.org/project/requests/) - `pip install requests` (already pre-installed)

### Usage

#### Code:
The code below imports `hanime.py` and uses the `info` function to print out a dictionary.
```python
import hanime
print(hanime.info("https://hanime.tv/videos/hentai/lovely-heart-2"))
```
#### Output:
```python
{
  'brand': 'Mary Jane'
  'branduploads': '118'
  'releasedate': 'February 6, 2020',
  'uploaddate': 'February 11, 2020',
  'views': '3,669,440 views',
  'censored': True,
  'alternatetitles': ['Lovely Heart', 'らぶりー♡', '러블리 하트', 'Lovely', 'Lovely ♡', 'Lovely Heart']
}
```
