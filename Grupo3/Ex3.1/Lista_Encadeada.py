class Node:
    """Representa um nó da lista encadeada."""
    def __init__(self, value):
        self.value = value
        self.next = None  # Ponteiro para o próximo nó

class LinkedList:
    """Lista encadeada simples."""
    def __init__(self):
        self.head = None  # Início (cabeça) da lista

    def insert_at_beginning(self, value):
        """
        Insere um novo nó no início da lista.
        """
        new_node = Node(value)
        new_node.next = self.head  # Aponta para o antigo primeiro nó
        self.head = new_node       # Atualiza o head para o novo nó

    def insert_at_end(self, value):
        """
        Insere um novo nó no final da lista.
        """
        new_node = Node(value)
        if self.head is None:
            # Se a lista estiver vazia, o novo nó é o head
            self.head = new_node
        else:
            # Percorre até o último nó
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_value(self, value):
        """
        Exclui o primeiro nó que contém 'value'.
        Se o valor não existir, não faz nada.
        """
        if self.head is None:
            # Lista vazia, nada a deletar
            return

        # Se o valor a ser removido está no head
        if self.head.value == value:
            self.head = self.head.next
            return

        # Caso contrário, percorre a lista
        current = self.head
        while current.next:
            if current.next.value == value:
                # Remove o nó, ajustando o ponteiro
                current.next = current.next.next
                return
            current = current.next
        # Se chegar aqui, o valor não foi encontrado

    def display(self):
        """
        Exibe todos os elementos da lista.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) if elements else "Lista vazia.")

def test_linked_list():
    # Cria lista encadeada
    ll = LinkedList()

    # Insere no início
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(2)

    # Exibe estado atual
    print("Depois de inserir no início (2, 5, 10):")
    ll.display()

    # Insere no final
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    print("\nDepois de inserir no final (20, 30):")
    ll.display()

    # Exclui valor 5
    ll.delete_value(5)
    print("\nDepois de deletar 5:")
    ll.display()

    # Exclui valor inexistente (não faz nada)
    ll.delete_value(99)
    print("\nTentando deletar 99 (inexistente):")
    ll.display()

    # Exclui o head (2)
    ll.delete_value(2)
    print("\nDepois de deletar o head (2):")
    ll.display()

    # Exclui o valor 30
    ll.delete_value(30)
    print("\nDepois de deletar 30 (último nó):")
    ll.display()

if __name__ == "__main__":
    test_linked_list()
