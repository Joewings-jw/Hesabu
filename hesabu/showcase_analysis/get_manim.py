from manim import *
from get_analysis import get_analysed_latex

class Hesabu(ThreeDScene):
    def __init__(self, analysed_latex, **kwargs):
        self.analysed_latex = analysed_latex
        super().__init__(**kwargs)

    def construct(self):
        original_latex = VGroup(*[MathTex(entry["latex_expr"]) for entry in self.analysed_latex])
        original_latex.arrange(DOWN, buff=0.5)
        original_latex.to_edge(UP)


        self.play(Create(original_latex), run_time=10)
        self.wait(4)


        wrong_expression_frameboxes = []
        consequential_error_frameboxes = []
        for i, element in enumerate(self.analysed_latex):
            if element["status"] == "wrong":
                wrong_expression_framebox = SurroundingRectangle(original_latex[i], buff=0.1, color=RED)
                wrong_expression_frameboxes.append(wrong_expression_framebox)

            elif element["status"] == "cons_error":
                consequential_error_framebox = SurroundingRectangle(original_latex[i], buff=0.1, color=YELLOW)
                consequential_error_frameboxes.append(consequential_error_framebox)

        wrong_expression_frameboxes_animation = Create(VGroup(*wrong_expression_frameboxes))
        consequential_error_frameboxes_animation = Create(VGroup(*consequential_error_frameboxes))

        self.play(wrong_expression_frameboxes_animation, consequential_error_frameboxes_animation)
        self.wait(4)

if __name__ == "__main__":
    analysed_latex_data = get_analysed_latex()
    hesabu_instance = Hesabu(analysed_latex_data)

    hesabu_instance.render()
