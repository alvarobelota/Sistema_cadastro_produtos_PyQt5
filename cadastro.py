from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
import json
import os

class projeto:
    def __init__(self):
        self.nome = ""
        self.inicio = ""
        self.fim = ""
        self.valor = ""
        self.risco = ""
        self.integrante = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setInicio(self, inicio):
        self.inicio = inicio

    def getInicio(self):
        return self.inicio

    def setFim(self, fim):
        self.fim = fim

    def getFim(self):
        return self.fim

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def setRisco(self, risco):
        self.risco = risco

    def getRisco(self):
        return self.risco

    def setIntegrantes(self, integrante):
        self.integrante = integrante

    def getIntegrantes(self):
        return self.integrante


def confirma_edita(self):
    new_project = projeto()
    new_project.setNome(form_edit.edtNome.text())
    new_project.setInicio(form_edit.edtInicio.text())
    new_project.setFim(form_edit.edtFim.text())
    new_project.setValor(form_edit.edtValor.text())
    new_project.setRisco(str(form_edit.spRisco.value()))
    new_project.setIntegrantes(form_edit.edtIntegrantes.text())

    if new_project.getNome() and new_project.getInicio() and new_project.getFim() and new_project.getValor() and new_project.getRisco() and new_project.getIntegrantes():
        linha = form_main.tbProjects.currentRow()
        form_main.tbProjects.setItem(linha, 0, QtWidgets.QTableWidgetItem(form_edit.edtNome.text()))
        form_main.tbProjects.setItem(linha, 1, QtWidgets.QTableWidgetItem(form_edit.edtInicio.text()))
        form_main.tbProjects.setItem(linha, 2, QtWidgets.QTableWidgetItem(form_edit.edtFim.text()))
        form_main.tbProjects.setItem(linha, 3, QtWidgets.QTableWidgetItem(form_edit.edtValor.text()))
        form_main.tbProjects.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(form_edit.spRisco.value())))
        form_main.tbProjects.setItem(linha, 5, QtWidgets.QTableWidgetItem(form_edit.edtIntegrantes.text()))

        form_edit.close()
        table_changed()
    else:
        QMessageBox.about(form_edit, "ALERT", "CAMPO SEM PREENCHIMENTO")


def inserir_proj(self):
    new_project = projeto()
    new_project.setNome(form_new.edtNome.text())
    new_project.setInicio(form_new.edtInicio.text())
    new_project.setFim(form_new.edtFim.text())
    new_project.setValor(form_new.edtValor.text())
    new_project.setRisco(str(form_new.spRisco.value()))
    new_project.setIntegrantes(form_new.edtIntegrantes.text())

    if new_project.getNome() and new_project.getInicio() and new_project.getFim() and new_project.getValor() and new_project.getRisco() and new_project.getIntegrantes():
        form_main.tbProjects.insertRow(form_main.tbProjects.rowCount())

        form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(new_project.getNome()))
        form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(new_project.getInicio()))
        form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(new_project.getFim()))
        form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(new_project.getValor()))
        form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 4, QtWidgets.QTableWidgetItem(new_project.getRisco()))
        form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 5, QtWidgets.QTableWidgetItem(new_project.getIntegrantes()))

        form_new.edtNome.setText("")
        form_new.edtInicio.setText("")
        form_new.edtFim.setText("")
        form_new.edtValor.setText("")
        form_new.spRisco.setValue(0)
        form_new.edtIntegrantes.setText("")

        form_new.close()
        table_changed()
    else:
        QMessageBox.about(form_new,"ALERT","CAMPO SEM PREENCHIMENTO")



def chama_form_delete():
    form_main.tbProjects.removeRow(form_main.tbProjects.currentRow())
    table_changed()


def fechar_form_new(self):
    form_new.close()


def fechar_form_edit(self):
    form_edit.close()


def chama_form_cad():
    form_new.show()


def chama_form_sim():
    linha = form_main.tbProjects.currentRow()

    if linha != -1:
      window3.show()
      window3.label_5.setText("")


