from http import HTTPStatus

class NotListTypeError(Exception):
    def __init__(self):
        self.message = {"error": "the key tags must have values type equal to a  list of strings. Example: ['#tag1', '#tag2']."
                         }, HTTPStatus.BAD_REQUEST
        super().__init__(self.message)