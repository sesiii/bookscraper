import subprocess

def run_scrapy():
    subprocess.Popen(". ./env/bin/activate && scrapy crawl bookscraper", shell=True, executable="/bin/bash")

if __name__ == "__main__":
    run_scrapy()