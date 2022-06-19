import itertools
import timeit

from crack_lenght import POSSIBLE_CHARS, crack_length, generate_random_str
from pass_checker import check_pass


def crack_psswd(length: int, debug: bool = False):
    curr_guess = generate_random_str(length)
    counter = itertools.count()

    while True:
        idx = next(counter) % length  # Next index to change
        for c in POSSIBLE_CHARS:
            alt_guess = curr_guess[:idx] + c + curr_guess[idx + 1 :]

            alt_time = timeit.repeat(
                stmt="check_pass(alt)",
                setup=f"alt={alt_guess!r}",
                globals=globals(),
                number=1000,
                repeat=10,
            )

            curr_guess_time = timeit.repeat(
                stmt="check_pass(p)",
                setup=f"p={curr_guess!r}",
                globals=globals(),
                number=1000,
                repeat=10,
            )

            # If alt guess was slower, then it's more correct.
            if min(alt_time) > min(curr_guess_time):
                curr_guess = alt_guess
                if debug:
                    print(curr_guess)

            if check_pass(alt_guess):
                return alt_guess


def demo_attack() -> int:
    # 1. crack length
    length = crack_length()
    print(f"the password length is {length}")

    # 2. crack pasword
    password = crack_psswd(length, debug=True)

    print("Password was cracked successfully")
    print(f"your password is {password}")

    return 0


if __name__ == "__main__":
    SystemExit(demo_attack())
