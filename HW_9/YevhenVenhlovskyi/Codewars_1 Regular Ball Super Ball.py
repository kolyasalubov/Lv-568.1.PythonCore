## Regular Ball Super Ball

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
        print(self.ball_type)

# Ball()
Ball("super")

# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

# Test.assert_equals(Ball().с, "regular")
# Test.assert_equals(Ball("super").ball_type, "super")