from PIL import Image, ImageDraw
from datetime import datetime
import os

def image_report(target, risk):
    os.makedirs("reports", exist_ok=True)

    img = Image.new("RGB", (900, 500), "#0f172a")
    d = ImageDraw.Draw(img)

    d.text((40, 40), "AREBAZ BLACKBOX - SECURITY REPORT", fill="white")
    d.text((40, 100), f"Target: {target}", fill="cyan")
    d.text((40, 150), f"Risk Level: {risk}", fill="red")
    d.text((40, 200), f"Generated: {datetime.now()}", fill="gray")

    path = f"reports/{target}_report.png"
    img.save(path)

    return path
