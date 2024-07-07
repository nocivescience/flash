from manim import *
class LightScene(Scene):
    conf={
        
    }
    def construct(self):
        self.get_points(400)
    def get_points(self, n_points):
        points=np.array([[
            np.random.uniform(-config["frame_x_radius"]+1, config["frame_x_radius"]-1),
            np.random.uniform(-config["frame_y_radius"]+1, config["frame_y_radius"]-1),
            0
        ] for i in range(n_points)])
        dots=VGroup(*[Dot(i, radius=.03) for i in points])
        self.wait()
        flash=VMobject().set_points_as_corners(*[points]).set_stroke(width=1)
        self.play(LaggedStart(*[FadeIn(i) for i in dots]))
        self.play(ShowPassingFlash(flash, time_width=.01, run_time=10))
        self.wait()
        