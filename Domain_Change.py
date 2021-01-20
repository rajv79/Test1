def replace_domain(email,old_domain,new_domain):
    if "@"+old_domain in email:
        index = email.index("a"+old_domain)
        new_email = email[:index]+"@"+ new_domain
        return new_email
    return email

print("Enter your info")
print(replace_domain("rajv79@gmail.com","yahoo.com","hotmail.com"))