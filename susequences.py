A = "kanagaaroo" #mother string
B = {"kanga", "roo", "apple", "nag", "kanbar", "kangaroo"} #set of words

def get_longest_word(A, B):
    possible_solutions = []
    for word in B:
        correct = False
        position = 0
        for letter in word:
            for x in range(position, len(A)):
                if letter == A[x]:
                    position+=1
                    break
        if position == len(word):
            correct = True
        if correct:
            possible_solutions.append(word)
    return possible_solutions

if __name__ == '__main__':
    possible_solutions = get_longest_word(A, B)
    print(max(possible_solutions, key=len))