from parser import parse_input, copy_files


def main():
    try:
        args = parse_input()
    except ValueError as e:
        print(f"Error: {e}")
        return

    args.dist.mkdir(exist_ok=True, parents=True)
    copy_files(args.source, args.dist)


if __name__ == "__main__":
    main()
