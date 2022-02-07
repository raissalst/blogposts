from app.exc.not_list_type_error import NotListTypeError

def check_if_is_list(tags):
        if type(tags) == list:
            return tags
        else:
            raise NotListTypeError