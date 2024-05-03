# Creating-Torrents-with-Scripts

Scripts that allows you to create torrent files from any directory or file on your system. This tool also supports loading tracker information from a separate text file, making it flexible for various sharing needs.

## Features

- Create torrent files for sharing files or directories.
- Load tracker URLs from a text file.
- Prompt user input for file/directory paths for flexibility and ease of use.

## Prerequisites

Before you can run the script, make sure you have Python installed on your system. Additionally, you need to install the `libtorrent` library, which can be done using pip:

```bash
pip install python-libtorrent
```

## Installation

1. Ensure you have a `trackers.txt` file in the same directory as your script. This file should contain tracker URLs, each on a new line.

## Usage

To use Create_Torrent.py, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory containing `Create_Torrent.py`.
3. Run the script with Python:

```bash
python Create_Torrent.py
```

4. When prompted, enter the full path to the directory or file you wish to share.
5. The script will create a torrent file named `output.torrent` in the same directory.

## Tracker File Format

Ensure your `trackers.txt` file follows this format:

```
http://tracker1.com:6881/announce
http://tracker2.com:6881/announce
...

Replace the example URLs with actual tracker URLs as per your requirements.

