# to check the file exists using luigi
# run with a custom command
# python gitcommits.py GitCommitsCount --local-scheduler --fileName giturls.txt

import luigi
from bs4 import BeautifulSoup
import requests
import csv

 
class GitCommitsCount(luigi.Task):
    fileName = luigi.Parameter()
    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("gitcommits.csv")

    def run(self):
       with open(self.fileName, 'r') as fin, self.output().open('w') as fout:
            for line in fin:
                URL = str(line.strip())
                response = requests.get(URL)
                soup = BeautifulSoup(response.text, features="lxml")
                span = soup.find("span", attrs={'class': 'num text-emphasized'})
                print (span.text.strip().replace(',', ''))
                fout.write(span.text.strip().replace(',', ''))

if __name__ == '__main__':
    luigi.run()