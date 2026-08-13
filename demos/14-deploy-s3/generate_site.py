"""Copy index.html into site/ and fill in Jenkins build placeholders."""

import os
from datetime import datetime, timezone
from pathlib import Path

DEMO_DIR = Path(__file__).resolve().parent
TEMPLATE = DEMO_DIR / "index.html"
SITE_DIR = DEMO_DIR / "site"
OUTPUT = SITE_DIR / "index.html"


def main():
    html = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "{{SITE_TITLE}}": os.environ.get("SITE_TITLE", "Jenkins Workshop Site"),
        "{{S3_BUCKET}}": os.environ.get("S3_BUCKET", "(not set)"),
        "{{BUILD_NUMBER}}": os.environ.get("BUILD_NUMBER", "local"),
        "{{JOB_NAME}}": os.environ.get("JOB_NAME", "demo-14-deploy-s3"),
        "{{GENERATED_AT}}": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    }
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    SITE_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
