import arrow
from arrow.parser import ParserMatchError
from dateutil.parser import parse


def is_date(string):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """

    if string.isnumeric() or string is None:
        return False
    else:
        try:
            parse(string)
            arrow.get(string,"M/D/YYYY")
            return True

        except (ParserMatchError,ValueError,TypeError):
            return False