def valor_proj():
    window3.label_5.setText("")
    valor_invest = window3.lineEdit.text()
    a=float(valor_invest)
    row = form_main.tbProjects.currentItem().row()
    valor_p = int(form_main.tbProjects.item(row, 3).text())
    if(a<valor_p):
        QMessageBox.about(window3, "ALERT", "valor inválido")
    row = form_main.tbProjects.currentItem().row()
    risco = int(form_main.tbProjects.item(row, 4).text())
    if (risco == 0 and valor_p<=a):
        valor=(a)+(0.05*a)
        valor = str(valor)
        window3.label_5.setText(valor)
    elif (risco == 1 and valor_p<=a):
        valor= (a)+(0.1*a)
        valor = str(valor)
        window3.label_5.setText(valor)
    elif (risco == 2 and valor_p<=a):
        valor= (a)+(0.20*a)
        valor = str(valor)
        window3.label_5.setText(valor)
    else:
        print("risco invalido")

    window3.lineEdit.setText("")


def chama_form_edit():
    linha = form_main.tbProjects.currentRow()

    if linha != -1:
        form_edit.edtNome.setText(form_main.tbProjects.item(linha, 0).text())
        form_edit.edtInicio.setText(form_main.tbProjects.item(linha, 1).text())
        form_edit.edtFim.setText(form_main.tbProjects.item(linha, 2).text())
        form_edit.edtValor.setText(form_main.tbProjects.item(linha, 3).text())
        form_edit.spRisco.setValue(int(form_main.tbProjects.item(linha, 4).text()))
        form_edit.edtIntegrantes.setText(form_main.tbProjects.item(linha, 5).text())
        form_edit.show()


def table_changed():
    if form_main.tbProjects.rowCount() > 0:
        project = projeto()
        json_project = {}
        json_project['projects'] = []

        for linha in range(0, form_main.tbProjects.rowCount()):
            project.setNome(form_main.tbProjects.item(linha, 0).text())
            project.setInicio(form_main.tbProjects.item(linha, 1).text())
            project.setFim(form_main.tbProjects.item(linha, 2).text())
            project.setValor(form_main.tbProjects.item(linha, 3).text())
            project.setRisco(form_main.tbProjects.item(linha, 4).text())
            project.setIntegrantes(form_main.tbProjects.item(linha, 5).text())

            json_project['projects'].append({
                "nome": project.getNome(),
                "inicio": project.getInicio(),
                "fim": project.getFim(),
                "valor": project.getValor(),
                "risco": project.getRisco(),
                "integrantes": project.getIntegrantes(),
            })

        with open("data.json", "w") as proj:
            json.dump(json_project, proj)


def load_projects():
    if os.path.exists('./data.json'):
        with open("data.json", "r") as proj:
            data = json.load(proj)
            for p in data['projects']:
                form_main.tbProjects.insertRow(form_main.tbProjects.rowCount())

                form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(p["nome"]))
                form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(p["inicio"]))
                form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(p["fim"]))
                form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(p["valor"]))
                form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 4, QtWidgets.QTableWidgetItem(p["risco"]))
                form_main.tbProjects.setItem(form_main.tbProjects.rowCount() - 1, 5, QtWidgets.QTableWidgetItem(p["integrantes"]))
    else:
        json_project = {}
        json_project['projects'] = []
        with open('data.json', 'w') as outfile:
            json.dump(json_project, outfile)


app = QtWidgets.QApplication([])
form_main = uic.loadUi("window1.ui")
form_new = uic.loadUi("window2.ui")
form_edit = uic.loadUi("window2.ui")
window3 = uic.loadUi("window3.ui")

form_main.btNew.clicked.connect(chama_form_cad)
form_main.btEdit.clicked.connect(chama_form_edit)
form_main.btSim.clicked.connect(chama_form_sim)
form_main.btDelete.clicked.connect(chama_form_delete)

form_new.btSave.clicked.connect(inserir_proj)
form_new.btCancel.clicked.connect(fechar_form_new)

form_edit.btSave.clicked.connect(confirma_edita)
form_edit.btCancel.clicked.connect(fechar_form_edit)

window3.pushButton.clicked.connect(valor_proj)

load_projects()

form_main.show()
app.exec()
