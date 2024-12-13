def is_palindrome(s):
    return str(s) == str(s)[::-1] if isinstance(s, int) else s == s[::-1]
