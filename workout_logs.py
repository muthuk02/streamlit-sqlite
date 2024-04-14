
class WorkoutLogs(object):
    """Workout Logs"""

    def __init__(self, log_date, user_name, current_weight, calories_intake, calories_burned):
        self.log_date = log_date
        self.user_name = user_name
        self.current_weight = current_weight
        self.calories_intake = calories_intake
        self.calories_burned = calories_burned

    def __repr__(self):
        return f"WorkoutLogs({self.log_date},{self.user_name}, {self.current_weight}, {self.calories_intake}, {self.calories_burned})"