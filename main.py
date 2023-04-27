
class Stack(list):
    # проверка стека на пустоту. Метод возвращает True или False
    def is_empty(self):
        return len(self) == 0

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, data):
        self.append(data)

    # удаляет верхний элемент стека.Стек изменяется.Метод возвращает верхний элемент стека
    def pop(self):
        if not self.is_empty():
            data = self[-1]
            self.__delitem__(-1)
        return data

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        if not self.is_empty():
            return self[-1]

    # возвращает количество элементов в стеке
    def size(self):
        return len(self)

def check_ballance(lists):
    stack = Stack()
    for data in lists:
        if data in res_dict:
            stack.push(data)
        elif data == res_dict.get(stack.peek()):
            stack.pop()
        else:
            return "Несбалансировано"
    return "Сбалансировано"

if __name__ == '__main__':
    balance_list = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}'
    ]
    no_balance_list = [
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]
    res_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for seq in balance_list + no_balance_list:
        print(f'{seq:<25}{check_ballance(seq)}')


