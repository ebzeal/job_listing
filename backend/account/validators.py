import os


def validate_file_extension(name):
    isValid = True

    # this returns a tuple e.g ('resume', '.pdf')
    ext = os.path.splitext(name)[1]
    # print(f'file type is {ext}')
    valid_extensions = ['.pdf']

    if not ext.lower() in valid_extensions:
        isValid = False

    return isValid
