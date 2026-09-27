from urllib.parse import urlparse


def normalize_profile_username(value: str, platform: str) -> str:
    """Accept either a profile handle or a public profile URL."""
    value = value.strip()
    if not value:
        return ""

    if "://" not in value and (value.startswith("www.") or f"{platform}.com/" in value.lower()):
        value = f"https://{value}"

    if "://" in value:
        segments = [segment for segment in urlparse(value).path.split("/") if segment]
        if platform == "leetcode" and len(segments) > 1 and segments[0].lower() in {"u", "user"}:
            return segments[1].lstrip("@")
        return segments[0].lstrip("@") if segments else ""

    return value.lstrip("@").split("/")[0].strip()