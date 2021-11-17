from src.Domain.Node import Node
from src.Domain.Search import Search


class BFS(Search):
    def remove_choice(self) -> Node:
        return self.border.pop(0)

    def search(self) -> list[Node]:
        # marca todos os vértices como não visitados.
        visited = {node: False for node in self.graph.nodes}
        # pega o nó de origem, marca como visitado
        visited[self.root] = True

        while self.border:
            # retira o último vértice inserido
            s = self.remove_choice()
            self.search_path.append(s)
            # Verificando vertice adjacentes. Se um adjacente não foi visitado, marca como true e adiciona a fila para visitar
            for adj in self.graph.adj[s]:
                if not visited[adj]:
                    self.border.append(adj)
                    visited[adj] = True
                    adj.parent = s
                if s in self.destiny:
                    return self.back_tracking()

