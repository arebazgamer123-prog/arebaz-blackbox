def score(output):
    risk = 0

    if "21/tcp open" in output:
        risk += 40

    if "80/tcp open" in output:
        risk += 10

    if "Powered by" in output:
        risk += 5

    if "443/tcp open" in output:
        risk -= 10

    if risk <= 10:
        return "LOW"
    elif risk <= 30:
        return "MEDIUM"
    else:
        return "HIGH"
