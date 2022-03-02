class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            row_count = len(self.value)
            item_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(item_count)
                ]
                for row in range(row_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Матрицы разного размера")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )


a = Matrix([
    [11, 12, 13],
    [14, 15, 16],
])

b = Matrix([
    [21, 22, 23],
    [24, 25, 26],
])

c = a + b

print(c)
#Завершено