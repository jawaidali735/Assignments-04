#ans of question 2 in loops_controle flow

MAX_TERM_VALUE : int = 10000



def main():
    current_term = 0
    next_term = 1

    while current_term <= MAX_TERM_VALUE:
        print(current_term)
        term_after_current = current_term + next_term
        current_term = next_term
        next_term = term_after_current
    
if __name__ == '__main__':
    main()