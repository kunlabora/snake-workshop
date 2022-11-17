class SnakeGame():
    def __init__(self, initial_snake_positions, food_position, field_size):
        self.snake_positions = initial_snake_positions
        self.food_position = food_position
        self.field_size = field_size

    def get_snake_positions(self):
        return self.snake_positions

    def get_food_position(self):
        return self.food_position

    def turn_snake_north(self):
        pass

    def turn_snake_south(self):
        pass

    def turn_snake_east(self):
        pass

    def turn_snake_west(self):
        pass

    def is_snake_dead(self):
        return False

    def get_head_position(self):
        return self.snake_positions[0]

    def tick(self):
        pass