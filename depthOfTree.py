import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):

    global maxdepth
    level=level+1
    maxdepth=max(maxdepth,level)

    for child in elem:
        depth(child,level)
    return maxdepth

if __name__ == '__main__':
    n = int(raw_input())
    xml = ""
    for i in range(n):
        xml =  xml + raw_input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth
