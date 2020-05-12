# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QUrl, QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
import autofill
import sys


class Qml(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.data = autofill.loadData()
        self.corpus = autofill.sentenceTokenize(self.data)
        self.results = dict
        self.words = list

    @Slot(result=str)
    def getResults(self):
        topResult = ""
        if len(self.words) > 1:
            for key in self.results.keys():
               topResult += key + " "
        return topResult

    @Slot(str)
    def getSearchSentence(self, sentence):
        self.words = sentence.split()
        if len(self.words) > 1:
            self.results = autofill.searchOnData(self.corpus, word1=self.words[-2], word2=self.words[-1])


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qml = Qml()
    engine.rootContext().setContextProperty("qml", qml)
    engine.load(QUrl("guiQml.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
