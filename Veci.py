import sys

    
def permutations(word):
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i].strip() + char.strip() + perm[i:].strip())
    return result


for user_input in sys.stdin:    
    # Get all permutations
    possbilities = permutations(user_input)
    answers = list()

    # Only keeep those which are bigger (first number only considered)
    for answer in possbilities:
        if int(answer[0]) >= int(user_input[0]):
            answers.append(answer)

    answers.sort()
    found = False

    # In case there's no answers (speed up)
    if len(answers) == 0:
        print(0)
    else:
        for answer in answers:
            if answer > user_input:
                print(answer)
                found = True
                break

    if not found:
        # If there's no answers
        print(0)