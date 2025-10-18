from stats import word_count, letters, dictionary
import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]    
    text = get_book_text(book_path)
    wrd_cnt = word_count(text)
    letrs = letters(text)
    
    dict_list = dictionary(letrs)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wrd_cnt} total words")
    print("--------- Character Count -------")

    for dict in dict_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")

main()
    
