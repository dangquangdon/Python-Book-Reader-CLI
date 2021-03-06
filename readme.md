# PyBookReader (WIP)

Command Line Interface (CLI) application to read a PDF book for you, utilizing the Python Text-to-Speech library `pyttsx3` and `pdftotext` and a few others.
You can have all your books stored in a directory and have `pybookreader` to scan, detect and store your books to an `SQLite` database. The database is stored locally in your computer so you don't have to worry about the books being stolen. Plus, the database only stores basic information such as book's name, path location and so on, not the book content.

This project is using `pdftotext` and so you'll need to install some dependencies that `pdftotext` requires.
## OS Dependencies

These instructions assume you're using Python 3 on a recent OS. Package names
may differ for Python 2 or for an older OS.

### Debian, Ubuntu, and friends

```
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

### Fedora, Red Hat, and friends

```
sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel
```

### macOS

```
brew install pkg-config poppler python
```

### Windows

Currently tested only when using conda:

 - Install the Microsoft Visual C++ Build Tools
 - Install poppler through conda:
   ```
   conda install -c conda-forge poppler
   ```

Reference: [pdftotext Github](https://github.com/jalan/pdftotext)

## Installation

```
pip install PyBookReader
```

## Usage

```
Usage: pybookreader [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  read-book-from-db  Read a book already stored in the database by the...
  scan-books         Scan books in a given directory
  show-all-books     Show all available books stored in the database
```

### Commands

**scan-books**

Scan the directory that given after `--location` argument and store all the books

Add `--save` flag if you want to save the books to the database after scanning them.

```
Usage: pybookreader scan-books [OPTIONS]

  Scan books in a given directory

Options:
  -l, --location TEXT  Path to the folder contains your books
  --save               Save the books after scanning them
  --help               Show this message and exit.
```

For example

```
pybookreader scan-books -l "/Users/don/Documents/Books/" --save
```

**show-all-books**

Show all available books stored in the database

Usage

```
pybookreader show-all-books
```


**read-book-from-db**

Read a book that is stored in the database by specifying its name or its ID

The book will be read from the last read page where it was stopped, or from the beginning if it's read for the first time.
You can also specify a specific page number that you want to start from, by passing `--start-from-page` argument

```
Usage: pybookreader read-book-from-db [OPTIONS]

  Read a book already stored in the database by the book's name or its ID.

Options:
  -b, --book TEXT            Name of the book you want to read
  -i, --id INTEGER           ID of the book if it is in the database
  --start-from-page INTEGER  Start reading from the specified page
  --help                     Show this message and exit.
```

Example:

```
pybookreader read-book-from-db -b "Learn Python the hard way.pdf" --start-from-page 20
```

### Stop reading

To stop reading, press `Ctrl + C`,then `pybookreader` will ask if you want to store the progress so that you can continue later on.