def secret_replace(text, **replaces):
    result = ''
    replaces = {d: (v, 0) for d, v in replaces.items()}
    for i in text:
        if i in replaces:
            result += replaces[i][0][replaces[i][1] % len(replaces[i][0])]
            replaces[i] = replaces[i][0], replaces[i][1] + 1
        else:
            result += i
    return result
