# Scraping MyAnimeList with Scrapy

This project aims to develop my skills on web scraping using Scrapy. The target website is [MyAnimeList](https://myanimelist.net/), a popular website for anime and manga fans. The goal is to create a comprehensive dataset of anime and manga titles, including their details such as genre, score, and number of members.

## Usage

To scrape the top anime titles, run the following command:

```bash
cd myanimelist
scrapy crawl -O output.json topanime
```
