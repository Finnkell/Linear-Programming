from manimlib.imports import *


class Jacobi(Scene):

    def construct(self):
        self.scene1()
        self.wait(2)
        self.clear()
        self.scene2()
        self.wait(2)
        self.clear()


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
