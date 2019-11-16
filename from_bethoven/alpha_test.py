from customutils2.manimutils.make_scene import make_scene
from manimlib.animation.update import UpdateFromAlphaFunc
from manimlib.mobject.geometry import Circle, Square
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.scene.scene import Scene
from manimlib.constants import *
from manimlib.utils.rate_functions import linear


class AlphaTest(Scene):

    def construct(self):
        circle = Circle()
        square = Square()

        self.add(circle)
        self.add(square)

        self.play(UpdateFromAlphaFunc(circle, self.update_stuff),
                  UpdateFromAlphaFunc(square, self.update_stuff, rate_func=linear))

        self.wait()

    def update_stuff(self, mobject: VMobject, alpha):
        mobject.move_to(alpha * (UP + LEFT))


if __name__ == '__main__':
    make_scene(AlphaTest,
               video_dir="../video",
               tex_dir="../tex")
