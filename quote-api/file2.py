class QuoteManager:
    def __init__(self):
        self.quotes = []

    def add_quote(self, text):
        if not text.strip():
            raise ValueError("Quote cannot be empty.")
        self.quotes.append(text.strip())

    def list_quotes(self):
        return self.quotes

    def search_quotes(self, keyword):
        return [q for q in self.quotes if keyword.lower() in q.lower()]


def main():
    manager = QuoteManager()
    manager.add_quote("The only limit to our realization of tomorrow is our doubts of today.")
    manager.add_quote("In the middle of difficulty lies opportunity.")
    manager.add_quote("Success is not final, failure is not fatal: It is the courage to continue that counts.")

    print("All Quotes:")
    for quote in manager.list_quotes():
        print(f"- {quote}")

    print("\nSearch Results for 'success':")
    for quote in manager.search_quotes("success"):
        print(f"- {quote}")


if __name__ == "__main__":
    main()
