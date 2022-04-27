# Simple PDF page extractor 

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## How to use

1. Activate virtual environment
2. Restore python dependencies by `pip install -r requirements.txt` in the shell
3. Three arguments are required to execute this program. 
    * -i input PDF file path
    * -o output PDF file path
    * -p page number in JSON array format e.g. `[1,3,5,7,9]`. Remember to escape square brackets if you are using zsh.
4. Execute `python pdf-splitter.py -i <input-file> -o <output-file> -p <page-number-array>`