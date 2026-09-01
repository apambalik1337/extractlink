# 🔗 Link Extractor

**Extract URLs from a text file quickly and effortlessly.**

Link Extractor is a lightweight Python command-line tool designed to scan a `.txt` file and automatically extract all HTTP and HTTPS URLs found inside it.

Instead of manually searching through a large text file for links, Link Extractor finds them automatically and saves the extracted URLs into a separate result file.

---

## ✨ Features

* 🔗 Automatically detect HTTP and HTTPS URLs
* 📄 Read links directly from `.txt` files
* ⚡ Fast and lightweight
* 💾 Automatically save extracted links
* 📁 Creates a separate result file
* 🎨 Simple colored terminal output
* 🐍 Built with Python
* 📦 No external packages required

---

## 🛠️ Requirements

You only need:

```text
Python 3.x
```

The tool uses Python's built-in libraries:

```python
re
os
```

No additional packages are required.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Link-Extractor.git
```

### 2. Navigate to the project directory

```bash
cd Link-Extractor
```

### 3. Run the tool

```bash
python main.py
```

---

## 💻 Usage

Run the program:

```bash
python main.py
```

The tool will ask you to provide the path to a `.txt` file.

Example:

```text
Example: /home/user/Desktop/text.txt

Please enter the path of the input text file (.txt):
```

Enter your file path:

```text
/home/user/Desktop/text.txt
```

The program will scan the file and extract all URLs.

---

## 📸 Example

### Input File

Suppose `text.txt` contains:

```text
Welcome to my website:
https://example.com

You can also visit:
https://github.com
https://google.com

More information:
https://example.org/about
```

Run the tool:

```text
Please enter the path of the input text file (.txt): text.txt
```

Output:

```text
Links found in the input file:

https://example.com
https://github.com
https://google.com
https://example.org/about

Output (result) saved to: text_result.txt
```

---

## 📄 Output File

The tool automatically creates a new file using the original filename.

For example:

```text
text.txt
```

will produce:

```text
text_result.txt
```

The result file contains:

```text
Links found in the input file:

https://example.com
https://github.com
https://google.com
https://example.org/about
```

---

## 🧠 How It Works

Link Extractor reads the entire text file:

```python
with open(file_path, "r") as file:
    contents = file.read()
```

It then uses a regular expression to identify URLs beginning with `http://` or `https://`:

```python
links = re.findall(r'(https?://\S+)', contents)
```

The detected links are displayed in the terminal and saved to a new result file.

---

## 🔄 Workflow

```text
       📄 TXT File
           │
           ▼
     Link Extractor
           │
           ▼
      Scan Contents
           │
           ▼
     Detect HTTP/HTTPS
           │
           ▼
      Extract URLs
           │
           ▼
     📋 Display Results
           │
           ▼
     💾 Save Result File
```

---

## 📂 Project Structure

```text
Link-Extractor/
│
├── main.py
├── README.md
└── example_result.txt
```

> The result file is generated automatically when links are found.

---

## 🔍 Supported URL Types

The tool can detect URLs such as:

```text
https://example.com
http://example.com
https://github.com/user/repository
https://example.com/page?id=123
https://subdomain.example.com/path
```

---

## ⚠️ Notes

The current URL detection method is designed for straightforward HTTP and HTTPS URLs.

It may not correctly handle every possible URL format, especially URLs containing certain spaces, unusual characters, or punctuation.

For best results, use clean text files containing standard web URLs.

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Remove duplicate URLs
* [ ] Sort URLs alphabetically
* [ ] Export results to CSV
* [ ] Export results to JSON
* [ ] Detect email addresses
* [ ] Detect IP addresses
* [ ] Detect domains without `https://`
* [ ] Add URL validation
* [ ] Add URL categorization
* [ ] Add drag-and-drop file support
* [ ] Add graphical user interface
* [ ] Add command-line arguments
* [ ] Add recursive directory scanning

---

## 📜 License

This project is provided for educational and personal use.

---

## 👨‍💻 Author

**ApamBalik1337**

Built with 🐍 **Python**

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ **Star** on GitHub.

**Extract smarter. Search faster. 🔗**
