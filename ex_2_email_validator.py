from ex_custom_exceptions import MustContainAtSymbolError,NameTooShortError,InvalidDomainError
command = input()
valid_domains = {"com", 'bg', 'org', 'net'}
while command != 'End':
    emails = command.split('@')
    if len(emails) != 2:
        raise MustContainAtSymbolError('Email must contain @')
    name_email, second_email_part = emails
    if len(name_email) <= 4:
       raise NameTooShortError('Name must be more than 4 characters')
    domain = second_email_part.split('.')[-1]
    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')
    command = input()








    command = input()
