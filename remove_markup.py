import re
import sys
import argparse

def remove_markup(text):
    # Remove HTML/XML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove Markdown headers (e.g., #, ##, ###)
    text = re.sub(r'^#+ ', '', text, flags=re.MULTILINE)

    # Remove Markdown bold and italic (**, __, *, _)
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)

    # Remove Markdown links [text](url)
    text = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', text)

    # Remove Markdown images ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', r'\1', text)

    # Remove code blocks (``` or ~~~)
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'~~~[\s\S]*?~~~', '', text)

    # Remove inline code (`code`)
    text = re.sub(r'`([^`]+)`', r'\1', text)

    # Remove Markdown lists (-, *, +, 1.)
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)

    # Remove extra whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()

    return text

def main():
    parser = argparse.ArgumentParser(description="Remove markup from a file and output plain text.")
    parser.add_argument("input_file", help="Path to the input file containing markup")
    parser.add_argument("output_file", help="Path to the output file for plain text")

    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        plain_text = remove_markup(content)

        with open(args.output_file, 'w', encoding='utf-8') as file:
            file.write(plain_text)

        print(f"Markup removed. Plain text written to {args.output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
