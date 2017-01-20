from HTMLParser import HTMLParser
import re
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
parser = MyHTMLParser()
texts = str()
for _ in range(int(raw_input().strip())):
    texts += raw_input()
texts = re.sub(r"\<\!--.*?--\>", "", texts)
parser.feed(texts)