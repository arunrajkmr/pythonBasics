# to check the file exists using luigi
# run with a custom command
# python luigiImageContent.py FileImageContent --local-scheduler --fileName macbookResultPage.txt

import luigi
from bs4 import BeautifulSoup
 
class FileImageContent(luigi.Task):
    fileName = luigi.Parameter()
    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("maccontent.txt")

    def run(self):
        soup = BeautifulSoup (open(self.fileName), features="lxml")
        links = soup.find_all('a')
        with self.output().open('w') as fout :
            for link in links:
                names = link.contents[0]
                fullLink = link.get('href')
                fout.write("Contect:{}, link:{}\n".format(names, fullLink))

if __name__ == '__main__':
    luigi.run()