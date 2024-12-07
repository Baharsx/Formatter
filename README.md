
## How to Use 🚀

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/proxy-formatter.git
   cd proxy-formatter
   ```

2. **Prepare Your Input File**:
   - Create a file named `input_proxies.txt` in the same directory.
   - Add your proxies, one per line, for example:
     ```
     proxy1
     proxy2
     proxy3
     ```

3. **Run the Script**:
   ```bash
   python script.py
   ```

4. **Output**:
   - The formatted proxies will be saved to `formatted_proxies.txt`.
   - A custom ASCII art logo will appear in the terminal after processing.

---

## Example Output 📂

### Input File (`input_proxies.txt`):
```plaintext
proxy1
proxy2
proxy3
```

### Output File (`formatted_proxies.txt`):
```plaintext
"proxy1",
"proxy2",
"proxy3",
```

### Terminal Display:
```plaintext
Saving completed! Loading a fancy logo for you...

Generating Logo: ██████████████████████████████████████████████ 100%

███████╗ ██████╗ ██╗  ██╗███████╗██╗██╗      ██████╗ ██╗     
██╔════╝██╔═══██╗██║ ██╔╝██╔════╝██║██║     ██╔═══██╗██║     
███████╗██║   ██║█████╔╝ █████╗  ██║██║     ██║   ██║██║     
╚════██║██║   ██║██╔═██╗ ██╔══╝  ██║██║     ██║   ██║██║     
███████║╚██████╔╝██║  ██╗███████╗██║███████╗╚██████╔╝███████╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝ ╚═════╝ ╚══════╝

🎉 Done! Enjoy your formatted proxies! 🎉
```

---

## Customization 🛠️

### 1. Change Input/Output File Names
Edit the `input_file` and `output_file` variables in the script to use different file names:
```python
input_file = "your_input_file.txt"
output_file = "your_output_file.txt"
```

### 2. Add Your Own ASCII Art
To replace the ASCII logo, use an online tool like [TAAG](https://patorjk.com/software/taag/) to generate a new design and update the script's `print` statement.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions 🤝

Feel free to open issues or submit pull requests to improve this project. All contributions are welcome!

---

## Author 🙋‍♂️

Created with ❤️ by **SOHEIL DL**.
```

---

### Notes:
- Replace `yourusername` in the clone instructions with your GitHub username.
- Add a `LICENSE` file to your repository if you're using an open-source license.
- This `README.md` will render perfectly on GitHub without breaking the formatting. If needed, preview it locally using a Markdown editor like VSCode or GitHub's built-in preview.
