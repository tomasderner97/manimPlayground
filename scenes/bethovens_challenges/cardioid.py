import numpy as np
from customutils2.manimutils.make_scene import make_scene, MEDIUM_QUALITY
from manimlib.animation.creation import ShowCreation
from manimlib.constants import *
from manimlib.mobject.geometry import Circle, Dot, Line, DEFAULT_DOT_RADIUS
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.scene.scene import Scene
from manimlib.utils.rate_functions import linear


class Cardioid(Scene):
    CONFIG = {
        "points": 200,
        "step": 10,
        "radius": 3,
        "line_config": {
            "stroke_width": 0.2 * DEFAULT_STROKE_WIDTH,
        },
        "dot_config": {
            "radius": 0.5 * DEFAULT_DOT_RADIUS,
        },
    }

    def construct(self):
        circle = Circle(color=YELLOW).scale(self.radius)

        points = []
        lines = []
        for point in range(self.points):
            start_angle = (point / self.points) * 2 * np.pi
            start_point = (RIGHT * np.cos(start_angle) + UP * np.sin(start_angle)) * self.radius
            points.append(start_point)

            stop_angle = (point + point * self.step) / self.points * 2 * np.pi
            stop_point = (RIGHT * np.cos(stop_angle) + UP * np.sin(stop_angle)) * self.radius
            lines.append(Line(start_point, stop_point, **self.line_config))

        self.play(ShowCreation(circle))
        self.wait()

        points_group = VGroup(*[Dot(point, **self.dot_config) for point in points])
        lines_group = VGroup(*lines)

        # self.play(ShowCreation(points_group), run_time=2)
        self.play(ShowCreation(lines_group), run_time=10, rate_func=linear)
        self.wait()


if __name__ == '__main__':
    make_scene(Cardioid,
               quality=MEDIUM_QUALITY)
