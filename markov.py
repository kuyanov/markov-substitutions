def test_function(function, tests):
    for args, ans in tests:
        out = function(*args)
        if out != ans:
            print('Error in function {};\nInput: {};\nOutput: {}\nCorrect: {}\n'.format(
                function, args, out, ans))


def apply_substitution(word, first, second):
    left = word.find(first)
    right = left + len(first)
    if left == -1:
        return (False, word)
    return (True, word[:left] + second + word[right:])

test_function(
    apply_substitution,
    [
        (('a', 'a', 'b'), (True, 'b')),
        (('abbac', 'b', 'ab'), (True, 'aabbac')),
        (('bbbc', 'a', 'b'), (False, 'bbbc'))
    ]
)


def is_final(to):
    return bool(to and to[0] == '.')

test_function(
    is_final,
    [
        (('.aaa',), True),
        (('.',), True),
        (('',), False),
        (('aaba',), False)
    ]
)


def apply_schema_once(word, schema):
    for first, second in schema:
        success, word = apply_substitution(word, first, second)
        if success:
            return (is_final(second), word)
    return (True, word)

test_function(
    apply_schema_once,
    [
        (('abb', [('ab', 'cc'), ('b', 'aaa')]), (False, 'ccb'))
    ]
)


def apply_schema(word, schema):
    while True:
        ended, word = apply_schema_once(word, schema)
        if ended:
            return word

test_function(
    apply_schema,
    [
        (('abbcb', [('ab', 'c'), ('cb', 'a'), ('aa', '.abbcb')]), '.abbcb')
    ]
)


input_file = input('Input file to read schema: ')
fin = open(input_file, 'r')
schema = [tuple(line.rstrip().split('->')) for line in fin.readlines()]
print(apply_schema(input('Enter string: '), schema))
