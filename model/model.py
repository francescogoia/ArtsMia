import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList = DAO.get_all_objects()     # è una lista
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def creaGrafo(self):
        self.add_edges()

    def add_edges(self):
        self._grafo.clear_edges()
        edges = DAO.get_all_connessioni(self._idMap)
        for edge in edges:
            self._grafo.add_edge(edge.v1, edge.v2, weight = edge.peso)


        # oppure ciclo sui nodi
        """        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                singleEdge = DAO.getEdge(u, v)
        """

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]
        # modo 1 predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f"Metodo 1 (predecessori): {len(predecessors.values())}")
        # modo 2 successori di v0 in DFS
        successors = nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)           # così aggiunge tutti gli elementi, anche quelli raggruppati
        print(f"Metodo 2 (successori): {len(allSucc)}")
        # modo 3 conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")            # c'è anche la source
        # modo 4 node_connected_component
        connComp = nx.node_connected_component(self._grafo, v0)
        print(f"Metodo 4 (connected comp): {len(connComp)}")        # c'è anche la source
        return len(connComp)

    def checkExistance(self, idOggetto):
        return idOggetto in self._idMap

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)