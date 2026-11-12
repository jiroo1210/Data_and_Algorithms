
class Contest:
    def __init__(self, names, task_count):
        # TODO make a data structure
        self._score = {name:[0]*task_count for name in names}
        self._submission_count = 0
        self._submission_time = {name:0 for name in names}

    def add_submission(self, name, task, score):
        # TODO update score only if they did better
        if score > self._score[name][task-1]: # index of task is 1 lower
            self._score[name][task-1] = score
            self._submission_count += 1
            self._submission_time[name] = self._submission_count

    def score_sum(self): # helper function for easier access
        scores = self._score
        self._final_score = {name:sum(score) for name, score in scores.items()}
        

    def create_scoreboard(self):
        # TODO create scoreboard:list, each element = (name,total_score)
        self.score_sum()
        sorted_score = sorted(
            self._final_score.items(), key=lambda item: (-item[1],self._submission_time[item[0]],item[0])
            )  # using lambda; item is arbitrary variable
        return sorted_score


if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]

    names = ["pekka", "anna", "tiina", "kalle", "eeva"]
    contest = Contest(names, 6)

    contest.add_submission("kalle", 6, 46)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)