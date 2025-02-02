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

        self.view.printParameter(verbs.list_of_verbs, tenses.list_of_tenses, subjects.list_of_subjects, forms.list_of_forms)

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

        for i in range(len(verbs.list_of_verbs)):
            if verbs.list_of_verbs[i][1]:
                filtered_verbs.append(verbs.list_of_verbs[i][0])

        for i in range(len(subjects.list_of_subjects)):
            if subjects.list_of_subjects[i][1]:
                filtered_subjects.append(subjects.list_of_subjects[i][0])

        for i in range(len(tenses.list_of_tenses)):
            if tenses.list_of_tenses[i][1]:
                filtered_tenses.append(tenses.list_of_tenses[i][0])

        for i in range(len(forms.list_of_forms)):
            if forms.list_of_forms[i][1]:
                filtered_forms.append(forms.list_of_forms[i][0])

        return [random.choice(filtered_subjects), random.choice(filtered_verbs), random.choice(filtered_tenses), random.choice(filtered_forms)]

    def get_method(self):
        return [[verbs.add_verbs, verbs.select_verbs, verbs.deselect_verbs, verbs.update_verb],
                [subjects.add_subjects, subjects.select_subjects, subjects.deselect_subjects, subjects.update_subject],
                [tenses.add_tenses, tenses.select_tenses, tenses.deselect_tenses, tenses.update_tense],
                [forms.add_forms, forms.select_forms, forms.deselect_forms, forms.update_form]]


if __name__ == "__main__":
    app = Vue.QApplication(sys.argv)

    verbModel = Verbs()
    tenseModel = Tenses()
    subjectModel = Subjects()
    formModel = Forms()

    view = Vue.MainView()

    controller = MainControlleur(verbModel, tenseModel, subjectModel, formModel, view)

    view.showMaximized()

    sys.exit(app.exec())



    #choose_mode = Vue.choose_mod()
    #if choose_mode == "parameter":
    #    finish = False
    #    while not finish:
    #        Vue.print_parameter(verbs.list_of_verbs, tenses.list_of_tenses, subjects.list_of_subjects, forms.list_of_forms)
    #        Vue.change_parameter(get_method())
    #        if Vue.is_parameter_finish():
    #            finish = True
    #elif choose_mode == "play":
    #    c = 0
    #    while Vue.is_ready(c):
    #        random_phrase = random_phrase()
    #        Vue.question(random_phrase)
    #        Vue.check_answer(answer(), random_phrase[1], random_phrase[2], random_phrase[0], random_phrase[3])
    #        c += 1