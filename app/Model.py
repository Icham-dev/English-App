class Verbs:
    def __init__(self):
        self.list_of_verbs = []
    
    def __str__(self):
        return "\n".join([verb[0] for verb in self.list_of_verbs])

    def add_verbs(self, v):
        if type(v) != list:
            v = [v]
        for i in range(len(v)):
            if v[i] not in self.list_of_verbs:
                self.list_of_verbs.append((v[i], True))

    def select_verbs(self, v):
        if type(v) != list:
            v = [v]
        for i in range(len(self.list_of_verbs)):
            for j in range(len(v)):
                if self.list_of_verbs[i][0] == v[j] and self.list_of_verbs[i][1] == False:
                    self.list_of_verbs[i] = list(self.list_of_verbs[i])
                    self.list_of_verbs[i][1] = True
                    self.list_of_verbs[i] = tuple(self.list_of_verbs[i])
                    break

    def deselect_verbs(self, v):
        if type(v) != list:
            v = [v]
        for i in range(len(self.list_of_verbs)):
            for j in range(len(v)):
                if self.list_of_verbs[i][0] == v[j] and self.list_of_verbs[i][1] == True:
                    self.list_of_verbs[i] = list(self.list_of_verbs[i])
                    self.list_of_verbs[i][1] = False
                    self.list_of_verbs[i] = tuple(self.list_of_verbs[i])
                    break
    
    def update_verb(self, v1, v2):
        for i in range(len(self.list_of_verbs)):
            if self.list_of_verbs[i][0] == v1:
                self.list_of_verbs[i] = list(self.list_of_verbs[i])
                self.list_of_verbs[i][0] = v2
                self.list_of_verbs[i] = tuple(self.list_of_verbs[i])
                
                return
            
    def is_selected(self, verb):
        for v, state in self.list_of_verbs:
            if v == verb:
                return state
        return False

class Subjects:
    def __init__(self):
        self.list_of_subjects = []
    
    def __str__(self):
        return "\n".join([subject[0] for subject in self.list_of_subjects])

    def add_subjects(self, s):
        if type(s) != list:
            s = [s]
        for i in range(len(s)):
            if s[i] not in self.list_of_subjects:
                self.list_of_subjects.append((s[i], True))


    def select_subjects(self, s):
        if type(s) != list:
            s = [s]
        for i in range(len(self.list_of_subjects)):
            for j in range(len(s)):
                if self.list_of_subjects[i][0] == s[j] and self.list_of_subjects[i][1] == False:
                    self.list_of_subjects[i] = list(self.list_of_subjects[i])
                    self.list_of_subjects[i][1] = True
                    self.list_of_subjects[i] = tuple(self.list_of_subjects[i])
                    break

    def deselect_subjects(self, s):
        if type(s) != list:
            s = [s]
        for i in range(len(self.list_of_subjects)):
            for j in range(len(s)):
                if self.list_of_subjects[i][0] == s[j] and self.list_of_subjects[i][1] == True:
                    self.list_of_subjects[i] = list(self.list_of_subjects[i])
                    self.list_of_subjects[i][1] = False
                    self.list_of_subjects[i] = tuple(self.list_of_subjects[i])
                    break
    
    def update_subject(self, s1, s2):
        for i in range(len(self.list_of_subjects)):
            if self.list_of_subjects[i][0] == s1:
                self.list_of_subjects[i] = list(self.list_of_subjects[i])
                self.list_of_subjects[i][0] = s2
                self.list_of_subjects[i] = tuple(self.list_of_subjects[i])
                return
    
    def is_selected(self, subject):
        for s, state in self.list_of_subjects:
            if s == subject:
                return state
        return False

