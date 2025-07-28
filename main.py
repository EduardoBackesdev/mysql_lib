from lib.Comum.select import select

def main():
    select("users", ["id", "name", "email"])

if __name__ == "__main__":
    main()