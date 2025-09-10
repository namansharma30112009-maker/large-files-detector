import os

# 🔧 Settings
target_extensions = ['.vdi', '.vhdx', '.iso', '.zip', '.exe']
min_size_mb = 500
scan_root = 'C:\\'  # You can change this to scan a specific folder

def bytes_to_mb(size_bytes):
    return round(size_bytes / (1024 * 1024), 2)

def scan_large_files():
    print(f"🔍 Scanning {scan_root} for files over {min_size_mb}MB...")
    for root, dirs, files in os.walk(scan_root):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                ext = os.path.splitext(file)[1].lower()
                if ext in target_extensions:
                    size = os.path.getsize(file_path)
                    if size >= min_size_mb * 1024 * 1024:
                        print(f"📁 {file_path} — {bytes_to_mb(size)} MB")
            except Exception as e:
                pass  # Skip inaccessible files

scan_large_files()
