str = input("Enter the file name: ").lower().replace(" ", "")
match str[-4::]:
    case ".jpg":
        print("image/jpg")
    case ".jpeg":
        print("image/jpeg")
    case ".txt":
        print("text/txt")
    case ".pdf":
        print("document/pdf")
    case ".zip":
        print("compressed/zip")
    case ".png":
        print("image/png")
    case other:
        print("application/octet-stream")
