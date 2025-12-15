import subprocess

def scan(target, mode):
    profiles = {
        "1": f"nmap -T4 -F {target}",
        "2": f"nmap -A -p- {target}",
        "3": f"nmap -p 80,443 --script http-enum {target}",
        "4": f"nmap -p 443 --script ssl-cert {target}"
    }

    command = profiles.get(mode)

    if not command:
        return "Invalid scan option selected."

    try:
        result = subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )
        return result
    except subprocess.CalledProcessError as e:
        return e.output
