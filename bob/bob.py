def hey(phrase):
    phrase = phrase.strip()
    if phrase.endswith('?') :
        if phrase.isupper() :
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif phrase.isupper() :
        return "Whoa, chill out!"
    elif phrase == "Bob" or phrase == '' :
        return "Fine. Be that way!"
    return "Whatever."
