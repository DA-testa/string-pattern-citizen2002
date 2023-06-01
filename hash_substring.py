def read_input():
    pattern=""
    text=""
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':   
        with open(f"./tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    answer = []
    pattern_len = int(len (pattern))
    text_len = int(len(text))
    return answer

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

