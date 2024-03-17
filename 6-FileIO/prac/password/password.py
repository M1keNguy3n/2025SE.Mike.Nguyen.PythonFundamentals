def valid_username(username):
    bool = True
    if len(username.split()) != 1:
        bool = False
        error = "No spaces in your username."
    if len(username) < 4 or len(username) > 20:
        bool = False
        error = "Username must be shorter than 20 and longer than 4 characters."
    if username in dict.keys():
        bool = False
        error = "Username taken."
    return [bool, error]


def valid_password(password):
    bool = True
    if len(password.split()) != 1:
        bool = False
        error = "No spaces in your password."
    if len(password) < 4 or len(password) > 20:
        bool = False
        error = "Password must be shorter than 20 and longer than 4 characters."
    if password in dict.values():
        bool = False
        error = "Password taken."
    if not password.isalpha() and not password.isnum():
        bool = False
        error = "Password must contain both letters and numbers."
    return [bool, error]


def str_password(password):
    if (not password.isalpha()) and len(password) > 8:
        return "Strong"
    elif not password.isalpha():
        return "Medium"
    elif len(password) > 8:
        return "Weak"


def main():
    dict = {}
    process = input("Log in or Sign in: ")
    if process == "Sign in":
        while True:
            username = input("Enter your username: ")
            if not valid_username(username)[0]:
                print(valid_username(username)[1])
                continue
            password = input("Enter your password: ")
            if not valid_password(password)[0]:
                print(valid_password(password)[1])
                continue
            else:
                print(str_password(password))
                resp = input("Another password? y/n: ")
                if resp == "y":
                    continue
                else:
                    break
        dict["username":username, "password":password]
    else:
        pass


if __name__ == "__main__":
    main()
