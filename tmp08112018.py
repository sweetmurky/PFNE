ip1 = '1.2.3.4'
ip2 = '2.2.3.4'
ip3 = '3.2.3.4'
octets1 = ip1.split('.')

ipString = ['1.2.3.4', '2.2.3.4', '3.2.3.4']
print("\n")
print("-" * 80)
print("{:<20}{:>20}{:>20}".format(ip1, ip2, ip3))

print("\n")
print("-" * 80)
print(octets1)

print("\n")
print("-" * 80)
print(ipString)

for i in range(len(ipString)):
    print('Index ' + str(i) + ' the ip address list is: ' +ipString[i])
    


