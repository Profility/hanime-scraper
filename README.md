# H-Anime Scraper
A simple hanime.tv scraper using BeautifulSoup4

Note: Please put a ratelimit to all of the HTTP Requests to prevent getting banned from accessing the hanime.tv website, just in case.

## Getting Started

### Prerequisites

You need these modules:

* [bs4](https://pypi.org/project/bs4/)
* [requests](https://pypi.org/project/requests/)

## Usage

Code:
```python
import hanime
print(hanime.info("https://hanime.tv/videos/hentai/lovely-heart-2"))
```

Output:
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
