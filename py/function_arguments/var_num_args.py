def greet(*persons, greeting_word="Hi Merry X'Mas!"):
    """
    Demonstrates variable number of positional arguments which are packed as
    a tuple

    Parameters
    ----------
    persons: tuple
        Packed as a tuple

    greeting_word: str
        default is "Hi Merry X'Mas"
    """
    print("Persons to greet:", persons)
    print("Type of persons:", type(persons))
    message = greeting_word + ", " + ", ".join(persons)
    print(message)


def mean_grade(**grades):
    """
    Function illustrating passing in variable number of keyword arguments.
    They are sent as a packed dictionary

    Parameters
    ----------
    grades: dictionary
        key word arguments
    """
    print("Grades for the total:", grades)
    print("Type of grades:", type(grades))
    total_grade = sum(grades.values())
    average_grade = total_grade / len(grades)
    print("Mean Grade:", average_grade)


def func(*args, **kwargs):
    """
    Define a function for which its number of arguments are not predetermined

    Parameters
    ----------
    args: tuple
        packed positional arguments

    kwargs: dict
        dictionary of keyword arugments
    """
    a = [arg for arg in args]
    print(a)
    kw = [(k, v) for k, v in kwargs.items()]
    print(kw)


def append_score(score, scores=[]):
    scores.append(score)
    print(f"Scores: {scores}\nScores id: {id(scores)}")
    return scores


if __name__ == '__main__':
    greet("Naz", "Rabiah", "Jehan", 'Sarah')

    print('-' * 4)
    mean_grade(Naz=5, Rabiah=5, Jehan=2)
    mean_grade(Jules=5, Brownie=5, Zico=2, Nyope=1)

    res = append_score(98)
    print(f"Scores: {res}\nres id: {id(res)}")
    res = append_score(94)
    print(f"Scores: {res}\nres id: {id(res)}")
    print('-' * 4)
    res = append_score(92, [100, 95])
    print(f"Scores: {res}\nres id: {id(res)}")
    res = append_score(92, [100, 95, 56])
    print(f"Scores: {res}\nres id: {id(res)}")

    func("Naz", "Rabiah", "Jehan", 'Sarah', Jules=5, Brownie=5, Zico=2, Nyope=1)
    func('Naz', Jules=5)

    # unpack a list into firt item, followed by the rest
    n, *rest = ['Naz', 'Rabiah', 'Jehan', 'Sarah']
    print(n)
    print(f"rest={rest}")
