import pyshorteners
url = input("enter the url: ")

def shortenurl(url):
    x = pyshorteners.Shortener()
    print(x.tinyurl.short(url))
shortenurl(url)
