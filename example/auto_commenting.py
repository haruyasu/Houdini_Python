import hou
import os
import zipfile

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/", os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')


def getHeader(path):
    path = path.replace("operator:", "").replace("object/", "obj/").split("?")[0]
    path = path.lower()
    nodeHelpContent = ARCHIVE.read(path+".txt")
    splitted = nodeHelpContent.split("\"\"\"")
    return splitted[1] if len(splitted) > 1 else "Not found"


def main(kwargs):
    node = kwargs["node"]
    if len(node.comment()) == 0:
        description = getHeader(node.type().defaultHelpUrl())
        node.setComment(description)
        node.setGenericFlag(hou.nodeFlag.DisplayComment, True)


main(kwargs)
