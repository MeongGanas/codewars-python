def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    return ''.join([i for i in s if not i.isdigit()])
