# URL Path Checker App

This is a simple URL path Brute checker app built applied to an vulnerable flask app. It includes scripts for both multi-threaded and mono-threaded directory traversal checks.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/JonatanaRandria/directory_check
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

### Launching the Flask App

1. Navigate to the directory containing the Flask app:

    ```
    cd directory_check
    ```

2. Run the Flask app using the `flask` command:

    ```
    flask --app .\pathtrav.py run
    ```

3. The app will be accessible at http://127.0.0.1:5000.

### Running the Path Checking Scripts

#### Multi-threaded Script

1.  Run the multi-threaded script:

    ```
    python brute_multithread.py
    ```

#### Mono-threaded Script

1. Run the mono-threaded script:

    ```
    python brute_monothread.py
    ```
## About Me

- **Name:** RANDRIAMPARANY Jonatana Andrianina
- **Email:** hei.jonatana@gmail.com
- **Référence STD:** STD21090
