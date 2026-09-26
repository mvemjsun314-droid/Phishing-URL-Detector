import re
from urllib.parse import urlparse


def extract_url_features(url):
    parsed = urlparse(url)

    domain = parsed.netloc

    features = {
        "URLLength": len(url),

        "DomainLength": len(domain),

        "IsDomainIP": int(
            bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", domain))
        ),

        "NoOfSubDomain": (
    0
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", domain)
    else max(len(domain.split(".")) - 2, 0)
),
        "HasObfuscation": int(
            "%" in url or "\\" in url
        ),

        "NoOfObfuscatedChar": url.count("%"),

        "NoOfLettersInURL": sum(c.isalpha() for c in url),

        "NoOfDegitsInURL": sum(c.isdigit() for c in url),

        "NoOfEqualsInURL": url.count("="),

        "NoOfQMarkInURL": url.count("?"),

        "NoOfAmpersandInURL": url.count("&"),

        "NoOfOtherSpecialCharsInURL": sum(
            not c.isalnum() and c not in "/.-_?=&:%"
            for c in url
        ),

        "IsHTTPS": int(parsed.scheme.lower() == "https"),
    }

    return features
