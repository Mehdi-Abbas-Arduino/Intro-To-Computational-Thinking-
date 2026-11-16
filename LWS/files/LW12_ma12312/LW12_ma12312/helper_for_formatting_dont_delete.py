# NOTE: Please don't delete

def dictFormatting(d):
    d = {k: sorted(v) for k, v in d.items()}
    d = dict(sorted(d.items(), key=lambda x: x[0]))
    return d