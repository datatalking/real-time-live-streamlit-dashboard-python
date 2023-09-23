import sys
import streamlit.web.cli as cli


if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(cli.main())
