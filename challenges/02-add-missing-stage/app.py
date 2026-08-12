"""Word counter app — the code works. Your job is to fix the pipeline."""

import sys


def count_words(text):
    return len(text.split())


def main():
    sample = "Jenkins makes CI/CD easy"
    count = count_words(sample)
    print(f'"{sample}" has {count} words')
    return count


if __name__ == "__main__":
    main()
