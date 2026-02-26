"""This script is used for filename sanitizing purposes."""

def sanitize_filename(filename:str) -> str:
    """Replace every potential forbidden characters from the given file name by underscores, converts and returns the resulting path into lower case."""

    sanitized_name = ""

    # List of potentially forbidden characters
    forbidden_chars = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]

    for character in filename:
        if character in forbidden_chars:
            sanitized_name += "_"

        else:
            sanitized_name += character


    return sanitized_name.lower()            

