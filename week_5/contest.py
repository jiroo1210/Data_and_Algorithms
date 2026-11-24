
class Contest:
    def __init__(self, names, task_count):
        # TODO make a data structure
        self._score = {name:[0]*task_count for name in names}
        self._submission_count = 0
        self._submission_time = {name:0 for name in names}
        self._final_score = {}  # better to declare attributes in __init__

    def add_submission(self, name, task, score):
        # TODO update score only if they did better
        if score > self._score[name][task-1]: # index of task 0:n-1 is 1 lower than task number 1:n+1
            self._score[name][task-1] = score
            self._submission_count += 1
            self._submission_time[name] = self._submission_count

    def score_sum(self): # helper function for easier access
        self._final_score = {name:sum(score) for name, score in self._score.items()}    

    def create_scoreboard(self):
        # TODO create scoreboard:list, each element = (name,total_score)
        self.score_sum()
        sorted_score = sorted(# sort by score descending, then submission time ascending, then name ascending
            self._final_score.items(), key=lambda item: (-item[1],self._submission_time[item[0]],item[0])
            )  # using lambda; item is arbitrary variable
        return sorted_score

""" # model solution

class Contest:
    def __init__(self, names, task_count):
        self.scores = {}
        self.updated = {}
        tasks = range(1, task_count + 1)
        for name in names:
            self.scores[name] = {task: 0 for task in tasks} # better for bug fixing or generalizing
            self.updated[name] = 0
        self.counter = 0

    def add_submission(self, name, task, score):
        self.counter += 1
        if self.scores[name][task] < score:
            self.scores[name][task] = score
            self.updated[name] = self.counter

    def create_scoreboard(self):
        data = []
        for name in self.scores:
            data.append((-sum(self.scores[name].values()),
                         self.updated[name],
                         name))
        data.sort()

        scoreboard = []
        for neg_score, updated, name in data:
            scoreboard.append((name, -neg_score))
        return scoreboard
"""

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