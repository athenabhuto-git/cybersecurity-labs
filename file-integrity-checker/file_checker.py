import hashlib

def generate_file_hash(filename):
    """Generate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            # Read the file in chunks (useful for large files)
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    print("🔐 File Integrity Checker")
    print("1. Generate file hash")
    print("2. Verify file integrity")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        file_path = input("Enter file path: ")
        file_hash = generate_file_hash(file_path)
        if file_hash:
            print(f"SHA256 Hash: {file_hash}")
        else:
            print("⚠️ File not found!")

    elif choice == "2":
        file_path = input("Enter file path: ")
        original_hash = input("Enter the original SHA256 hash: ")
        new_hash = generate_file_hash(file_path)
        if new_hash:
            if new_hash == original_hash:
                print("✅ File integrity verified! (No changes)")
            else:
                print("❌ File has been modified!")
        else:
            print("⚠️ File not found!")

    else:
        print("Invalid choice!")
