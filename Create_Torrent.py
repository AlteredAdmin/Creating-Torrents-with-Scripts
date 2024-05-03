import libtorrent as lt

# Load trackers from a text file
with open('trackers.txt', 'r') as f:
    trackers = [line.strip() for line in f if line.strip()]

# Prompt the user for the directory or file to share
path_to_share = input("Enter the path to the directory or file you want to share: ")

# Create a new `file_storage` object
fs = lt.file_storage()

# Add files to this object
lt.add_files(fs, path_to_share)

# Create torrent creation parameters
piece_size = 512 * 1024  # 512 KiB piece size
create_torrent_params = {
    'trackers': trackers,
    'piece_size': piece_size
}

# Create the torrent
tor = lt.create_torrent(fs, **create_torrent_params)

# Save the torrent to a file
with open('output.torrent', 'wb') as f:
    f.write(lt.bencode(tor.generate()))

print("Torrent file created as 'output.torrent'")
