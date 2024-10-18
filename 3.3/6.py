{x: text.lower().count(x) for x in text.lower().replace(' ', '') if x.isalpha()}
