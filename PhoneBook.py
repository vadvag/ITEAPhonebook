def createrecord(phones,username,phonenum):
    """ testing createrecord function
    >>> phones = {}
    >>> createrecord(phones,"John","322233")
    >>> phones
    {'John': '322233'}
    >>> createrecord(phones,"John","322233")
    Traceback (most recent call last):
        ...
    ValueError: This username are already exist
    """
    if username in phones:
        raise ValueError("This username are already exist")
    else:
        phones[username] = phonenum


def readrecord(phones,username,phonenum):
    """ testing readrecord function
    >>> phones = {}
    >>> phones["John"] = "322233"
    >>> phones
    {'John': '322233'}
    >>> readrecord(phones,"John","5555555")
    Traceback (most recent call last):
        ...
    ValueError: John:322233
    >>> readrecord(phones,"Steave","9999999")
    Traceback (most recent call last):
        ...
    ValueError: This username are not exist
    """
    if username in phones:
        raise ValueError(username+ ":"+phones[username])
    else:
        raise ValueError("This username are not exist")
        
    
def updaterecord(phones,username,phonenum):
    """ testing updaterecord function
    >>> phones = {}
    >>> phones["John"] = "322233"
    >>> phones
    {'John': '322233'}
    >>> updaterecord(phones,"John","5555555")
    >>> phones
    {'John': '5555555'}
    >>> updaterecord(phones,"Steave","5555555")
    Traceback (most recent call last):
        ...
    ValueError: This username are not exist
    """
    if username in phones:
        phones[username] = phonenum
    else:
        raise ValueError("This username are not exist")

        
def deleterecord(phones,username,phonenum):
    """ testing deleterecord function
    >>> phones = {}
    >>> phones["John"] = "322233"
    >>> phones
    {'John': '322233'}
    >>> deleterecord(phones,"Steave","5555555")
    Traceback (most recent call last):
        ...
    ValueError: This username are not exist
    >>> deleterecord(phones,"John","5555555")
    >>> phones
    {}
    """
    if username in phones:
        del phones[username]
    else:
        raise ValueError("This username are not exist")


def mainread(typeformat):
    def read_pickle(dbase):
        import pickle
        print("read_pickle")
        return pickle.load(dbase)
    
    def read_csv(dbasename):
        import csv
        print("read csv")
        r = csv.DictReader(dbasename)
        for row in r:
            print(row)
            return row
        return dict()

    def read_json(dbasename):
        import json
        print('read json')
        s = json.loads(dbasename.read())
        return s
        
    try:
        if typeformat == "pickle":
            fks = 'rb'
        else:
            fks = 'rt'
        with open("phoneDB",fks) as f:
            if typeformat == "pickle":
                return read_pickle(f)
            elif typeformat == "csv":
                return read_csv(f)
            elif typeformat == "json":
                return read_json(f)
    except:
        print("Error reading file")
        return dict()
        

def mainwrite(typeformat, phones):
    def write_pickle(phones):
        import pickle
        print("write_pickle")
        try:
            with open("phoneDB","wb") as f:
                pickle.dump(phones,f)
        except:
            print("Error writing pickle-file")
        return None

    def write_csv(phones):
        import csv
        print('write csv')
        print(phones)
        try:
            with open("phoneDB","wt") as f:
                w = csv.DictWriter(f,phones.keys())
                w.writeheader()
                w.writerow(phones)
        except:
            print('Error writing csv-file')
        return None

    def write_json(dbasename):
        import json
        print('write json')
        try:
            with open('phoneDB','wt') as f:
                f.write(json.dumps(phones))
        except:        
            print('Error writing json-file')
        return None    
    
    if typeformat == "pickle":
        return write_pickle(phones)
    elif typeformat == "csv":
        return write_csv(phones)
    elif typeformat == "json":
        return write_json(phones)

    
def createconfig(path):
    import configparser
    c = configparser.ConfigParser()
    c.add_section('settings')
    c.set('settings', 'file_type', 'csv')
    with open(path,'wb') as f:
        c.write(f)


def initialise():
    import configparser
    import os
    path = 'PhonesCNF'
    if not os.path.exists(path):
        createconfig(path)
    c = configparser.ConfigParser()
    c.read(path)
    return c.get('settings', 'file_type')
    

typeformat = initialise()
phones = mainread(typeformat)
print(phones)
while True:
    username = input("Enter username: ")
    phonenumber = input("Enter phone number: ")
    print("Enter operation code: ")
    print("c - create; r - read; u - update; d - delete; q - quit ")
    usercommand = input()
    try:
        if usercommand == "c":
            createrecord(phones,username,phonenumber)
            mainwrite(typeformat,phones)
        elif usercommand == "r":
            readrecord(phones,username,phonenumber)
        elif usercommand == "u":
            updaterecord(phones,username,phonenumber)
            mainwrite(typeformat,phones)
        elif usercommand == "d":
            deleterecord(phones,username,phonenumber)
            mainwrite(typeformat,phones)
        elif usercommand == "q":
            break
        else:
            print("Incorect command!")
        print(phones)
    except ValueError as e:
        print(e)
