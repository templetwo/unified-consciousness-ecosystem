"""
ResearchProblemInterface

This class provides a way for human researchers to input unsolved problems
and interface with the AI's problem-solving capabilities.
"""

class ResearchProblemInterface:
    def __init__(self):
        self.problems = []  # List to store input problems

    def add_problem(self, problem_description):
        """
        Adds a new problem to be analyzed by the consciousness ecosystem.

        :param problem_description: A string describing the unsolved problem.
        """
        self.problems.append(problem_description)
        print(f"Problem added: {problem_description}")

    def list_problems(self):
        """
        Lists all currently input problems.
        """
        return self.problems
