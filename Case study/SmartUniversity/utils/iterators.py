class CourseIterator:

    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration
        course = self.courses[self.index]
        self.index += 1
        return course