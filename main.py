from PyQt5 import QtCore
from PyQt5.QtCore import QMetaObject
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QMenu, QMenuBar, QWidget, QToolBar, QAction, QApplication, QMainWindow, QActionGroup, \
    QFileSystemModel, QTreeView, QGridLayout, QHBoxLayout, QLabel, QComboBox, QSizePolicy, QToolButton, QFrame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(600, 400)
        icon = QIcon()
        icon.addPixmap(QPixmap("icon.png"), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menuFiles = QMenu(self.menubar)
        self.menuMark = QMenu(self.menubar)
        self.menuCommands = QMenu(self.menubar)
        self.menuNet = QMenu(self.menubar)
        self.menuShow = QMenu(self.menubar)
        self.menuConfiguration = QMenu(self.menubar)
        self.menuStart = QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.helpMenuBar = QMenuBar(self.menubar)
        self.menuHelp = QMenu(self.helpMenuBar)
        self.helpMenuBar.addMenu(self.menuHelp)
        self.menubar.setCornerWidget(self.helpMenuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)

        font2 = QFont()
        font2.setFamily("MS Sans Serif")
        font2.setWeight(700)
        font2.setPixelSize(8)
        font2.setBold(True)

        self.model1 = QFileSystemModel()
        self.model1.setRootPath('C:\\Windows')
        self.tree1 = QTreeView()
        self.tree1.setModel(self.model1)
        self.tree1.setRootIndex(self.model1.index("C:\\Windows\\"))
        self.tree1.setAnimated(False)
        self.tree1.setFont(font2)
        self.tree1.setIndentation(20)
        self.tree1.setSortingEnabled(True)
        self.tree1.setItemsExpandable(False)
        self.tree1.setRootIsDecorated(False)
        self.tree1.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tree1.resize(350, 480)

        self.model2 = QFileSystemModel()
        self.model2.setRootPath('C:\\Windows\\System32')
        self.tree2 = QTreeView()
        self.tree2.setModel(self.model2)
        self.tree2.setRootIndex(self.model2.index("C:\\Windows\\System32\\"))
        self.tree2.setAnimated(False)
        self.tree2.setFont(font2)
        self.tree2.setIndentation(20)
        self.tree2.setItemsExpandable(False)
        self.tree2.setRootIsDecorated(False)
        self.tree2.setSortingEnabled(True)
        self.tree2.resize(350, 480)

        for i in range(1, self.tree1.model().columnCount()):
            self.tree1.header().hideSection(i)

        for i in range(1, self.tree2.model().columnCount()):
            self.tree2.header().hideSection(i)

        self.centralHBox = QHBoxLayout()
        self.centralHBox.addWidget(self.tree1)
        self.centralHBox.addWidget(self.tree2)
        self.centralHBox.setContentsMargins(3, 3, 3, 3)
        self.centralwidget.setLayout(self.centralHBox)

        self.toolBar_2.setMovable(False)

        self.toolBar_3 = QToolBar(MainWindow)
        self.toolBar_3.setFixedHeight(30)
        self.toolBar_3.setContentsMargins(1, 1, 1, 1)
        self.dirLabel = QLabel()
        self.dirLabel.setText('c:\\Windows>')
        self.dirBox = QComboBox()
        self.dirBox.setEditable(True)
        self.dirBox.addItem('')
        self.dirBox.setFixedWidth(470)
        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolBar_3.addWidget(self.spacer)
        self.toolBar_3.addWidget(self.dirLabel)
        self.toolBar_3.addWidget(self.dirBox)
        self.toolBar_3.setFont(font)
        self.toolBar_3.setMovable(False)
        self.toolBar_3.setStyleSheet("QToolBar{spacing: 5px;}")

        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_2)
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_3)
        MainWindow.insertToolBarBreak(self.toolBar_3)
        self.actionIndex = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("help_1.png"), QIcon.Normal, QIcon.Off)
        self.actionIndex.setIcon(icon1)
        self.actionKeyboard = QAction(MainWindow)
        self.actionRegistration_Info = QAction(MainWindow)
        self.actionVisit_Total_CMD_s_website = QAction(MainWindow)
        self.actionAbout_Total_Commander = QAction(MainWindow)
        self.actionOption_1 = QAction(MainWindow)
        self.actionOption_2 = QAction(MainWindow)
        self.actionOption_3 = QAction(MainWindow)
        self.actionOption_4 = QAction(MainWindow)
        self.actionOption_5 = QAction(MainWindow)
        self.actionOption_6 = QAction(MainWindow)
        self.actionOption_7 = QAction(MainWindow)
        self.actionOption_8 = QAction(MainWindow)
        self.actionOption_9 = QAction(MainWindow)
        self.actionOption_10 = QAction(MainWindow)
        self.actionOption_11 = QAction(MainWindow)
        self.actionOption_12 = QAction(MainWindow)
        self.actionOption_13 = QAction(MainWindow)
        self.actionOption_14 = QAction(MainWindow)
        self.Refresh = QAction(MainWindow)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("refresh_1.png"), QIcon.Normal, QIcon.Off)
        self.Refresh.setIcon(icon2)
        self.action_view1 = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("folder_structure_1.png"), QIcon.Normal, QIcon.Off)
        self.view_group = QActionGroup(MainWindow)
        self.action_view1.setIcon(icon3)
        self.action_view1.setCheckable(True)
        self.action_view2 = QAction(MainWindow)
        self.action_view2.setCheckable(True)
        self.action_view2.setChecked(True)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("folder_structure_2.png"), QIcon.Normal, QIcon.Off)
        self.action_view2.setIcon(icon4)
        self.view_group.addAction(self.action_view1)
        self.view_group.addAction(self.action_view2)
        self.view_group.setExclusive(True)
        self.actionF3_View = QToolButton(MainWindow)
        self.actionF3_View.setStyleSheet("QToolButton{border: none;}")
        self.actionF3_View.setFont(font)
        self.actionF4_Edit = QToolButton(MainWindow)
        self.actionF4_Edit.setStyleSheet("QToolButton{border: none;}")
        self.actionF4_Edit.setFont(font)
        self.actionF5_Copy = QToolButton(MainWindow)
        self.actionF5_Copy.setStyleSheet("QToolButton{border: none;}")
        self.actionF5_Copy.setFont(font)
        self.actionF6_Move = QToolButton(MainWindow)
        self.actionF6_Move.setStyleSheet("QToolButton{border: none;}")
        self.actionF6_Move.setFont(font)
        self.actionF5_NewFolder = QToolButton(MainWindow)
        self.actionF5_NewFolder.setStyleSheet("QToolButton{border: none;}")
        self.actionF5_NewFolder.setFont(font)
        self.actionF8_Delete = QToolButton(MainWindow)
        self.actionF8_Delete.setStyleSheet("QToolButton{border: none;}")
        self.actionF8_Delete.setFont(font)
        self.actionAlt_F4_Exit = QToolButton(MainWindow)
        self.actionAlt_F4_Exit.setStyleSheet("QToolButton{border: none;}")
        self.actionAlt_F4_Exit.setFont(font)
        self.menuFiles.addAction(self.actionOption_1)
        self.menuFiles.addAction(self.actionOption_2)
        self.menuMark.addAction(self.actionOption_3)
        self.menuMark.addAction(self.actionOption_4)
        self.menuCommands.addAction(self.actionOption_5)
        self.menuCommands.addAction(self.actionOption_6)
        self.menuNet.addAction(self.actionOption_7)
        self.menuNet.addAction(self.actionOption_8)
        self.menuShow.addAction(self.actionOption_9)
        self.menuShow.addAction(self.actionOption_10)
        self.menuConfiguration.addAction(self.actionOption_11)
        self.menuConfiguration.addAction(self.actionOption_12)
        self.menuStart.addAction(self.actionOption_13)
        self.menuStart.addAction(self.actionOption_14)
        self.menuHelp.addAction(self.actionIndex)
        self.menuHelp.addAction(self.actionKeyboard)
        self.menuHelp.addAction(self.actionRegistration_Info)
        self.menuHelp.addAction(self.actionVisit_Total_CMD_s_website)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Total_Commander)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuMark.menuAction())
        self.menubar.addAction(self.menuCommands.menuAction())
        self.menubar.addAction(self.menuNet.menuAction())
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuStart.menuAction())
        self.helpMenuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.Refresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_view1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_view2)

        self.separator1 = QFrame()
        self.separator1.setFrameShape(QFrame.VLine)
        self.separator1.setFrameShadow(QFrame.Sunken)
        self.separator2 = QFrame()
        self.separator2.setFrameShape(QFrame.VLine)
        self.separator2.setFrameShadow(QFrame.Sunken)
        self.separator3 = QFrame()
        self.separator3.setFrameShape(QFrame.VLine)
        self.separator3.setFrameShadow(QFrame.Sunken)
        self.separator4 = QFrame()
        self.separator4.setFrameShape(QFrame.VLine)
        self.separator4.setFrameShadow(QFrame.Sunken)
        self.separator5 = QFrame()
        self.separator5.setFrameShape(QFrame.VLine)
        self.separator5.setFrameShadow(QFrame.Sunken)
        self.separator6 = QFrame()
        self.separator6.setFrameShape(QFrame.VLine)
        self.separator6.setFrameShadow(QFrame.Sunken)

        self.toolbarHBoxWidget = QWidget()
        self.toolbarHBoxWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolbarHBox = QGridLayout()
        self.toolbarHBoxWidget.setLayout(self.toolbarHBox)
        self.toolbarHBox.addWidget(self.actionF3_View, 0, 0)
        self.toolbarHBox.addWidget(self.separator1, 0, 1)
        self.toolbarHBox.addWidget(self.actionF4_Edit, 0, 2)
        self.toolbarHBox.addWidget(self.separator2, 0, 3)
        self.toolbarHBox.addWidget(self.actionF5_Copy, 0, 4)
        self.toolbarHBox.addWidget(self.separator3, 0, 5)
        self.toolbarHBox.addWidget(self.actionF6_Move, 0, 6)
        self.toolbarHBox.addWidget(self.separator4, 0, 7)
        self.toolbarHBox.addWidget(self.actionF5_NewFolder, 0, 8)
        self.toolbarHBox.addWidget(self.separator5, 0, 9)
        self.toolbarHBox.addWidget(self.actionF8_Delete, 0, 10)
        self.toolbarHBox.addWidget(self.separator6, 0, 11)
        self.toolbarHBox.addWidget(self.actionAlt_F4_Exit, 0, 12)
        self.toolBar_2.addWidget(self.toolbarHBoxWidget)
        self.toolBar_2.setFixedHeight(40)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Total Commander 7.50a - Politechnika Lodzka - Wydzial EEIA")
        self.menuFiles.setTitle("Files")
        self.menuMark.setTitle("Mark")
        self.menuCommands.setTitle("Commands")
        self.menuNet.setTitle("Net")
        self.menuShow.setTitle("Show")
        self.menuConfiguration.setTitle("Configuration")
        self.menuStart.setTitle("Start")
        self.menuHelp.setTitle("Help")
        self.toolBar.setWindowTitle("toolBar")
        self.toolBar_2.setWindowTitle("toolBar_2")
        self.actionIndex.setText("Index")
        self.actionIndex.setIconText("Index")
        self.actionIndex.setShortcut("F1")
        self.actionKeyboard.setText("Keyboard")
        self.actionRegistration_Info.setText("Registration Info")
        self.actionVisit_Total_CMD_s_website.setText("Visit Totalcmd\'s Web Site")
        self.actionAbout_Total_Commander.setText("About Total Commander...")
        self.actionOption_1.setText("Option 1")
        self.actionOption_2.setText("Option 2")
        self.actionOption_3.setText("Option 1")
        self.actionOption_4.setText("Option 2")
        self.actionOption_5.setText("Option 1")
        self.actionOption_6.setText("Option 2")
        self.actionOption_7.setText("Option 1")
        self.actionOption_8.setText("Option 2")
        self.actionOption_9.setText("Option 1")
        self.actionOption_10.setText("Option 2")
        self.actionOption_11.setText("Option 1")
        self.actionOption_12.setText("Option 2")
        self.actionOption_13.setText("Option 1")
        self.actionOption_14.setText("Option 2")
        self.Refresh.setText("Refresh")
        self.action_view1.setText("View 1")
        self.action_view2.setText("View 2")
        self.actionF3_View.setText("F3 View")
        self.actionF3_View.setShortcut("F3")
        self.actionF4_Edit.setText("F4 Edit")
        self.actionF4_Edit.setShortcut("F4")
        self.actionF5_Copy.setText("F5 Copy")
        self.actionF5_Copy.setShortcut("F5")
        self.actionF6_Move.setText("F6 Move")
        self.actionF6_Move.setShortcut("F6")
        self.actionF5_NewFolder.setText("F7 NewFolder")
        self.actionF5_NewFolder.setShortcut("F7")
        self.actionF8_Delete.setText("F8 Delete")
        self.actionF8_Delete.setShortcut("F8")
        self.actionAlt_F4_Exit.setText("Alt+F4 Exit")
        self.actionAlt_F4_Exit.setShortcut("Ctrl+Alt+F4")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
