while True:
    love_status = input ('Do you love me? y/n ')
    if love_status in ("n", "N") :
        break
    if love_status in ("y", "Y") :
        print("I love you too")