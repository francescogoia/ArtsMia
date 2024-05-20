import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.clear()
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
                # fill DD
                self._view.DD_lun.disabled = False
                self._view._btn_cerca_percorso.disabled = False
                myOptsNum = list(range(2, sizeConnessa))
                myOptsDD = list(map(lambda x : ft.dropdown.Option(x), myOptsNum))
                self._view.DD_lun.options = myOptsDD            ## aggiungo le cose al DD
                self._view.update_page()


            else:
                self._view.txt_result.controls.append(ft.Text(f"L'oggetto con id {intIdAdded} NON è presente nel grafo"))
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un intero"))

        self._view.update_page()

    def handleCercaPercorso(self, e):
        try:
            path, peso = self._model.getBestPath(int(self._view.DD_lun.value), self._model.getObjFromId(int(self._view._txtIdOggetto.value)))
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Percorso trovato"
                                                          f"con peso migliore uguale a {peso}"))
            self._view.txt_result.controls.append(ft.Text(f"Percorso: "))
            for p in path:
                self._view.txt_result.controls.append(ft.Text(f"{p}"))
            self._view.update_page()

        except ValueError:
            print("Errore conversione")
