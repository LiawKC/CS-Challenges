Photos = int(input("How many photos do you have? "))

SDPhotos = int(input("How many SD photos do you have? "))
SDPhotosSize = SDPhotos * 2
HDPhotos = int(input("How many HD photos do you have? "))
HDPhotosSize = SDPhotos * 5
VeryHDPhotos =  int(input("How many VERY HD photos do you have? "))
VeryHDPhotosSize = SDPhotos * 10

TotalPhotos = SDPhotos + HDPhotos + VeryHDPhotos
TotalPhotosSize = SDPhotosSize + HDPhotosSize + VeryHDPhotosSize

while TotalPhotos > Photos:
    print("Try again!")
    TotalPhotos = 0
    SDPhotos = int(input("How many SD photos do you have? "))
    SDPhotosSize = SDPhotos * 2
    HDPhotos = int(input("How many HD photos do you have? "))
    HDPhotosSize = SDPhotos * 5
    VeryHDPhotos = int(input("How many VERY HD photos do you have? "))
    VeryHDPhotosSize = SDPhotos * 10
    TotalPhotos = SDPhotos + HDPhotos + VeryHDPhotos

if TotalPhotos < Photos:
    print("The rough total photo size is", TotalPhotosSize, "MB")