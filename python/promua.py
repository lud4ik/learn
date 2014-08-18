
def rev(s):
    return s[-1] + rev(s[:-1]) if s else ''


if __name__ == "__main__":
    print rev('123456789')
