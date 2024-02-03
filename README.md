# Golestan-Crawler

## Project Overview

This project is a fully automated crawler for the Golestan website (https://golestan.iust.ac.ir/).
It uses Selenium for automation, including bypassing the Captcha using a GitHub Repository (https://github.com/AmirH-Moosavi/CaptchaCrack).
The crawler can access the **102** report on Golestan and is configured to retrieve undergraduate 
course information without requiring a username, password, or human configuration.
The only requirement is to set the semesters you want to retrieve.

## Installation Guide

#### Pre-requisites
- Python 3.6 or higher
- A browser (Preferably Chrome)

#### Installation
1. Clone the repository to your local machine.
   ```bash
    git clone https://github.com/KamyarMoradian/Golestan-Crawler.git
    ```
2. Navigate to the project directory.
   ```bash
    cd Golestan-Crawler
    ```
3. Install the required packages.
   ```bash
   pip install -r requirements.txt
    ```

## Usage
1. Set the driver version in the `config.py` file.
   ```python
   DRIVER_VERSION = "YOUR_CHROME_DRIVER_VERSION"
    ```
2. Set the semesters you want to retrieve in the `main.py` file.


3. Uncomment commented lines in `main.py` based on the guide given above each one of them.


4. Run the `main.py` file.
   ```bash
   python main.py
    ```
5. The retrieved data will be saved in the `data` directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
