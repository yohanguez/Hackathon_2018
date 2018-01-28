import hashlib


def gravatar(email, size=100, default='identicon', rating='g', request = "is_secure"):
    if request == "is_secure":
        url = 'https://secure.gravatar.com/avatar'
    else:
        url = 'http://www.gravatar.com/avatar'
    hash = hashlib.md5(email.encode('utf-8')).hexdigest()

    return '{url}/{hash}'.format(url=url, hash=hash)