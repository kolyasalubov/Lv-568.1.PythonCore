class Ball():
  def __init__(self, ball_type = "regular"):
    self.ball_type = ball_type

bal1 = Ball("Super")
print(bal1.ball_type)