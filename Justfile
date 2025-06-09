# Install uv and cups using Homebrew
bootstrap:
    brew bundle install

# Install python dependencies
install:
    uv sync

# Print a file using the CUPS helper script
print: install
    uv run print_file.py
