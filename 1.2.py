ipAddr = (input('please enter an IP '))
octets = ipAddr.split('.')
print("\n")

print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print('-' * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("\n")
print('-' * 60)


