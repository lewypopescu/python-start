import requests
import hashlib
import sys
import getpass


def request_api_data(query_char: str):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    try:
        res = requests.get(url, timeout=10)
    except requests.RequestException as e:
        raise RuntimeError(f'Network error: {e!r}')
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again')
    return res


def get_password_leaks_count(response, hash_tail_to_check: str) -> int:
    lines = (line.split(':') for line in response.text.splitlines())
    for hash_tail, count in lines:
        if hash_tail == hash_tail_to_check:
            return int(count)
    return 0


def pwned_api_check(password: str) -> int:
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'"{password}" was found {count} times — you should probably change your password!')
        else:
            print(f'"{password}" was NOT found. Carry on!')
    return 'done!'


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        pwd = getpass.getpass('Enter password to check (hidden): ')
        args = [pwd]
    sys.exit(main(args))
