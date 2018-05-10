import zipfile

def extract_file(z_file, password):
    try:
        z_file.extractall(pwd=password)
        return password
    except:
        return
def main():
    z_file = zipfile.ZipFile('password_protected_zip_file.zip')

    pass_file = open('password_containing_dictionary.txt')

    for line in pass_file.readlines():
        password = line.strip('\n')
        guess =extract_file(z_file, password)

        if guess:

            print '[+] Password = ' + password + '\n'
            exit(0)

if __name__ == '__main__':
    main()
