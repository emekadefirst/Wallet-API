from src.session import add
from src.db import create_db_and_tables

def main():
    create_db_and_tables()
    # add("emeka", "edf@mail.com", "edf@mail.com")


if __name__ == "__main__":
    main()