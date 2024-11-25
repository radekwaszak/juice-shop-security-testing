# Zero Web App Security - Security Testing Project

This project performs security testing on the [**Zero Web App Security** website](http://zero.webappsecurity.com/index.html) using the **OWASP ZAP** (Zed Attack Proxy) tool. The goal of the project is to identify security vulnerabilities in the web application through automated scans, including spidering and active scanning.

## Project Setup

### 1. Install Required Tools

To run the security tests, you will need to install the following tools:

- **OWASP ZAP**: The main tool for security testing. You can download it from the [official OWASP ZAP website](https://www.zaproxy.org/download/).
- **Python 3**: The script is written in Python 3. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Required Python Packages**:
  
  - `zapv2`: The official OWASP ZAP Python client.
  - `python-dotenv`: To load the ZAP API key securely from a `.env` file.

To install the required Python packages, run:

  ```
  pip install -r requirements.txt
  ```

### 2. Securely Store API Key

To securely store your ZAP API key, follow these steps:

  1. Create a .env file in the root of your project directory and add your ZAP API key:

  ```
  ZAP_API_KEY=your_zap_api_key_here
  ```
 
  2. Ensure .env is added to `.gitignore` to keep the API key safe:

  ```
  .env
  ```

  3. The Python script will use the python-dotenv package to load the API key from the `.env` file.

### 3. Run the Script

  1. Configure the ZAP API key: The script will automatically read the API key from the `.env` file.

  2. Execute the script: Run the Python script `zap_script.py` to start the security testing:

  ```
  python zap_script.py
  ```

  This will:
  
    - Launch a spider scan on the Zero Web App Security site.
    - Perform an active scan to identify vulnerabilities.
    - Generate an HTML security report.

### 4. Report Generation

The security report will be generated in HTML format. After running the script, you can find the generated report in the reports folder as `security_report.html`.

Note: To view the report:
  - Download the raw file from GitHub and open it in a web browser.
  - Alternatively, you can host the report on GitHub Pages or open it in a local browser using the Live Server extension in VS Code.

### 5. Future Improvements
  - Automate the process: You could schedule this security testing process to run periodically.
  - Add more tests: Extend the testing suite to include additional security checks such as SQL injection, XSS, etc.
  - Integrate with CI/CD pipelines: Automate security testing within your continuous integration pipeline.

## Project Structure

```
.
├── zap_script.py       # Main script to run the ZAP scans
├── .env                # Stores ZAP API key securely
├── .gitignore          # Prevents .env and other sensitive files from being pushed
├── requirements.txt    # Python dependencies
└── reports/            # Directory to store generated security reports
    └── security_report.html
```

## License

This project is licensed under the MIT License - see the [LICENSE file](https://github.com/radekwaszak/zero-webapp-security-tests/blob/main/LICENSE) for details.

### **Explanation of the Sections:**

  - **Project Setup**: Instructions for installing required tools and libraries.
  - **Secure API Key Storage**: Instructions on how to securely store and load the ZAP API key.
  - **Running the Script**: Instructions for executing the script to run the security tests and generate the report.
  - **Report Generation**: Details on where to find the report and how to view it.
  - **Future Improvements**: Ideas for enhancing the project.
  - **Project Structure**: Directory structure for clarity.
  - **License**: Mention of the MIT license (you can update this if you're using a different license).

This README file should provide clear instructions for anyone using the repository and following along with the project. Let me know if you need more details or adjustments!

