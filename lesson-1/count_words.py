"""Count words."""


def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # Count the number of occurences of each word in s

    # decompose the string in words
    words = s.split(" ")

    # dictionnary to store distinct words
    dictionnary = {}

    # loop over words to compute occurences
    for w in words:
        if w in dictionnary:
            dictionnary[w] += 1
        else:
            dictionnary[w] = 1

    # transform dictionnary into a list of tuples
    tuples = []
    for key in list(dictionnary.keys()):
        tuples.append((key, dictionnary[key]))

    # Sort the occurences in descending order (alphabetically in case of ties)
    sortedTuples = sorted(sorted(tuples, key=lambda t: t[0]), key=lambda t: t[1], reverse=True)

    # Return the top n words as a list of tuples (<word>, <count>)
    return sortedTuples[:n]


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))

    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
