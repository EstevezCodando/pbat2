class DNode:
    """
    Nó para lista duplamente encadeada.
    Armazena um valor e ponteiros para o nó anterior (prev) e para o próximo nó (next).
    """
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Lista duplamente encadeada com ponteiros para o nó cabeça (head) e cauda (tail).
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # Para facilitar a remoção por índice, podemos manter o tamanho

    def insert_at_beginning(self, value):
        """
        Insere um novo nó no início (head) da lista.
        """
        new_node = DNode(value)
        if self.head is None:
            # Lista vazia
            self.head = new_node
            self.tail = new_node
        else:
            # Conecta o novo nó com o antigo head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, value):
        """
        Insere um novo nó no final (tail) da lista.
        """
        new_node = DNode(value)
        if self.head is None:
            # Lista vazia
            self.head = new_node
            self.tail = new_node
        else:
            # Conecta o novo nó com o antigo tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_at_position(self, pos):
        """
        Exclui o nó na posição 'pos' (0-based).
        Se pos for inválido, não faz nada ou gera um erro.
        """
        if pos < 0 or pos >= self.size:
            print(f"Posição {pos} inválida para remoção.")
            return  # ou poderíamos levantar uma exceção

        # Caso especial: remover o head
        if pos == 0:
            removed_node = self.head
            # Se só houver um elemento
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                # Ajusta o head para o próximo
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return

        # Caso especial: remover o tail
        if pos == self.size - 1:
            removed_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        # Caso geral: percorrer até a posição
        # (para performance, poderíamos decidir se é mais perto do head ou tail,
        # mas aqui faremos de modo simples, sempre do head)
        current = self.head
        current_index = 0
        while current_index < pos:
            current = current.next
            current_index += 1

        # "Desencaixa" o nó atual da lista
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1

    def display_forward(self):
        """
        Exibe todos os elementos da lista na ordem head → tail.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print("Forward: " + " <-> ".join(elements) if elements else "Lista vazia (forward).")

    def display_backward(self):
        """
        Exibe todos os elementos da lista na ordem tail → head.
        """
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev
        print("Backward: " + " <-> ".join(elements) if elements else "Lista vazia (backward).")
def test_doubly_linked_list():
    dll = DoublyLinkedList()

    # Inserir no início
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(5)
    dll.insert_at_beginning(2)  # Lista deve ser [2, 5, 10]

    # Inserir no final
    dll.insert_at_end(20)
    dll.insert_at_end(30)       # Lista deve ser [2, 5, 10, 20, 30]

    print("Depois das inserções:")
    dll.display_forward()
    dll.display_backward()

    # Excluir nó na posição 0 (head)
    dll.delete_at_position(0)   # Remove 2
    print("\nDepois de remover o nó na posição 0 (valor 2):")
    dll.display_forward()
    dll.display_backward()

    # Excluir nó no final (posição size-1)
    dll.delete_at_position(dll.size - 1)  # Remove 30
    print("\nDepois de remover o último nó (valor 30):")
    dll.display_forward()
    dll.display_backward()

    # Excluir nó no meio, por exemplo posição 1 (atual)
    # Agora a lista está [5, 10, 20], então posição 1 é o valor 10
    dll.delete_at_position(1)
    print("\nDepois de remover a posição 1 (valor 10):")
    dll.display_forward()
    dll.display_backward()

    # Tentar remover posição inválida
    dll.delete_at_position(100)
    print("\nTentando remover posição 100 (inexistente):")
    dll.display_forward()
    dll.display_backward()

    # Resultado final esperado: [5, 20]
    print("\nLista final esperada: [5, 20] (ordem forward)")

if __name__ == "__main__":
    test_doubly_linked_list()
