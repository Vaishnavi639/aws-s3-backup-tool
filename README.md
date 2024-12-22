# Python-Based Automation for Backups

This repository contains a Python-based automation project for efficiently managing backups. The project includes two scripts:

## Features

### `s3_backup.py`
- Automates the process of uploading local backups to an AWS S3 bucket.
- Ensures reliable and efficient storage of backups in the cloud.

### `backup.py`
- Creates a compressed `.tar.gz` backup of files from the source directory.
- Includes dynamic naming of backup files with the current date.

## Prerequisites

- Python 3.x
- AWS CLI configured with appropriate permissions for accessing S3.
- Required Python packages:
  - `boto3` (for AWS S3 operations)
  - `shutil` (for local file operations)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Vaishnavi639/python-backup-automation.git
   cd python-backup-automation
   ```
2. Install the required Python packages:
   ```bash
   pip install boto3
   ```

## Usage

### Running `backup.py`
This script creates a local backup of files.

1. Open `backup.py` and set the following variables:
   ```python
   source = "<source-directory>"  # Directory to back up
   destination = "<destination-directory>"  # Directory to save the backup file
   ```
2. Run the script:
   ```bash
   python backup.py
   ```
3. The script will create a compressed backup file in the destination directory with the naming format `backup_<YYYY-MM-DD>.tar.gz`.

### Running `s3_backup.py`
This script uploads local backups to an AWS S3 bucket.

1. Open `s3_backup.py` and configure the necessary variables:
   ```python
   bucket_name = "<your-s3-bucket-name>"
   local_file_path = "<path-to-local-backup-file>"
   ```
2. Run the script:
   ```bash
   python s3_backup.py
   ```
3. The script will upload the specified backup file to the configured S3 bucket.

## Example Workflow

1. Use `backup.py` to create a local backup of your files:
   ```bash
   python backup.py
   ```
2. Upload the generated backup file to AWS S3 using `s3_backup.py`:
   ```bash
   python s3_backup.py
   ```

## File Structure
```
python-backup-automation/
├── backup.py        # Script for creating local backups
├── s3_backup.py            # Script for uploading backups to AWS S3
└── README.md        # Documentation

---

Feel free to use this project and adapt it to your specific needs!
