# Add hyperlinks to chapter notes

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`
  `source venv/bin/activate`

- Install necessary Python modules via `pip3 install -r requirements.txt`

- Save necessary Python modules via `pip3 freeze > requirements.txt`

## Environment variables
- FOLDER_TO=full path to the folder holding the source chapter and section notes
- FOLDER_FROM=full path to the folder to hold the altered source chapter and section notes

## Usage

`python3 format_chapter_notes.py`
