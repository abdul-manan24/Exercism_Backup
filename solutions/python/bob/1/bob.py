def response(hey_bob):
    is_question = hey_bob.strip().endswith("?")
    is_yelling = hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return 'Sure.'
    if is_yelling:
        return 'Whoa, chill out!'
    if hey_bob == '' or hey_bob.isspace():
        return "Fine. Be that way!"
        
    return "Whatever."