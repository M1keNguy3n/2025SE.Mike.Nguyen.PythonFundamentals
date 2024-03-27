def valid_username_sign_in(username, hist):
    bool = True
    error = None
    if len(username.split()) != 1:
        bool = False
        error = "No spaces in your username."
    if len(username) < 4 or len(username) > 20:
        bool = False
        error = "Username must be shorter than 20 and longer than 4 characters"
    if username in hist.keys():
        bool = False
        error = "Username taken."
    return [bool, error]


def valid_username_log_in(username):
    bool = True
    error = None
    if len(username.split()) != 1:
        bool = False
        error = "No spaces in your username."
    if len(username) < 4 or len(username) > 20:
        bool = False
        error = "Username must be shorter than 20 and longer than 4 characters"
    return [bool, error]


def valid_password_sign_in(password, hist):
    bool = True
    error = None
    if len(password.split()) != 1:
        bool = False
        error = "No spaces in your password."
    if len(password) < 4 or len(password) > 20:
        bool = False
        error = "Password must be shorter than 20 and longer than 4 characters"
    if password in hist.values():
        bool = False
        error = "Password taken."
    if not password.isalpha() and not password.isnum():
        bool = False
        error = "Password must contain both letters and numbers."
    return [bool, error]


def valid_password_log_in(password):
    bool = True
    error = None
    if len(password.split()) != 1:
        bool = False
        error = "No spaces in your password."
    if len(password) < 4 or len(password) > 20:
        bool = False
        error = "Password must be shorter than 20 and longer than 4 characters"
    if not password.isalpha() and not password.isnum():
        bool = False
        error = "Password must contain both letters and numbers."
    return [bool, error]


def str_password(password):
    if (not password.isalpha()) and len(password) > 8:
        return "Strong"
    elif not password.isalpha():
        return "Medium"
    elif len(password) < 8:
        return "Weak"


def main():
    hist = {}
    process = input("Log in or Sign in: ")
    if process.lower() == "sign in":
        while True:
            username = input("Enter your username: ")
            if not valid_username_sign_in(username, hist)[0]:
                print(valid_username_sign_in(username, hist)[1])
                continue
            password = input("Enter your password: ")
            if not valid_password_sign_in(password, hist)[0]:
                print(valid_password_sign_in(password, hist)[1])
                continue
            else:
                print(str_password(password))
                resp = input("Another password? y/n: ")
                if resp == "y":
                    continue
                else:
                    break
        hist[username] = password
        with open("accounts.txt", "w") as acc_log:
            acc_log.write(f"{username},{hist[username]}")
        if input("Would you like to log in? y/n: ") == "y":
            process = "Log in"
        else:
            return None
    if process.lower() == "log in":
        count = 0
        while count < 3:
            username = input("Enter your username: ")
            if not valid_username_log_in(username)[0]:
                print(valid_username_log_in(username)[1])
                count += 1
                continue
            if username not in hist.keys():
                print("No account with username")
                return None
            password = input("Enter your password: ")
            if not valid_password_log_in(password)[0]:
                print(valid_password_log_in(password)[1])
                count += 1
                continue
            if hist[username] != password:
                print("Wrong password.")
                count += 1
                continue
            else:
                print("Login successful.")
                return None
        print("Failed login, 3 errors made.")


if __name__ == "__main__":
    main()
