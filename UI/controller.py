import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi"))

        self._view.update_page()

    def handleCompConnessa(self,e):
        idAdded = self._view._txtIdOggetto.value
        try:
            intIdAdded = int(idAdded)
            if self._model.checkExistance(intIdAdded):
                self._view.txt_result.controls.append(ft.Text(f"L'oggetto con id {intIdAdded} è presente nel grafo"))
                sizeConnessa = self._model.getConnessa(intIdAdded)
                self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {intIdAdded} ha dimensione {sizeConnessa}"))
            else:
                self._view.txt_result.controls.append(ft.Text(f"L'oggetto con id {intIdAdded} NON è presente nel grafo"))
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un intero"))

        self._view.update_page()
