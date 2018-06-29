import hou
import os
import re

# from hutil.Qt import QtWidgets
from PySide2 import QtWidgets, QtUiTools

new_suffix_format = '_001'
regex = re.compile('(.*?)(\d+)(\.\w+)')

class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()
        # Houdini Style
        self.setStyleSheet(hou.qt.styleSheet())
        self.setProperty("houdiniStyle", True)

        self.proj = hou.getenv('JOB') + "/"
        self.projpathname = ""

        # Load UI File
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load('C:/Users/haruyasu/Documents/houdini16.0/scripts/python/projman/projman_tab.ui')

        # get UI elements
        # Tab 1
        self.setproj = self.ui.findChild(QtWidgets.QPushButton, "setproj_2")
        self.newproj = self.ui.findChild(QtWidgets.QPushButton, "newproj_2")
        self.newscene = self.ui.findChild(QtWidgets.QPushButton, "newscene_2")
        self.incsave = self.ui.findChild(QtWidgets.QPushButton, "incsave_2")
        self.reflist = self.ui.findChild(QtWidgets.QPushButton, "reflist_2")
        self.projpath = self.ui.findChild(QtWidgets.QLabel, "projpath_2")
        self.projname = self.ui.findChild(QtWidgets.QLabel, "projname_2")
        self.scenelist = self.ui.findChild(QtWidgets.QListWidget, "scenelist_2")

        # Tab 2

        # Tab 3
        self.refbtn1 = self.ui.findChild(QtWidgets.QPushButton, "btn1")
        self.refbtn2 = self.ui.findChild(QtWidgets.QPushButton, "btn2")
        self.refbtn3 = self.ui.findChild(QtWidgets.QPushButton, "btn3")
        self.refbtn4 = self.ui.findChild(QtWidgets.QPushButton, "btn4")
        self.refbtn5 = self.ui.findChild(QtWidgets.QPushButton, "btn5")

        # create widgets
        # self.btn = QtWidgets.QPushButton("Click ME")
        # self.lblTitle = QtWidgets.QLabel("PROJECT MANAGER")
        # self.label = QtWidgets.QLabel(self.proj)
        # self.listwidget = QtWidgets.QListWidget()

        # create connections
        # Tab 1
        self.setproj.clicked.connect(self.setProject)
        self.newproj.clicked.connect(self.newProject)
        self.newscene.clicked.connect(self.newScene)
        self.incsave.clicked.connect(self.incSave)
        self.reflist.clicked.connect(self.refList)

        # Tab 2

        # Tab 3
        self.refbtn1.clicked.connect(self.refBtn1)
        # self.refbtn2.clicked.connect(self.refBtn2)
        # self.refbtn3.clicked.connect(self.refBtn3)
        # self.refbtn4.clicked.connect(self.refBtn4)
        # self.refbtn5.clicked.connect(self.refBtn5)


        # layout
        mainLayout = QtWidgets.QVBoxLayout()

        mainLayout.addWidget(self.ui)

        # Add widgets to layout
        # mainLayout.addWidget(self.lblTitle)
        # mainLayout.addWidget(self.label)
        # mainLayout.addWidget(self.listwidget)
        # mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)

    # Tab 1
    def setProject(self):
        try:
            setjob = hou.ui.selectFile(title="Set Project", file_type=hou.fileType.Directory)

            li = setjob.split("/")
            # print li
            if li[-1] == li[-2]:
                setjob = "/".join(li[:-1]) + "/"

            hou.hscript("setenv JOB=" + setjob)

            # self.proj = hou.getenv('JOB') + '/'
            self.proj = hou.getenv('JOB')

            projname = setjob.split('/')[-2]
            setjob = os.path.dirname(setjob)
            projpath = os.path.split(setjob)[0]

            self.projpathname = projpath

            self.projname.setText(projname)
            self.projpath.setText(projpath + '/')

            self.createInterface()
        except:
            pass

    def newProject(self):
        if self.projpathname != "":
            input_name = hou.ui.readInput("Input File Name", buttons=('OK','Cancel'), title="Project Name")
            if input_name[0] == 0:
                dir_path = self.projpathname + "/" + input_name[1]
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)

                self.projname.setText(input_name[1])
                self.scenelist.clear()

    def newScene(self):
        hou.hipFile.clear()

        if not hou.node('/obj/work'):
            geo = hou.node('/obj/').createNode('geo', 'work')
            geo.moveToGoodPosition()

            for n in geo.children():
                n.destroy()

    def incSave(self):
        hip = hou.hipFile
        filename = hip.path()
        match = regex.match(filename)

        if match:
            filename, number, ext = match.groups()
            filename += str(int(number) + 1).rjust(len(number), '0') + ext
        else:
            filename, ext = os.path.splitext(filename)
            filename += new_suffix_format + ext

        if os.path.isfile(filename):
            overwrite = hou.ui.displayConfirmation(
                'The file "{}" already exists. Do you want to overwrite it?'
                    .format(filename))
            if not overwrite:
                return

        hip.save(filename)

    def refList(self):
        self.scenelist.clear()

        for file in os.listdir(self.proj):
            if file.endswith(".hip") or file.endswith(".hipnc"):
                self.scenelist.addItem(file)

    def openScene(self, item):
        hipFile = self.proj + item.data()
        hou.hipFile.load(hipFile)

    def createInterface(self):
        self.scenelist.clear()

        for file in os.listdir(self.proj):
            if file.endswith(".hip") or file.endswith(".hipnc"):
                self.scenelist.addItem(file)

        self.scenelist.doubleClicked.connect(self.openScene)

    # Tab 2

    # Tab 3
    def refBtn1(self):
        sticky = hou.node("/obj").createStickyNote()
        sticky.setText("import hou\n"
                       "geo = hou.node('/obj').createNode('geo', 'sphere',0)\n"
                       "geo.createNode('sphere')")

