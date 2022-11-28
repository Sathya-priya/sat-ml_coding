email = input("Enter Your Email Address: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
sliced_text = f"Your user name is '{username}' and your domain is '{domain_name}'"
print(sliced_text)