# Zero Web App Security - Security Testing Project

This project performs security testing on the **Zero Web App Security** website using the **OWASP ZAP** (Zed Attack Proxy) tool. The goal of the project is to identify security vulnerabilities in the web application through automated scans, including spidering and active scanning.

## Project Setup

### 1. Install Required Tools

To run the security tests, you will need to install the following tools:

- **OWASP ZAP**: The main tool for security testing. You can download it from the [official OWASP ZAP website](https://www.zaproxy.org/download/).
- **Python 3**: The script is written in Python 3. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Required Python Packages**:
  - `zapv2`: The official OWASP ZAP Python client.
  - `python-dotenv`: To load the ZAP API key securely from a `.env` file.

  To install the required Python packages, run:

  ```bash
  pip install -r requirements.txt
