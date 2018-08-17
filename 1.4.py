show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 
print('printing "show_version"')
print(show_version)
#show_version = show_version.strip()
#print(show_version)
fields = show_version.split()
model = fields[1]
print('#' * 80)
print('printing current value of "fields"')
print(fields)
print('#' * 80)
print('printing individual values of items in "fields" string')
for i in range(len(fields)):
    print('Index ' + str(i) + ' the first value is: ' +fields[i])
print('#' * 80)
print('The model number is: ' + fields[1])
print('#' * 80)

vendorCisco = 'cisco' in model.lower()
print('The vendor is Cisco: ' + str(vendorCisco))

#print('The vendor is: ' + )