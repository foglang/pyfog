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
        matchingTag = findMatchingTag(src, tagEnd)
        matchingTagEnd = src.find('>', matchingTag)
        end = src.find('<', matchingTagEnd)
        end = len(src) if end < 0 else end
        contents = src[tagEnd+1:matchingTag]
        out.append((tagElement, parseTags(contents)))
        if(end > matchingTagEnd+1):
            out.append(src[matchingTagEnd+1:end])
    return out

def findMatchingTag(src, index):
    depth = 0
    for i in range(index, len(src)):
        if(src[i] == '<'):
            if(src[i+1] == '/'):
                if(depth == 0):
                    return i
                depth -= 1
            else:
                depth += 1
    return -1

fog_program = """
This is a fog program that prints out the name of the program...
<u>I am <b>program</b></u>
and then the version number
<u>version <b>version number</b></u>
"""

print parseTags(nested_same_tags)
