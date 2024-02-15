def main():
    print('can_construct')
    print('-------------')
    target_one = "abcdef"
    wordbank_one = ["ab", "abc", "cd", "def", "abcd"]
    print(f'can_construct("{target_one}", {wordbank_one}) = {can_construct(target_one, wordbank_one)}')
    target_two = "skateboard"
    wordbank_two = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    print(f'can_construct("{target_two}", {wordbank_two}) = {can_construct(target_two, wordbank_two)}')
    target_three = "mousecatdogcatdog"
    wordbank_three = ["cat", "dog", "mouse"]
    print(f'can_construct("{target_three}", {wordbank_three}) = {can_construct(target_three, wordbank_three)}')


def can_construct(target, word_bank):
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if suffix == '' or can_construct(suffix, word_bank):
                return True
    return False


if __name__ == '__main__':
    main()
