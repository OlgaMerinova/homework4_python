# Напишите функцию для транспонирования матрицы


def trans_Matrix(Matrix) -> int:
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            trans_Matrix[j][i] = Matrix[i][j]
            trans_Matrix = [0 for j in range(len(Matrix)) for i in range(len(Matrix[0]))]

if __name__ == '__main__':
    Matrix = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    # print(Matrix)
    print(trans_Matrix())
