from typing import Annotated

import validators
from pydantic.functional_validators import AfterValidator


def check_url(url: str) -> str:
    if not validators.url(url):
        raise ValueError("Invalid URL")
    return url


UrlStr = Annotated[str, AfterValidator(check_url)]
