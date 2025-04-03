import random

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', grade={self.grade})"

def quicksort_students(students):
    """
    Ordena a lista de estudantes pelo atributo 'grade' usando QuickSort (versão simples).
    Retorna uma nova lista ordenada.
    """
    if len(students) <= 1:
        return students

    pivot = students[0].grade  # pivô simples: nota do primeiro estudante
    left = []
    right = []
    equal = []

    for student in students:
        if student.grade < pivot:
            left.append(student)
        elif student.grade > pivot:
            right.append(student)
        else:
            equal.append(student)

    return quicksort_students(left) + equal + quicksort_students(right)

def main():
    # Criando uma lista de estudantes (nome, nota) de exemplo
    students = [
        Student("Ana", 8.5),
        Student("Bruno", 7.0),
        Student("Carlos", 9.2),
        Student("Diana", 5.5),
        Student("Edu", 10),
        Student("Fernanda", 7.3)
    ]
    
    # Podemos embaralhar para simular uma lista não ordenada
    random.shuffle(students)

    print("Lista original:")
    print(students)

    # Aplica QuickSort e obtém lista ordenada
    sorted_students = quicksort_students(students)

    print("\nLista ordenada por nota (crescente):")
    print(sorted_students)

if __name__ == "__main__":
    main()
