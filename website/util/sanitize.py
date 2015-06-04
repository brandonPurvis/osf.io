import bleach


#Thank you Lyndsy
def strip_html(unclean):
    """Sanitize a string, removing (as opposed to escaping) HTML tags

    :param unclean: A string to be stripped of HTML tags

    :return: stripped string
    :rtype: str
    """
    return bleach.clean(unclean, strip=True, tags=[], attributes=[], styles=[])


def clean_tag(data):
    """Format as a valid Tag

    :param data: A string to be cleaned

    :return: cleaned string
    :rtype: str
    """
    #TODO: make this a method of Tag?
    return escape_html(data).replace('"', '&quot;').replace("'", '')


def escape_html(data):
    """Escape HTML characters in data.

    :param data: A string, dict, or list to clean of HTML characters

    :return: A cleaned object
    :rtype: str or list or dict
    """
    if isinstance(data, dict):
        return {
            key: escape_html(value)
            for (key, value) in data.iteritems()
        }
    if isinstance(data, list):
        return [
            escape_html(value)
            for value in data
        ]
    if isinstance(data, basestring):
        return bleach.clean(data)
    return data


def assert_clean(data):
    """Ensure that data is cleaned

    :raise: AssertionError
    """
    def _ensure_clean(value):
        if value != bleach.clean(value):
            raise ValueError

    return escape_html(data)


# TODO: Remove safe_unescape_html when mako html safe comes in
def safe_unescape_html(data):
    """
    Return data without html escape characters.

    :param data: A string, dict, or list
    :return: string or list or dict

    """
    safe_characters = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
    }
    if isinstance(data, dict):
        return {
            key: safe_unescape_html(value)
            for (key, value) in data.iteritems()
        }
    if isinstance(data, list):
        return [
            safe_unescape_html(value)
            for value in data
        ]
    if isinstance(data, basestring):
        for escape_sequence, character in safe_characters.items():
            data = data.replace(escape_sequence, character)
        return data
    return data