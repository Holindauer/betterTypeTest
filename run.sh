#!/bin/bash

# Function to check if pyspellchecker is installed
check_spellchecker_installed() {
    pip show pyspellchecker > /dev/null 2>&1
}

# Function to install pyspellchecker
install_spellchecker() {
    echo "Installing pyspellchecker..."
    pip install pyspellchecker
}

# Main program execution
main() {
    # Check if pyspellchecker is installed
    check_spellchecker_installed

    # If pyspellchecker is not installed, install it
    if [[ $? -ne 0 ]]; then
        install_spellchecker
    fi

    # Run the Python program
    echo "Running BetterTypeTest..."
    python3 betterTypeTest.py
}

main