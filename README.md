# H-Anime Scraper
A simple hanime.tv scraper that scrapes release information using BeautifulSoup4.

## Getting Started

Run the `pip install -r requirements.txt` to install all the necessary dependencies

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
