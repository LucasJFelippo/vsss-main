class FieldF():
    def __init__(self, width, length, goal_width, goal_depth) -> None:
        self.width = width
        self.length = length
        self.goal_width = goal_width
        self.goal_depth = goal_depth

    def __str__(self) -> str:
        return "Field:\n   width: {width}\n   length: {length}\n   goal_width: {goal_width}\n   goal_depth: {goal_depth}".format(width = self.width, length = self.length, goal_width = self.goal_width, goal_depth = self.goal_depth)