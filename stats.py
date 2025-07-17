def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def count_words(file_content):
    num_words = len(file_content.split())
    return f"{num_words}"

def count_caracters(file_content):
    caracter_count = {}
    for c in file_content:
        c_lower = c.lower()
        if c_lower in caracter_count:
            caracter_count[c_lower] += 1
        else:
            caracter_count[c_lower] = 1
    return caracter_count