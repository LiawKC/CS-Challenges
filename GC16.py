name = input("PLease input your name: ")
uppercases = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercases = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbollist = ["!","@","#","$","`","~","%","^","&","*","(",")","_","-","+","=","[","{","]","}","\",",";",":","'",'"',",","<",".",">","/","?"]
qwerty = ["qw",'we','er','rt','ty','yu','ui','io','op','pa','as','sd','df','fg','gh','hj','jk','kl','lz','zx','xc','cv','vb','bn','nm']
numbercount = 0
uppercasenum = 0
lowercasenum = 0
passwordcheck = 0
symbolcount = 0

while True:
    password = input("Input your password here:")
    for i in password:
        if i in uppercases:
            uppercasenum = uppercasenum+1
        elif i in lowercases:
            lowercasenum = lowercasenum+1
        elif i in numbers:
            numbercount = numbercount+1
        elif i in symbollist:
            symbolcount = symbolcount+1
    points = 0
    if uppercasenum > 0:
        if lowercasenum > 0:
            points = points+1
            print("Password contains at least one uppercase and lowercase.")
    if symbolcount > 0:
        if numbercount > 0:
            points = points+1
            print("Password contains at least one symbol and number.")
    if len(password) > 10:
        points = points+1
        print("Password length is greater than 10.")
    if name not in password:
        points = points+1
        print("Name not in password.")
    print("Password strength:",points)

    #extension 1
    for i in range(len(password)):
        compare = password[i] + password[i+1]
        if compare in qwerty:
            break
        else:
            print("no 2 letters consecutive in qwerty")




    #extension 2
    if points < 3:
        print("Password strength: weak")
        print("Please enter a password that is medium or strong.")
    elif points == 3 or 4:
        print("Password strength: medium")
        break
    elif points >= 5:
        print("Password strength: strong")
        break
