import Augmentor
p = Augmentor.Pipeline("./")
p.rotate(probability=1, max_left_rotation=25, max_right_rotation=25)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.sample(30)
p.process()