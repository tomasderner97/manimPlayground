import numpy as np
from colour import Color
from customutils2.manimutils.make_scene import make_scene, MEDIUM_QUALITY
from manimlib.animation.composition import AnimationGroup
from manimlib.animation.fading import FadeIn, FadeOut
from manimlib.animation.growing import GrowFromCenter
from manimlib.animation.transform import ApplyMethod
from manimlib.animation.update import UpdateFromFunc
from manimlib.constants import *
from manimlib.mobject.coordinate_systems import Axes
from manimlib.mobject.geometry import Vector
from manimlib.mobject.types.vectorized_mobject import VGroup, VMobject
from manimlib.scene.scene import Scene


class Polarization(Scene):
    CONFIG = {
        "axes_scale": 0.9,
        "vector_length": 2,
        "vector_args": {
            "max_stroke_width_to_length_ratio": 10000,
            "max_tip_length_to_length_ratio": 0.95,
        },
        "xy_line_stroke_width": DEFAULT_STROKE_WIDTH / 2,
        "xy_line_color": Color("blue"),
        "path_color": Color("red"),
        "axes_color": BLACK,
        "axes_vector_color": Color("green"),
        "xy_vector_color": Color("blue"),
    }

    def construct(self):
        self.period = self.camera.frame_rate * 4
        self.phase = 0
        self.n = 0

        point_x, point_y = self.comp_point()

        self.make_axes()

        self.ellipse = VMobject(color=self.path_color).set_points([UP * point_y + RIGHT * point_x])

        self.x_vector = Vector(point_x * RIGHT, color=self.axes_vector_color, **self.vector_args)
        self.y_vector = Vector(point_y * UP, color=self.axes_vector_color, **self.vector_args)

        self.xy_vector = Vector(point_x * RIGHT + point_y * UP, color=self.xy_vector_color, **self.vector_args)

        update_group = VGroup(self.ellipse,
                              self.xy_vector,
                              self.x_vector,
                              self.y_vector,
                              )

        self.add(self.ellipse)

        self.play(FadeIn(self.x_vector), FadeIn(self.y_vector), FadeIn(self.xy_vector))
        self.play(UpdateFromFunc(update_group, self.update_stuff), run_time=8)
        self.wait(0.3)

        self.phase = np.pi / 2
        self.n = 0

        point_x, point_y = self.comp_point()
        self.play(ApplyMethod(self.y_vector.put_start_and_end_on, ORIGIN, point_y * UP),
                  ApplyMethod(self.xy_vector.put_start_and_end_on, ORIGIN, point_x * RIGHT + point_y * UP),
                  FadeOut(self.ellipse))
        self.wait(0.3)

        self.ellipse.set_points([UP * point_y + RIGHT * point_x])
        self.add(self.ellipse)
        self.play(UpdateFromFunc(update_group, self.update_stuff), run_time=8)

        self.play(FadeOut(self.ellipse))
        self.play(FadeOut(self.x_vector), FadeOut(self.y_vector), FadeOut(self.xy_vector))
        self.play(FadeOut(self.axes), FadeOut(self.axes_labels))
        self.wait()

    def make_axes(self):
        self.axes = Axes(x_min=-self.axes_scale * FRAME_X_RADIUS,
                         x_max=self.axes_scale * FRAME_X_RADIUS,
                         y_min=-self.axes_scale * FRAME_Y_RADIUS,
                         y_max=self.axes_scale * FRAME_Y_RADIUS,
                         x_axis_config={"include_ticks": False},
                         y_axis_config={"include_ticks": False},
                         number_line_config={"color": self.axes_color}
                         )
        self.axes_labels = self.axes.get_axis_labels(x_label_tex="E_x", y_label_tex="E_y").set_color(self.axes_color)

        self.play(AnimationGroup(GrowFromCenter(self.axes),
                                 FadeIn(self.axes_labels),
                                 lag_ratio=0.4))

    def update_stuff(self, *args, **kwargs):
        if self.n > 2 * self.period:
            return
        point_x, point_y = self.comp_point()
        if self.n <= self.period:
            self.ellipse.add_points_as_corners([UP * point_y + RIGHT * point_x])
        self.x_vector.put_start_and_end_on(ORIGIN, point_x * RIGHT)
        self.y_vector.put_start_and_end_on(ORIGIN, point_y * UP)
        self.xy_vector.put_start_and_end_on(ORIGIN, point_x * RIGHT + point_y * UP)

        self.n += 1

    def comp_point(self):
        point_x = self.vector_length * np.cos(2 * np.pi * self.n / self.period) * RIGHT + 0.01 * RIGHT
        point_y = self.vector_length * np.cos(2 * np.pi * self.n / self.period + self.phase) * UP + 0.01 * UP
        return point_x, point_y


if __name__ == '__main__':
    make_scene(Polarization,
               quality=MEDIUM_QUALITY,
               frame_rate=24,
               color="white",
               )
