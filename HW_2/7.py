def brackets(n):
    open_bracket = 0
    close_bracket = 0
    answer = ''
    def process_brackets(n,open_bracket, close_bracket, answer):
        if open_bracket + close_bracket == 2 * n:
            yield answer        
        if open_bracket < n:
            yield from process_brackets(n, open_bracket + 1, close_bracket, answer + '(')
        if open_bracket > close_bracket:
            yield from process_brackets(n, open_bracket, close_bracket + 1, answer + ')')
    yield from process_brackets(n,open_bracket, close_bracket, answer)
if __name__ == '__main__':
    for seq in brackets(int(input())):
        print(seq)