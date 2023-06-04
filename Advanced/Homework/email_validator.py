from re import findall


class NameTooShortError(Exception):
    pass


class MustContainSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = (".com", ".bg", ".net", ".org")
name_pattern = r'\w+'
domain_pattern = r'\.[a-z]+'

user_text = input()
email = str()

while user_text != "End":
    email = user_text

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters!")
    if findall(name_pattern, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name can contain only letters, digits and underscores!")
    if "@" not in email:
        raise MustContainSymbolError("Email must contain @!")
    if findall(domain_pattern, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")

    print("Email is valid.")

    user_text = input()
