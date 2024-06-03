# TxAdmin Attack Tool

## Overview
This tool is designed to simulate multiple users interacting with a TxAdmin panel by sending random commands at high frequency. It utilizes multithreading to generate concurrent requests to the TxAdmin API, allowing for stress testing or performance evaluation of the TxAdmin system.

## Requirements
- Python 3.x
- requests library (install via `pip install requests`)

## Usage
1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Run the script `fivem_dos.py`.
4. Enter the URL of your TxAdmin panel when prompted.
5. Enter the number of threads (simultaneous connections) you want to create.
6. The script will start sending random commands to the TxAdmin panel.

## Configuration
You can customize the list of commands sent to the TxAdmin panel by modifying the `commands` list in the `TxAdminClient` class within `txadmin_attack.py`.

## Caution
- This tool is intended for testing purposes only and should not be used against any system without proper authorization.
- Sending excessive requests may overload the target server and violate terms of service.

## Disclaimer
The developers of this tool are not responsible for any misuse or damage caused by its usage. By using this tool, you agree to take full responsibility for your actions.

## Contribution
Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
