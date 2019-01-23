from hashlib import md5

def hexdigest(filepath):
    hasher = md5()
    with open(filepath, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

