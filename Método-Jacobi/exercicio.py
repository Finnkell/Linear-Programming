import pprint
import scipy
import numpy as np
import scipy.linalg  

class PL():
    def exercicio(self, text, A, b):
        determinante = np.linalg.det(A)
        if determinante != 0:
            print(f'\n{text}: determinande da matriz igual a {determinante}, existe solução única!')
            print(f'Matriz A: \n {A}')
            print(f'Matriz b: \n {b}')

            # L = scipy.linalg.cholesky(A, lower=True)
            # U = scipy.linalg.cholesky(A, lower=False)
            # print(L)
            # print(U)

            X = np.linalg.solve(A, b)



            print(f"\nSolução \n {X} \n")

            print(f'Verificando a solução fazendo A*X = b temos \n {A.dot(X)} \n --------------------------------------------------------------------------------------------')


        else:
            print(f'\n{text}: determinande da matriz igual a {determinante}, infinitas ou nenhuma solução! \n --------------------------------------------------------------------------------------------')


solve = PL()

A_1 = np.array([[1, 1, 2, -5], [2, 5, -1, -9], [2, 1, -1, 3], [1, -3, 2, 7]])
b_1 = np.array([3,-3,-11,-5])

A_2 = np.array([[1, 2, 3], [2, -1, 1], [3, 0, -1]])
b_2 = np.array([9, 8, 3])

A_4 = np.array([[1, 2, -3], [2, -1, 1], [4, -1, 1]])
b_4 = np.array([9, 0, 4])

A_3 = np.array([[3, 2, 4], [1, 1, 2], [4, 3, -2]])
b_3 = np.array([1, 2, 3])

solve.exercicio('Exercício 1', A_1, b_1)
solve.exercicio('Exercício 2', A_2, b_2)
solve.exercicio('Exercício 3', A_3, b_3)
solve.exercicio('Exercício 4', A_4, b_4)
