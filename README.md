# Boston Startup Scraper

Ty-Lucas Kelley

---

Gets data from Boston Startups Guide and throws it in a CSV file.
Right now, it only grabs the name, web address, and industry of the company

$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ rm info.csv && touch info.csv
$ scrapy crawl scraper

It'll get better when I have time to work on it more!
