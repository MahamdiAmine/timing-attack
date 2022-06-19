from constants import PASSWORD


def get_password() -> str:
    """Get password from env var or from db"""

    return PASSWORD


def check_pass(candidate_psswd: str) -> bool:
    """Stupid way to check if the password is correct"""

    actual_psswd = get_password()

    if len(candidate_psswd) != len(actual_psswd):
        return False

    for char, actual_pass_char in zip(candidate_psswd, actual_psswd):
        if char != actual_pass_char:
            return False

    return True


def check_pass_test() -> int:
    assert check_pass(PASSWORD) == True
    assert check_pass("wrong pass") == False

    return 0


if __name__ == "__main__":
    SystemExit(check_pass_test())