class Tenses:
    def __init__(self):
        self.list_of_tenses = []
    
    def __str__(self):
        return "\n".join([tense[0] for tense in self.list_of_tenses])

    def add_tenses(self, t):
        if type(t) != list:
            t = [t]
        for i in range(len(t)):
            if t[i] not in self.list_of_tenses:
                self.list_of_tenses.append((t[i], True))


    def select_tenses(self, t):
        if type(t) != list:
            t = [t]
        for i in range(len(self.list_of_tenses)):
            for j in range(len(t)):
                if self.list_of_tenses[i][0] == t[j] and self.list_of_tenses[i][1] == False:
                    self.list_of_tenses[i] = list(self.list_of_tenses[i])
                    self.list_of_tenses[i][1] = True
                    self.list_of_tenses[i] = tuple(self.list_of_tenses[i])
                    break

    def deselect_tenses(self, t):
        if type(t) != list:
            t = [t]
        for i in range(len(self.list_of_tenses)):
            for j in range(len(t)):
                if self.list_of_tenses[i][0] == t[j] and self.list_of_tenses[i][1] == True:
                    self.list_of_tenses[i] = list(self.list_of_tenses[i])
                    self.list_of_tenses[i][1] = False
                    self.list_of_tenses[i] = tuple(self.list_of_tenses[i])
                    break
    
    def update_tense(self, t1, t2):
        for i in range(len(self.list_of_tenses)):
            if self.list_of_tenses[i][0] == t1:
                self.list_of_tenses[i] = list(self.list_of_tenses[i])
                self.list_of_tenses[i][0] = t2
                self.list_of_tenses[i] = tuple(self.list_of_tenses[i])
                
                return
            
    def is_selected(self, tense):
        for t, state in self.list_of_tenses:
            if t == tense:
                return state
        return False
    
class Forms:
    def __init__(self):
        self.list_of_forms = []
    
    def __str__(self):
        return "\n".join([form[0] for form in self.list_of_forms])

    def add_forms(self, f):
        if type(f) != list:
            f = [f]
        for i in range(len(f)):
            if f[i] not in self.list_of_forms:
                self.list_of_forms.append((f[i], True))


    def select_forms(self, f):
        if type(f) != list:
            f = [f]
        for i in range(len(self.list_of_forms)):
            for j in range(len(f)):
                if self.list_of_forms[i][0] == f[j] and self.list_of_forms[i][1] == False:
                    self.list_of_forms[i] = list(self.list_of_forms[i])
                    self.list_of_forms[i][1] = True
                    self.list_of_forms[i] = tuple(self.list_of_forms[i])
                    break

    def deselect_forms(self, f):
        if type(f) != list:
            f = [f]
        for i in range(len(self.list_of_forms)):
            for j in range(len(f)):
                if self.list_of_forms[i][0] == f[j]:
                    self.list_of_forms[i] = list(self.list_of_forms[i])
                    self.list_of_forms[i][1] = False
                    self.list_of_forms[i] = tuple(self.list_of_forms[i])
                    break
    
    def update_form(self, f1, f2):
        for i in range(len(self.list_of_forms)):
            if self.list_of_forms[i][0] == f1:
                self.list_of_forms[i] = list(self.list_of_forms[i])
                self.list_of_forms[i][0] = f2
                self.list_of_forms[i] = tuple(self.list_of_forms[i])
                return
            
    def is_selected(self, form):
        for f, state in self.list_of_forms:
            if f == form:
                return state
        return False  # Si le verbe n'existe pas, retourne False

"""
verbs = Verbs()
list_verbs = ["do", "be", "have", "say", "get", "make", "go", "know", "take", "see", "come", "think","look", "want", "give", "use", "find", "tell", "ask", "work", "seem", "feel", "try", "leave","call", "need", "fight", "put", "mean", "keep", "push", "cost", "cut", "hit", "hurt", "bring","build", "burn", "buy", "catch", "dream", "hear", "hold", "learn", "lose", "meet", "pay", "read","sell", "send", "sleep", "smell", "stand", "teach", "understand", "win", "begin", "drink", "break", "choose","draw", "drive", "eat", "fall", "fly", "forget", "grow", "hide", "show", "sing", "speak", "swear","swim", "throw", "write", "run"]
for verb in list_verbs:
    verbs.add_verbs(verb)

subjects = Subjects()
list_subjects = ["I", "You", "He", "She", "It", "We", "They", "My parents", "The children", "My neighbour", "Susan", "John"]
for subject in list_subjects:
    subjects.add_subjects(subject)

tenses = Tenses()
list_tenses = ["present simple", "present BE + V-ing", "preterit", "preterit BE + V-ing", "present perfect", "present perfect BE + V-ing", "past perfect", "past perfect BE + V-ing"]
for tense in list_tenses:
    tenses.add_tenses(tense)

forms = Forms()
list_forms = ["affirmative", "negative", "interrogative", "interro-negative"]
for form in list_forms:
    forms.add_forms(form)
"""