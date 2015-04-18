#!/bin/python

from tree import Tree

#def compile(source):

def parseTags(src):
    out = []
    tagStart = src.find('<')
    if(tagStart > 0):
        out.append(src[:tagStart])
    elif(tagStart < 0):
        out.append(src)
    matchingTagEnd = 0
    while(src.find('<', matchingTagEnd) > -1):
        tagStart = src.find('<', matchingTagEnd)
        tagEnd = src.find('>', tagStart)
        elementEnd = src.find(' ', tagStart)
        elementEnd = min(elementEnd, tagEnd) if elementEnd > -1 else tagEnd
        tagElement = src[tagStart+1:elementEnd]
        matchingTag = src.find('</' + tagElement, tagEnd)
        matchingTagEnd = src.find('>', matchingTag)
        end = src.find('<', matchingTagEnd)
        end = len(src) if end < 0 else end
        contents = src[tagEnd+1:matchingTag]
        out.append((tagElement, parseTags(contents)))
        if(end > matchingTagEnd+1):
            out.append(src[matchingTagEnd+1:end])
    return out


print parseTags('h<u>a<b>b</b></u>i')


"""
this program does cool stuff
<p>
    hello <b>world!</b><u>talking</u>
</p>




"""
