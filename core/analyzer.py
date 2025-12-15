def analyze(output):
    findings = []

    if "open" in output:
        findings.append("Open ports detected")

    if "Powered by" in output:
        findings.append("Service banner disclosure")

    if "443/tcp open" in output:
        findings.append("HTTPS service detected")

    if not findings:
        findings.append("No major issues detected")

    return findings
