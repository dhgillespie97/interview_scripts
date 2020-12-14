import ipaddress

def main():
    listOfNum = ['1.2.3.4',
'5.220.100.50',
'5.24.69.2',
'19.20.203.5',
'19.20.21.22',
'129.95.30.40']

    sortedNum=sorted(listOfNum, key = ipaddress.IPv4Address)
    for i in sortedNum:
        print(i)

if __name__ == "__main__":
    main()
