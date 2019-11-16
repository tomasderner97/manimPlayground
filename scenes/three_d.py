from customutils2.manimutils.make_scene import make_scene
from manimlib.animation.creation import ShowCreation
from manimlib.mobject.coordinate_systems import ThreeDAxes
from manimlib.mobject.geometry import Circle
from manimlib.scene.three_d_scene import ThreeDScene
from manimlib.constants import *


class CameraPosition1(ThreeDScene):

    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()

        self.set_camera_orientation(phi=0 * DEGREES)

        self.play(ShowCreation(circle), ShowCreation(axes))
        self.wait()


if __name__ == '__main__':
    make_scene(CameraPosition1)
