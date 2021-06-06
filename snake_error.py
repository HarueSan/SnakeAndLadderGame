class HeadSnakeLessThanTailSnake(Exception):

    def __init__(self, snake: "Snake") -> None:
        self.snake = snake

    def __str__(self) -> str:
        return f"{self.snake.head}  less than {self.snake.tail}"


class HeadSnakeEqualTailSnake(Exception):

    def __init__(self, snake: "Snake") -> None:
        self.snake = snake

    def __str__(self) -> str:
        return f"{self.snake.head}  equal {self.snake.tail}"


class HeadEqualStartPoint(Exception):

    def __init__(self, snake: "Snake") -> None:
        self.snake = snake

    def __str__(self) -> str:
        return f"{self.snake.head}  equal start point"


class SnakeSyntaxInputError(Exception):

    def __init__(self, snake: "Snake") -> None:
        self.snake = snake

    def __str__(self) -> str:
        return f"{self.snake.head} or {self.snake.tail} is Negative number or zero"
