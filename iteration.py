class ParentQueue:
    def __init__(self, patients):
        self.patients = patients
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.patients):
            patient = self.patients[self.index]
            self.index += 1
            return f"Attending patient: {patient}"
        else:
            raise StopIteration

# Example usage
patient_list = ["priya", "shobi", "maha", "sadhi"]
queue = ParentQueue(patient_list)

for p in queue:
    print(p)
