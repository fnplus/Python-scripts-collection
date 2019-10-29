
import urllib.request

def download(tutorialName):
    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    downloadLocation = '<location>'

    pdf = urllib.request.urlopen(url)
    saveFile = open(downloadLocation + tutorialName +  '.pdf', 'wb')
    saveFile.write(pdf.read())
    saveFile.close()

if __name__ == '__main__':
    tutorialName = input('Name of the pdf to be downloaded: ')
    download(tutorialName)