def title(text):
    print("\n" + "=" * 50)
    print(text.center(50))
    print("=" * 50)


def section(text):
    print("\n" + "-" * 50)
    print(text.center(50))
    print("-" * 50)


def success(msg):
    print(f"\n✅ {msg}")


def error(msg):
    print(f"\n❌ {msg}")