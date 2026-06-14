class Employee:
    def __init__(self, salary):
        self.salary = salary
        self._validate_salary()

    def _validate_salary(self):  # "Internal method. Use carefully." Nothing is enforced.
        if self.salary < 0:
            raise ValueError("Invalid salary")