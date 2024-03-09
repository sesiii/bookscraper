## Install and activate python virtual environment
source venv/bin/activate

## Install required python modules
Once the required python modules are installed you should be able to view/run the Python Scrapy Spider with the following command (from within the project folder):

Cd into the project spiders: cd bookscraper

View the project spiders: scrapy list

Run the project spider: scrapy crawl bookspider


## Helpful Dubugging
f you have issues running the pip install -r requirements.txt command this can be due to some things not being up to date on your computer.

Running the following may solve some of these issues:

pip install --upgrade pip
