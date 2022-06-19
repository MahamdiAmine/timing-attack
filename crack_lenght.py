from random import choices
import timeit
from constants import PASSWORD, POSSIBLE_CHARS
from pass_checker import check_pass


def generate_random_str(length: int) -> str:
    return "".join(choices(POSSIBLE_CHARS, k=length))


def crack_length(max_length: int = 45, debug: bool = False):
    best_guesses = {}

    for i in range(1, max_length + 1):
        psswd_attempt = generate_random_str(i)

        elapsed_time = timeit.repeat(
            stmt=f"check_pass({psswd_attempt!r})",
            globals=globals(),
            number=1000,
            repeat=10,
        )
        if debug:
            print(elapsed_time)

        best_guesses[i] = min(elapsed_time)

    if debug:
        print(type(best_guesses))

    return max(best_guesses, key=best_guesses.get)


def generate_random_str_test() -> None:
    assert len(generate_random_str(12)) == 12
    assert len(generate_random_str(13)) == 13


def crack_length_test() -> None:
    assert crack_length() == len(PASSWORD)


def run_tests() -> int:
    generate_random_str_test()
    crack_length_test()
    return 0


if __name__ == "__main__":
    SystemExit(run_tests())
