from manimlib.imports import *


class Jacobi(Scene):

    def construct(self):
        # self.scene1()
        # self.wait(2)
        # self.clear()
        # self.scene2()
        # self.wait(2)
        # self.clear()
        # self.scene3()
        # self.wait(2)
        self.scene4()
        self.wait(2)

    def scene1(self):
        texto1 = TextMobject("Seja:")

        matrix1 = TexMobject("A = \\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ a_{n1} & a_{n2} & \\cdots & a_{nn} \\\ \\end{bmatrix},")
        matrix2 = TexMobject("X = \\begin{bmatrix} x_{1} \\\ x_{2} \\\ \\vdots \\\ x_{n} \\end{bmatrix} \\mbox{ e  }")
        matrix3 = TexMobject("b = \\begin{bmatrix} b_{1} \\\ b_{2} \\\ \\vdots \\\ b_{n} \\end{bmatrix}")

        texto1.to_edge(UP + LEFT)
        matrix2.move_to(matrix1, RIGHT)
        matrix3.next_to(matrix2, RIGHT)

        self.play(FadeIn(texto1))
        self.play(Write(matrix1))
        self.wait(1)
        self.play(matrix1.to_edge, LEFT, .5)
        self.play(Write(matrix2), Write(matrix3))


    def scene2(self):
        texto1 = TextMobject("$A$ pode ser decomposto como: ")
        texto2 = TexMobject("A = D + L + U", tex_to_color_map={"D": YELLOW, "U": RED, "L": GREEN})
        
        texto1.to_edge(UP + LEFT)

        self.play(Write(texto1))
        self.wait(1)
        self.play(Write(texto2))
        self.play(FadeOut(texto2))
        self.play(Write(texto2.next_to(texto1, RIGHT)))
        self.wait(1)        

        matrix_A = TexMobject("A = \\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ a_{n1} & a_{n2} & \\cdots & a_{nn} \\\ \\end{bmatrix}")
        text_A = TexMobject("A =")
        
        self.add(matrix_A)
        self.play(Write(matrix_A))
        self.wait(1)
        self.play(matrix_A.to_edge, LEFT, 1)
        self.wait(1)
        
        text_A.to_edge(LEFT, 1)

        self.play(Transform(matrix_A, text_A))
        self.wait(1)

        plus1 = TexMobject("+")
        plus2 = TexMobject("+")

        matrix_D = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\end{bmatrix}")
        matrix_D.to_edge(RIGHT - 1.5*LEFT)

        text_D = TexMobject("D", tex_to_color_map={"D": YELLOW})
        text_D.next_to(text_A, RIGHT)

        self.add(matrix_D)
        self.play(Write(matrix_D))
        self.wait(1)
        self.play(matrix_D.next_to, text_A, RIGHT)
        self.wait(1)

        self.play(Transform(matrix_D, text_D))
        self.wait(1)

        plus1.next_to(text_D, RIGHT)
        self.add(plus1)

        matrix_L = TexMobject("\\begin{bmatrix} l_{11} & 0 & \\cdots & 0 \\\ l_{21} & l_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ l_{n1} & l_{n2} & \\cdots & l_{nn} \\end{bmatrix}")
        matrix_L.to_edge(RIGHT - 1.5*LEFT)

        text_L = TexMobject("L", tex_to_color_map={"L": GREEN})
        text_L.next_to(plus1, RIGHT)

        self.add(matrix_L)
        self.play(Write(matrix_L))
        self.wait(1)
        self.play(matrix_L.next_to, plus1, RIGHT)
        self.wait(1)

        self.play(Transform(matrix_L, text_L))
        self.wait(1)

        plus2.next_to(text_L, RIGHT)
        self.add(plus2)


        matrix_U = TexMobject("\\begin{bmatrix} u_{11} & u_{12} & \\cdots & u_{1n} \\\ 0 & u_{22} & \\cdots & u_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & u_{nn} \\\ \\end{bmatrix}")
        matrix_U.to_edge(RIGHT - 1.5*LEFT)

        text_U = TexMobject("U", tex_to_color_map={"U": RED})
        text_U.next_to(plus2, RIGHT)

        self.add(matrix_U)
        self.play(Write(matrix_U))
        self.wait(1)
        self.play(matrix_U.next_to, plus2, RIGHT)
        self.wait(1)

        self.play(Transform(matrix_U, text_U))
        self.wait(1)

        self.clear()
        self.add(texto1)
        self.add(texto2)
        self.play(texto2.move_to, 0)
        self.wait(1)

        matrix = TexMobject("A = \\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\end{bmatrix} + \\begin{bmatrix} l_{11} & 0 & \\cdots & 0 \\\ l_{21} & l_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ l_{n1} & l_{n2} & \\cdots & l_{nn} \\end{bmatrix} + \\begin{bmatrix} u_{11} & u_{12} & \\cdots & u_{1n} \\\ 0 & u_{22} & \\cdots & u_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & u_{nn} \\\ \\end{bmatrix}", tex_to_color_map={
            "\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\end{bmatrix}": YELLOW,
            "\\begin{bmatrix} l_{11} & 0 & \\cdots & 0 \\\ l_{21} & l_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ l_{n1} & l_{n2} & \\cdots & l_{nn} \\end{bmatrix}": GREEN,
            "\\begin{bmatrix} u_{11} & u_{12} & \\cdots & u_{1n} \\\ 0 & u_{22} & \\cdots & u_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & u_{nn} \\\ \\end{bmatrix}": RED,
            "+": WHITE
        })

        matrix.scale(0.8)

        self.play(Transform(texto2, matrix))
        self.wait(1)
        texto = TexMobject("A = D + L + U", tex_to_color_map={"D": YELLOW, "U": RED, "L": GREEN})
        self.play(Transform(texto2, texto))
        self.wait(1)


    def scene3(self):
        texto1 = TextMobject("\\justify Logo podemos escrever $Ax = b$ como $(D+L+U)x = b$ \\\ Ou ainda, podemos transformar a equação em:")
        texto1.to_edge(UP + LEFT)
        self.play(Write(texto1))
        self.wait(1)

        texto2 = TextMobject("$$Dx = (L+ U)x + b$$ E, se $D^{-1}$ existe, então, se $a_{ii} \\neq 0$ para cada $i$, temos: $$x = D^{-1}(L +U)x + D^{-1}b$$")
        texto2.next_to(texto1, BOTTOM)
        self.play(Write(texto2))
        self.wait(1)
        self.clear()


        texto3 = TextMobject("Forma iterativa de Jacobi: $$x^{(k)} = D^{-1}(L + U)x^{(k-1)} + D^{-1}b $$")
        texto3.to_edge(UP)
        self.play(Write(texto3))
        self.wait(1)

        texto4 = TextMobject("Essa forma é mais utilizada em uma abordagem teorica, \\\ para uma abordagem mais computacional temos o seguinte: $$x^{(k)} = \\frac{1}{a_{ii}}\\left[\\sum_{j=1}^{n} (-a_{ij}x_{j}^{(k-1)}) + b_i \\right], \\quad i = 1,2, \dots, n, \\,\\, j \\neq i$$")
        texto4.next_to(texto3, BOTTOM)
        self.play(Write(texto4))


    def scene4(self):
        texto1 = TextMobject("Dado o sistema na forma $Ax = b$: ")

        sistema = TexMobject("\\begin{bmatrix} 10 & -1 & 2 & 0 \\\ -1 & 11 & -1 & 3 \\\ 2 & -1 & 10 & -1 \\\ 0 & 3 & -1 & 8 \\end{bmatrix} \\cdot \\begin{bmatrix} x_1 \\\ x_2 \\\ x_3 \\\ x_4 \\end{bmatrix} = \\begin{bmatrix} 6 \\\ 25 \\\ -11 \\\ 15 \\end{bmatrix}")

        texto1.to_edge(UP)
        sistema.next_to(texto1, BOTTOM)

        self.add(texto1)
        self.add(sistema)

        self.wait(1)
        self.clear()
        
        texto2 = TextMobject("$x^{(0)} = (0,0,0,0)$, critério de parada: $$\\frac{||x^{(k)} - x^{(k-1)}||_{\\infty}}{||x^{(k)}||_{\\infty}} < 10^{-3}$$")
        self.add(texto2)

        self.clear()

        texto3 = TextMobject("Isolando $x_{i}$: ")

        x_1 = TexMobject("x_{1} = 0x_1 + \\frac{1}{10}x_2 - \\frac{1}{5}x_3 + 0x_4 + \\frac{3}{5}", tex_to_color_map={"x_{1}": GREEN})
        x_2 = TexMobject("x_{2} = \\frac{1}{11}x_1 + 0x_2 + \\frac{1}{11}x_3 - \\frac{3}{11}x_4 + \\frac{25}{11}", tex_to_color_map={"x_{2}": RED})
        x_3 = TexMobject("x_{3} = -\\frac{1}{5}x_1 + \\frac{1}{10}x_2 + 0x_3 +\\frac{1}{10}x_4 - \\frac{11}{10} ", tex_to_color_map={"x_{3}": YELLOW})
        x_4 = TexMobject("x_{4} = 0x_1 -\\frac{3}{8}x_2 + \\frac{1}{8}x_3 + 0x_4 +\\frac{15}{8}", tex_to_color_map={"x_{4}": BLUE})

        x_1.to_edge(UP + LEFT)
        x_1.align_to(LEFT)
        x_1.shift(RIGHT)
        x_2.next_to(x_1, BOTTOM)
        x_2.align_to(x_1, LEFT)
        x_3.next_to(x_2, BOTTOM)
        x_3.align_to(x_2, LEFT)
        x_4.next_to(x_3, BOTTOM)
        x_4.align_to(x_3, LEFT)

        self.add(x_1, x_2, x_3, x_4)

        self.wait(.5)
        self.clear()
        
        texto4 = TextMobject("Aproximação inicial: $x^{(0)} = (0,0,0,0)$")
        texto4.to_edge(UP + LEFT)
        self.add(texto4)
        
        x_1 = TexMobject("x_{1}^{(1)} = \\frac{1}{10}x_2^{(0)} - \\frac{1}{5}x_{3}^{(0)} + \\frac{3}{5} = 0.6000", tex_to_color_map={"x_{1}^{(1)}": GREEN})
        x_2 = TexMobject("x_{2}^{(1)} = \\frac{1}{11}x_1^{(0)} + \\frac{1}{11}x_3^{(0)} - \\frac{3}{11}x_4^{(0)} + \\frac{25}{11} = 2.2727", tex_to_color_map={"x_{2}^{(1)}": RED})
        x_3 = TexMobject("x_{3}^{(1)} = -\\frac{1}{5}x_1^{(0)} + \\frac{1}{10}x_2^{(0)} + \\frac{1}{10}x_4^{(0)} - \\frac{11}{10} = -1.1000", tex_to_color_map={"x_{3}^{(1)}": YELLOW})
        x_4 = TexMobject("x_{4}^{(1)} = -\\frac{3}{8}x_2^{(0)} + \\frac{1}{8}x_3^{(0)} + \\frac{15}{8} = 1.8750", tex_to_color_map={"x_{4}^{(1)}": BLUE})

        equations = [x_1, x_2, x_3, x_4]

        for eq in equations:
            eq.scale(.8)

        x_1.next_to(texto4, DOWN)
        x_1.align_to(0.5*LEFT)
        x_2.next_to(x_1, BOTTOM)
        x_2.align_to(x_1, LEFT)
        x_3.next_to(x_2, BOTTOM)
        x_3.align_to(x_2, LEFT)
        x_4.next_to(x_3, BOTTOM)
        x_4.align_to(x_3, LEFT)

        self.add(x_1, x_2, x_3, x_4)
        self.wait(.5)
        self.clear()

        texto5 = TextMobject("Iterando em $x^{(k)} = (x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, x_4^{(k)})$")
        texto5.to_edge(UP + LEFT)
        self.add(texto5)

        table = """ \\def\\arraystretch{1.7}
        \\begin{tabular}{c|c|c|c|c|c|c}
            $k$ & 0 & 1 & 2 & 3 & $\\cdots$ & 10 \\\ \\hline
            $x^{(k)}_1$ & 0.0000 & 0.6000 & 1.0473 & 0.9326 & $\\cdots$ & 1.0001  \\\ 
            $x^{(k)}_2$ & 0.0000 & 2.2727 & 1.7159 & 2.053 & $\\cdots$ & 1.9998  \\\ 
            $x^{(k)}_3$ & 0.0000 & $-1.1000$ & $-0.8052$ & $-1.0493$ & $\\cdots$ & $-0.9998$  \\\ 
            $x^{(k)}_4$ & 0.0000 & 1.8750 & 0.8852 & 1.1309 & $\\cdots$ & 0.9998 \\\ \\hline
        \\end{tabular}
        """

        tabela = TexMobject(table, tex_to_color_map={})
        self.add(tabela)

        self.wait(1)
