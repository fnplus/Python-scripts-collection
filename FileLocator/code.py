import os
from os.path import join


def get_human_size(file_size):
    """
    Provides a human-readable size from the
    given file size (in bytes).

    :param int file_size:
        The file size to convert.

    :rtype: str
    """

    for human_size_description in [
        "bib",
        "KiB",
        "MiB",
        "GiB",
        "TiB",
        "PiB",
        "EiB",
        "ZiB",
        "YiB",
    ]:
        if file_size < 1024:
            human_size = f"{file_size:3.1f}{human_size_description}"
            break

        file_size /= 1024.0

    return human_size


if __name__ == "__main__":
    search_location = str(input("Directory Location : ")).strip()
    extension = str(input("Extension of files to search for : ")).strip()

    if extension.startswith("."):
        extension = extension[1:]

    for dirname, _, files in os.walk(search_location):
        for filename in files:
            if filename.endswith(f".{extension}"):
                the_file = os.path.join(dirname, filename)

                print(
                    get_human_size(os.path.getsize(the_file)),
                    the_file,
                )
