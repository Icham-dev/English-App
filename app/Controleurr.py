from Model import *
import Vue

import random
import sys

class MainControlleur:
    def __init__(self, verbModel, tenseModel, subjectModel, formModel, view):
        self.verbModel = verbModel
        self.tenseModel = tenseModel
        self.subjectModel = subjectModel
        self.formModel = formModel
        self.view = view
        self.view.controller = self

        self.view.printParameter(self.verbModel.list_of_verbs, self.tenseModel.list_of_tenses, self.subjectModel.list_of_subjects, self.formModel.list_of_forms)

        self.view.startPlayButton.clicked.connect(lambda: self.view.printQuestion(self.random_phrase()))

        self.view.playButton.clicked.connect(lambda: self.view.buttonSidebar(self.view.playButton, self.view.parameterButton))
        self.view.parameterButton.clicked.connect(lambda: self.view.buttonSidebar(self.view.parameterButton, self.view.playButton))

        self.view.playButton.clicked.connect(lambda: self.view.switchPage(0))
        self.view.parameterButton.clicked.connect(lambda: self.view.switchPage(1))
        

    def random_phrase(self):
        filtered_verbs = []
        filtered_subjects = []
        filtered_tenses = []
        filtered_forms = []

        for i in range(len(self.verbModel.list_of_verbs)):
            if self.verbModel.list_of_verbs[i][1]:
                filtered_verbs.append(self.verbModel.list_of_verbs[i][0])

        for i in range(len(self.subjectModel.list_of_subjects)):
            if self.subjectModel.list_of_subjects[i][1]:
                filtered_subjects.append(self.subjectModel.list_of_subjects[i][0])

        for i in range(len(self.tenseModel.list_of_tenses)):
            if self.tenseModel.list_of_tenses[i][1]:
                filtered_tenses.append(self.tenseModel.list_of_tenses[i][0])

        for i in range(len(self.formModel.list_of_forms)):
            if self.formModel.list_of_forms[i][1]:
                filtered_forms.append(self.formModel.list_of_forms[i][0])

        return [random.choice(filtered_subjects), random.choice(filtered_verbs), random.choice(filtered_tenses), random.choice(filtered_forms)]

    def get_method(self):
        return [[self.verbModel.add_verbs, self.verbModel.select_verbs, self.verbModel.deselect_verbs, self.verbModel.update_verb],
                [self.subjectModel.add_subjects, self.subjectModel.select_subjects, self.subjectModel.deselect_subjects, self.subjectModel.update_subject],
                [self.tenseModel.add_tenses, self.tenseModel.select_tenses, self.tenseModel.deselect_tenses, self.tenseModel.update_tense],
                [self.formModel.add_forms, self.formModel.select_forms, self.formModel.deselect_forms, self.formModel.update_form]]
    
    def parameterObjectButton(self, obj, objType, index, buttonList):
        match objType:
            case self.verbModel:
                if self.verbModel.is_selected(obj):
                    objType.deselect_verbs(obj)
                    buttonList[index].setStyleSheet(self.view.parameterInvalidButtonStyle)
                else:
                    objType.select_verbs(obj)
                    buttonList[index].setStyleSheet(self.view.parameterValidButtonStyle)

            case self.tenseModel:
                if self.tenseModel.is_selected(obj):
                    objType.deselect_tenses(obj)
                    buttonList[index].setStyleSheet(self.view.parameterInvalidButtonStyle)
                else:
                    objType.select_tenses(obj)
                    buttonList[index].setStyleSheet(self.view.parameterValidButtonStyle)

            case self.subjectModel:
                if self.subjectModel.is_selected(obj):
                    objType.deselect_subjects(obj)
                    buttonList[index].setStyleSheet(self.view.parameterInvalidButtonStyle)
                else:
                    objType.select_subjects(obj)
                    buttonList[index].setStyleSheet(self.view.parameterValidButtonStyle)

            case self.formModel:
                if self.formModel.is_selected(obj):
                    objType.deselect_forms(obj)
                    buttonList[index].setStyleSheet(self.view.parameterInvalidButtonStyle)
                else:
                    objType.select_forms(obj)
                    buttonList[index].setStyleSheet(self.view.parameterValidButtonStyle)

if __name__ == "__main__":
    app = Vue.QApplication(sys.argv)

    verbModel = Verbs()
    list_verbs = ["do", "be", "have", "say", "get", "make", "go", "know", "take", "see", "come", "think","look", "want", "give", "use", "find", "tell", "ask", "work", "seem", "feel", "try", "leave","call", "need", "fight", "put", "mean", "keep", "push", "cost", "cut", "hit", "hurt", "bring","build", "burn", "buy", "catch", "dream", "hear", "hold", "learn", "lose", "meet", "pay", "read","sell", "send", "sleep", "smell", "stand", "teach", "understand", "win", "begin", "drink", "break", "choose","draw", "drive", "eat", "fall", "fly", "forget", "grow", "hide", "show", "sing", "speak", "swear","swim", "throw", "write", "run"]
    for verb in list_verbs:
        verbModel.add_verbs(verb)

    tenseModel = Tenses()
    list_tenses = ["present simple", "present BE + V-ing", "preterit", "preterit BE + V-ing", "present perfect", "present perfect BE + V-ing", "past perfect", "past perfect BE + V-ing"]
    for tense in list_tenses:
        tenseModel.add_tenses(tense)

    subjectModel = Subjects()
    list_subjects = ["I", "You", "He", "She", "It", "We", "They", "My parents", "The children", "My neighbour", "Susan", "John"]
    for subject in list_subjects:
        subjectModel.add_subjects(subject)

    formModel = Forms()
    list_forms = ["affirmative", "negative", "interrogative", "interro-negative"]
    for form in list_forms:
        formModel.add_forms(form)

    view = Vue.MainView()

    controller = MainControlleur(verbModel, tenseModel, subjectModel, formModel, view)

    view.showMaximized()

    sys.exit(app.exec())
