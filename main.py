class Low_level_static_array:
    def __init__(self, size: int):  # выделим память под статический массив
        self.memory = []
        for _ in range(size):
            self.memory.append(None)
        print(self.memory, "выделено памяти")

    def get_fill_len(self):  # вычисление занятого места (ну и индекса последнего элемента)
        return len(self.memory) - self.memory.count(None)

    def append(self, value, index=0):  # вставка (или добавление в конец) элемента на позицию
        ind = self.get_fill_len()
        if index < 0 or index > len(self.memory):  # вне разрешенного диапазона
            raise IndexError
        if ind + 1 < index or index == 0:
            index = ind + 1
        while ind >= index:
            self.memory[ind] = self.memory[ind - 1]
            ind -= 1
        self.memory[ind] = value
        print(self.memory, f" --- '{value}' добавлен на позицию № {index}")

        return self.memory

    def delete(self, index=0):  # удаление по индексу (или удаление последнего)
        ind = self.get_fill_len()
        if index > ind or index < 0 or ind < 1:
            raise IndexError
        if ind + 1 < index or index == 0:
            index = ind + 1
        while ind > index:
            self.memory[index - 1] = self.memory[index]
            index += 1
        value = self.memory[ind - 1]
        self.memory[ind - 1] = None
        print(self.memory, f" --- '{value}' удалён с позиции № {ind}")
        return value

    def get_elem(self, index):  # получение элемента по индексу
        ind = self.get_fill_len()
        if index > ind or index < 1:
            raise IndexError
        print(f"{index}-й элемент равен {self.memory[index - 1]!r}")
        return self.memory[index - 1]

    def set_elem(self, index, value):  # изменение значения элемента на новое по его индексу
        ind = self.get_fill_len()
        if index > ind or index < 1:
            raise IndexError
        self.memory[index - 1] = value
        print(self.memory, f" --- элемент № {index} изменен на '{value}'")

    def __str__(self):
        return self.memory


def main():
    # демонстрация работы
    arr = Low_level_static_array(5)
    arr.append("1")
    arr.append("2")
    arr.append("3")
    arr.append("4", 2)
    # arr.append("4",6)  # error
    # arr.append("5",5)
    # arr.append("6")  # error
    arr.set_elem(3, "8")
    # arr.set_elem(5,"8")  # error
    arr.get_elem(2)
    # arr.get_elem()  # error
    # arr.get_elem(5)  # error
    arr.delete(3)
    arr.delete()
    arr.delete()
    arr.delete()
    # arr.delete()  # error


if __name__ == "__main__":
    main()
