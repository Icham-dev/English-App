import time
import random
import os

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.imgPath = os.path.join(os.path.dirname(__file__), "img/")
        self.screen = QGuiApplication.primaryScreen().availableGeometry()
        print(self.screen.height(), self.screen.width())
        self.setWindowTitle("English Training")

        centreWidget = QWidget()
        centreWidget.setStyleSheet("background-color: #0a2463;")
        self.setCentralWidget(centreWidget)

        self.mainLayout = QHBoxLayout(centreWidget)

        self.sideBar = QFrame()
        #sideBar.setFrameShape(QFrame.StyledPanel)
        self.sideBar.setMaximumSize(70, 500)
        self.sideBar.setMinimumSize(70, 500)
        self.sideBar.setStyleSheet("  border-radius: 30px;")
        sidebarLayout = QVBoxLayout(self.sideBar)

        self.sidebarButtonStyle = """QPushButton{
                                        background-color: none;
                                        border: none;
                                        border-radius: 26px;
                                        padding: 10px;
                                    }
                                    QPushButton:hover{
                                        background-color: rgba(255, 255, 255, 0.20);
                                    }
                                    QPushButton:pressed{
                                        padding: 7px;
                                        margin: 3px;
                                        border-radius: 23px
                                    }
                                    """

        self.playButton = QPushButton('')
        self.playButton.setIcon(QIcon(f"{self.imgPath}circle-play-solid_1.svg"))
        self.playButton.setIconSize(QSize(32, 32))
        self.playButton.setStyleSheet("background-color: #FFD43B; padding: 10px; border-radius: 26px;")

        self.parameterButton = QPushButton('')
        self.parameterButton.setIcon(QIcon(f"{self.imgPath}gear-solid.svg"))
        self.parameterButton.setIconSize(QSize(32, 32))
        self.parameterButton.setStyleSheet(self.sidebarButtonStyle)
        
        sidebarLayout.addStretch(1)
        sidebarLayout.addWidget(self.playButton, alignment=Qt.AlignmentFlag.AlignCenter)
        sidebarLayout.addWidget(self.parameterButton, alignment=Qt.AlignmentFlag.AlignCenter)
        sidebarLayout.addStretch(2)

        self.stackedWidget = QStackedWidget()

        self.playPage = QFrame()
        self.playPage.setMinimumSize(self.screen.width()-self.sideBar.width()*2, self.screen.height()-self.sideBar.width()*2)
        self.playPage.setStyleSheet("background-color: rgba(255, 255, 255, 0.90); color:black; border-radius:10px;")
        self.playPageLayout = QVBoxLayout(self.playPage)

        self.startPlayButton = QPushButton(" Play !")
        self.startPlayButton.setStyleSheet("""
                                        QPushButton{
                                            background-color:#FFD43B;
                                            padding: 10px 30px;
                                            font-size: 20px;
                                            border-radius: 5px;
                                            color:#0a2463;
                                            font-weight: 600;
                                        }
                                        QPushButton:hover{
                                            background-color: #0a2463;
                                            color: #FFD43B;
                                        }
                                        """)
        self.playPageLayout.addWidget(self.startPlayButton, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.parameterPage = QFrame()
        self.parameterPage.setStyleSheet("background-color: rgba(255, 255, 255, 0.90); color:black; border-radius:10px;")
        self.parameterPage.setMaximumSize(self.screen.width()-self.sideBar.width()*2, self.screen.height()-self.sideBar.width()*2)
        self.parameterPageLayout = QVBoxLayout(self.parameterPage)

        self.stackedWidget.addWidget(self.playPage)
        self.stackedWidget.addWidget(self.parameterPage)

        self.mainLayout.addStretch()
        self.mainLayout.addWidget(self.sideBar, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.stackedWidget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addStretch()

    def printQuestion(self, random_phrase):
        if self.startPlayButton is not None:
            self.playPageLayout.removeWidget(self.startPlayButton)
            self.startPlayButton.deleteLater()
            self.startPlayButton = None
        else:
            self.removePlaypageWidget()

        self.decompte = 3
        self.timePrint = QLabel(f"{self.decompte}")
        self.timePrint.setStyleSheet("font-size: 80px; font-weight: 600; background-color:none; color: #0a2463;")
        self.playPageLayout.addWidget(self.timePrint, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Intervalle de 1 seconde
        self.timer.timeout.connect(self.updateCountdown)
        self.timer.start()

        self.question = QLabel("Give me a sentence with : ")
        self.question.setStyleSheet(f"font-size: 40px; font-weight: 400; color: black; background-color:none;")
        self.question.setMinimumHeight(70)
        self.question.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.question.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.questionBox = QGridLayout()
        self.questionBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.verbAttachement = QLabel("Verb :")
        self.verbAttachement.setStyleSheet("background:none; font-size: 20px;")
        self.verbAttachement.setMaximumHeight(50)
        self.subjectAttachement = QLabel("Subject :")
        self.subjectAttachement.setStyleSheet("background:none; font-size: 20px;")
        self.subjectAttachement.setMaximumHeight(50)
        self.tenseAttachement = QLabel("Tense :")
        self.tenseAttachement.setStyleSheet("background:none; font-size: 20px;")
        self.tenseAttachement.setMaximumHeight(50)
        self.formAttachement = QLabel("Form :")
        self.formAttachement.setStyleSheet("background:none; font-size: 20px;")
        self.formAttachement.setMaximumHeight(50)

        self.verb = QLabel(random_phrase[1])
        self.verb.setStyleSheet("background-color: #FFD43B; padding: 0 10px; border-radius: 3px; font-size: 40px; font-weight: 600;")
        self.verb.setMaximumHeight(70)
        self.subject = QLabel(random_phrase[0])
        self.subject.setStyleSheet("background-color: #FFD43B; padding: 0 10px; border-radius: 3px; font-size: 40px; font-weight: 600;")
        self.subject.setMaximumHeight(70)
        self.tense = QLabel(random_phrase[2])
        self.tense.setStyleSheet("background-color: #FFD43B; padding: 0 10px; border-radius: 3px; font-size: 40px; font-weight: 600;")
        self.tense.setMaximumHeight(70)
        self.form = QLabel(random_phrase[3])
        self.form.setStyleSheet("background-color: #FFD43B; padding: 0 10px; border-radius: 3px; font-size: 40px; font-weight: 600;")
        self.form.setMaximumHeight(70)

        self.questionBox.addWidget(self.subjectAttachement, 0, 0)
        self.questionBox.addWidget(self.verbAttachement, 0, 1)
        self.questionBox.addWidget(self.tenseAttachement, 0, 2)
        self.questionBox.addWidget(self.formAttachement, 0, 3)

        self.questionBox.addWidget(self.subject, 1, 0)
        self.questionBox.addWidget(self.verb, 1, 1)
        self.questionBox.addWidget(self.tense, 1, 2)
        self.questionBox.addWidget(self.form, 1, 3)

    def updateCountdown(self):
        if self.decompte > 1:
            self.playPageLayout.removeWidget(self.timePrint)
            self.timePrint.deleteLater()
            self.decompte -= 1
            self.timePrint = QLabel(f"{self.decompte}")
            self.timePrint.setStyleSheet("font-size: 80px; font-weight: 600; background-color:none; color: #0a2463;")
            self.playPageLayout.addWidget(self.timePrint, alignment=Qt.AlignmentFlag.AlignCenter)
        else:
            self.timer.stop()
            self.playPageLayout.removeWidget(self.timePrint)
            self.timePrint.deleteLater()

            self.playPageLayout.addWidget(self.question)
            self.playPageLayout.addLayout(self.questionBox)

            self.mainmenuButton = QPushButton("Main Menu")
            self.mainmenuButton.setStyleSheet("""
                QPushButton {
                    background-color:#FFD43B;
                    padding: 10px 30px;
                    font-size: 20px;
                    border-radius: 5px;
                    color:#0a2463;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #0a2463;
                    color: #FFD43B;
                }
            """)

            self.nextquestionButton = QPushButton("Next")
            self.nextquestionButton.setStyleSheet("""
                QPushButton {
                    background-color:#FFD43B;
                    padding: 10px 30px;
                    font-size: 20px;
                    border-radius: 5px;
                    color:#0a2463;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #0a2463;
                    color: #FFD43B;
                }
            """)
            self.playPageLayout.addWidget(self.mainmenuButton, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
            self.playPageLayout.addWidget(self.nextquestionButton, alignment=Qt.AlignmentFlag.AlignHCenter)
            self.mainmenuButton.clicked.connect(self.playPageInit)
            self.nextquestionButton.clicked.connect(self.nextQuestionAction)
            

    def nextQuestionAction(self):
        self.playPageLayout.removeWidget(self.mainmenuButton)
        self.playPageLayout.removeWidget(self.nextquestionButton)
        self.mainmenuButton.deleteLater()
        self.nextquestionButton.deleteLater()
        self.printQuestion(self.controller.random_phrase())

    def playPageInit(self):
        if self.startPlayButton is None:
            self.removePlaypageWidget()
        else:
            return
        
        self.startPlayButton = QPushButton(" Play !")
        self.startPlayButton.setStyleSheet("""
                                        QPushButton{
                                            background-color:#FFD43B;
                                            padding: 10px 30px;
                                            font-size: 20px;
                                            border-radius: 5px;
                                            color:#0a2463;
                                            font-weight: 600;
                                        }
                                        QPushButton:hover{
                                            background-color: #0a2463;
                                            color: #FFD43B;
                                        }
                                        """)
        self.playPageLayout.addWidget(self.startPlayButton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.startPlayButton.clicked.connect(lambda: self.printQuestion(self.controller.random_phrase()))

    def removePlaypageWidget(self):
            widgets = [self.question, self.verb, self.subject, self.tense, self.form, self.verbAttachement, self.subjectAttachement, self.tenseAttachement, self.formAttachement, self.nextquestionButton, self.mainmenuButton]
            for widget in widgets:
                self.playPageLayout.removeWidget(widget)
                widget.deleteLater()
            self.playPageLayout.removeItem(self.questionBox)
            self.questionBox.deleteLater()

    def switchPage(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def buttonSidebar(self, btn, other):
        btn.setStyleSheet("background-color: #FFD43B; padding: 10px; border-radius: 26px;")
        other.setStyleSheet(self.sidebarButtonStyle)
        if btn == self.playButton:
            other.setIcon(QIcon(f"{self.imgPath}gear-solid.svg"))
            btn.setIcon(QIcon(f"{self.imgPath}circle-play-solid_1.svg"))
        else:
            other.setIcon(QIcon(f"{self.imgPath}circle-play-solid.svg"))
            btn.setIcon(QIcon(f"{self.imgPath}gear-solid_1.svg"))

    def printParameter(self, v, t, s, f):
        self.parameterLabelStyle = "background-color: white; padding: 5px 5px; font-size: 15px; font-weight: 600;"
        self.parameterValidButtonStyle = "background-color: green; padding: 5px 5px; font-size: 15px; font-weight: 600;"
        self.parameterInvalidButtonStyle = "background-color: red; padding: 5px 5px; font-size: 15px; font-weight: 600;"
        
        self.verbLayout = QGridLayout()
        self.tenseLayout = QGridLayout()
        self.subjectLayout = QGridLayout()
        self.formLayout = QGridLayout()
        self.buttonPerLine = (17 * self.screen.width()) // 1920

        self.verbLabelParameter = QLabel("Verb :")
        self.parameterPageLayout.addWidget(self.verbLabelParameter, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.parameterPageLayout.addLayout(self.verbLayout)
        for i in range(len(v)):
            row = i // self.buttonPerLine
            col = i % self.buttonPerLine
            self.verbButton = QPushButton(v[i][0])
            self.verbButton.clicked.connect(self.controller.parameterObjectButton)
            self.verbLayout.addWidget(self.verbButton, row, col)
            if v[i][1]:
                self.verbButton.setStyleSheet(self.parameterValidButtonStyle)
            else:
                self.verbButton.setStyleSheet(self.parameterInvalidButtonStyle)

        self.tenseLabelParameter = QLabel("Tenses: ")
        self.parameterPageLayout.addWidget(self.tenseLabelParameter, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.parameterPageLayout.addLayout(self.tenseLayout)
        for i in range(len(t)):
            row = i // self.buttonPerLine
            col = i % self.buttonPerLine
            self.tenseButton = QPushButton(t[i][0])
            self.tenseButton.clicked.connect(self.controller.parameterObjectButton)
            self.tenseLayout.addWidget(self.tenseButton, row, col)
            if t[i][1]:
                self.tenseButton.setStyleSheet(self.parameterValidButtonStyle)
            else:
                self.tenseButton.setStyleSheet(self.parameterInvalidButtonStyle)

        self.subjectLabelParameter = QLabel("Subjects: ")
        self.parameterPageLayout.addWidget(self.subjectLabelParameter, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.parameterPageLayout.addLayout(self.subjectLayout)
        for i in range(len(s)):
            row = i // self.buttonPerLine
            col = i % self.buttonPerLine
            self.subjectButton = QPushButton(s[i][0])
            self.subjectButton.clicked.connect(self.controller.parameterObjectButton)
            self.subjectLayout.addWidget(self.subjectButton, row, col)
            if s[i][1]:
                self.subjectButton.setStyleSheet(self.parameterValidButtonStyle)
            else:
                self.subjectButton.setStyleSheet(self.parameterInvalidButtonStyle)

        self.formLabelParameter = QLabel("Forms: ")
        self.parameterPageLayout.addWidget(self.formLabelParameter, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.parameterPageLayout.addLayout(self.formLayout)
        for i in range(len(f)):
            row = i // self.buttonPerLine
            col = i % self.buttonPerLine
            self.formButton = QPushButton(f[i][0])
            self.formButton.clicked.connect(self.controller.parameterObjectButton)
            self.formLayout.addWidget(self.formButton, row, col)
            if f[i][1]:
                self.formButton.setStyleSheet(self.parameterValidButtonStyle)
            else:
                self.formButton.setStyleSheet(self.parameterInvalidButtonStyle)

        labels = [self.verbLabelParameter, self.tenseLabelParameter, self.subjectLabelParameter, self.formLabelParameter]
        for label in labels:
            label.setStyleSheet(self.parameterLabelStyle)
            #label.setMaximumSize(50, 50)

    
        

"""
def change_parameter(method):
    r = input("Do you want to make some changes ?(Yes/No) :")
    while r.lower() not in ["yes", "no"]:
        r = input("Please write your answer correctly (Yes or No) : ")

    if r.lower() == "yes":
        change_choice = input("Which one? (Verbs/Tenses/Subjects/Forms)").lower()
        while change_choice not in ["verbs", "tenses", "subjects", "forms"]:
            change_choice = input("Please write your answer correctly (Verbs/Tenses/Subjects/Forms) : ")
        match change_choice:
            case "verbs":
                choose_method = input("What do you want to do ?(Add/Select/Deselect/Update)").lower()
                match choose_method:
                    case "add":
                        choose_verb = input("Write the verb(s)(separate them with coma without space) : ").split(",")
                        method[0][0](choose_verb)
                    case "select":
                        choose_verb = input("Write the verb(s)(separate them with coma without space) : ").split(",")
                        method[0][1](choose_verb)
                    case "deselect":
                        choose_verb = input("Write the verb(s)(separate them with coma without space) : ").split(",")
                        method[0][2](choose_verb)
                    case "update":
                        choose_verb = input("Write the two verbs (separate them with coma without space) : ").split(",")
                        method[0][3](choose_verb[0], choose_verb[1])
            case "tenses":
                choose_method = input("What do you want to do ?(Add/Select/Deselect/Update)").lower()
                match choose_method:
                    case "add":
                        choose_tense = input("Write the tense(s)(separate them with coma without space) : ").split(",")
                        method[2][0](choose_tense)
                    case "select":
                        choose_tense = input("Write the tense(s)(separate them with coma without space) : ").split(",")
                        method[2][1](choose_tense)
                    case "deselect":
                        choose_tense = input("Write the tense(s)(separate them with coma without space) : ").split(",")
                        method[2][2](choose_tense)
                    case "update":
                        choose_tense = input("Write the two tenses (separate them with coma without space) : ").split(",")
                        method[2][3](choose_tense[0], choose_tense[1])
            case "subjects":
                choose_method = input("What do you want to do ?(Add/Select/Deselect/Update)").lower()
                match choose_method:
                    case "add":
                        choose_subject = input("Write the subject(s)(separate them with coma without space) : ").split(",")
                        method[1][0](choose_subject)
                    case "select":
                        choose_subject = input("Write the subject(s)(separate them with coma without space) : ").split(",")
                        method[1][1](choose_subject)
                    case "deselect":
                        choose_subject = input("Write the subject(s)(separate them with coma without space) : ").split(",")
                        method[1][2](choose_subject)
                    case "update":
                        choose_subject = input("Write the two subjects (separate them with coma without space) : ").split(",")
                        method[1][3](choose_subject[0], choose_subject[1])
            case "forms":
                choose_method = input("What do you want to do ?(Add/Select/Deselect/Update)").lower()
                match choose_method:
                    case "add":
                        choose_form = input("Write the form(s)(separate them with coma without space) : ").split(",")
                        method[3][0](choose_form)
                    case "select":
                        choose_form = input("Write the form(s)(separate them with coma without space) : ").split(",")
                        method[3][1](choose_form)
                    case "deselect":
                        choose_form = input("Write the form(s)(separate them with coma without space) : ").split(",")
                        method[3][2](choose_form)
                    case "update":
                        choose_form = input("Write the two forms (separate them with coma without space) : ").split(",")
                        method[3][3](choose_form[0], choose_form[1])

def is_ready(c):
    if c == 0:
        r = input("Are you ready ?(Yes/No) : ")
    else:
        r = input("Next ?(Yes/No) : ")
    while r.lower() not in ["yes", "no"]:
        r = input("Please write your answer correctly (Yes or No) : ")

    return r.lower() == "yes"

def question(random_phrase):
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print()
    print("Give me a sentence with : ")
    print(f"Subject : {random_phrase[0]}\nVerb : {random_phrase[1]}\nTense : {random_phrase[2]}\nForm : {random_phrase[3]}")
    print()

def check_answer(answer, verb, tense, subject, form):
    pass

"""