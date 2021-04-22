import codecs
from xml.sax import handler, make_parser
from time import strftime, localtime

# https://blog.csdn.net/weixin_43823859/article/details/85081619
paper_tag = ('article', 'inproceedings', 'proceedings', 'book',
             'incollection', 'phdthesis', 'mastersthesis', 'www')

# 打印当前时间
def printTime():
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    return

class mHandler(handler.ContentHandler):
    def __init__(self, result):
        self.result = result
        self.flag = 0

    def startDocument(self):
        print('Document Start')
        printTime()

    def endDocument(self):
        print('Document End')
        printTime()

    def startElement(self, name, attrs):
        if name == 'author':
            self.flag = 1

    def endElement(self, name):
        if name == 'author':
            self.result.write(',')
            self.flag = 0
        if (name in paper_tag):
            self.result.write('\r\n')

    def characters(self, chrs):  # [8]
        if self.flag:
            self.result.write(chrs)

def parserDblpXml(source, result):
    handler = mHandler(result)
    parser = make_parser()
    parser.setContentHandler(handler)

    parser.parse(source)

if __name__ == '__main__':
    source = codecs.open('data/dblp.xml', 'r', 'utf-8')
    result = codecs.open('data/authors.txt', 'w', 'utf-8')
    parserDblpXml(source, result)
    result.close()
    source.close()