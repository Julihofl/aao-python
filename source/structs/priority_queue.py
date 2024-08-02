from typing import List, Tuple

class PriorityQueue:
    def __init__(self) -> None:
        self.heap: List[Tuple[int, int]] = []

    # Fügt ein Element mit einer bestimmten Priorität zur Warteschlange hinzu.
    def push(self, item: int, priotity: int) -> None:
        # Fügt das Element als Tupel (Priorität, Element) zum Heap hinzu.
        self.heap.append((priotity, item))
        # Stellt die Heap-Eigenschaft von unten nach oben wieder her.
        self._heapify_up(len(self.heap) - 1)

    # Entfernt und gibt das Element mit der höchsten Priorität (niedrigster Wert) zurück.
    def pop(self) -> int:
        # Tauscht das erste Element (höchste Priorität) mit dem letzten Element.
        self._swap(0, len(self.heap) - 1)
        # Entfernt das letzte Element (ursprünglich das erste) aus dem Heap.
        item: int = self.heap.pop()[1]
        # Stellt die Heap-Eigenschaft von oben nach unten wieder her.
        self._heapify_down(0)
        return item
    
    def empty(self) -> bool:
        return len(self.heap) == 0
    
    # Stellt die Heap-Eigenschaft von einem gegebenen Index aus nach oben wieder her.
    def _heapify_up(self, i: int) -> None:
        # Berechnet den Index des Elternelements.
        parent: int = (i - 1) // 2
        # Überprüft, ob das aktuelle Element eine höhere Priorität als sein Elternteil hat.
        if parent >= 0 and self.heap[i][0] < self.heap[parent][0]:
            # Tauscht das aktuelle Element mit seinem Elternteil.
            self._swap(i, parent)
            # Wiederholt den Prozess rekursiv für das Elternteil.
            self._heapify_up(parent)

    # Stellt die Heap-Eigenschaft von einem gegebenen Index aus nach unten wieder her.
    def _heapify_down(self, i: int) -> None:
        # Berechnet die Indizes der Kinderelemente.
        left: int = 2 * i + 1
        right: int = 2 * i + 2
        smallest: int = i

        # Überprüft, ob das linke Kind eine höhere Priorität als das aktuelle Element hat.
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        # Überprüft, ob das rechte Kind eine höhere Priorität als das aktuelle Element hat.
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        # Wenn eines der Kinder eine höhere Priorität hat, tauscht es mit dem aktuellen Element.
        if smallest != i:
            self._swap(i, smallest)
            # Wiederholt den Prozess rekursiv für das neue Kind.
            self._heapify_down(smallest)

    def _swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]