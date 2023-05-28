import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class ConsecutiveUnderscoresError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = (".com", ".bg", ".org", ".net")

pattern_username = r'\w+'
pattern_domain = r'\.[A-Za-z]+'

email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @ symbol!")

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email must contain only one @ symbol!")

    if "__" in email:
        raise ConsecutiveUnderscoresError("The email cannot contain consecutive underscores!")

    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters!")

    if re.findall(pattern_username, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    if re.findall(pattern_domain, email)[-1].lower() not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")

    print("Email is valid")

    email = input()
