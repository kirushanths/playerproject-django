
class Result:
    ''' Generic result class, to return a boolean success with a provided message '''

    def __init__(self, success=True, message=None):
        self.success = success
        self.message = message