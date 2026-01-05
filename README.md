# MarkupRemover

Remove HTML and Markdown markup from files, outputting clean plain text.

## Features

- Removes HTML/XML tags
- Removes Markdown formatting:
  - Headers (`#`, `##`, `###`)
  - Bold and italic (`**`, `*`, `__`, `_`)
  - Links and images (`[text](url)`, `![alt](url)`)
  - Code blocks and inline code
  - Lists (bulleted and numbered)
- Cleans up extra whitespace

## Usage

```bash
python remove_markup.py input.md output.txt
```

## Example

Input (`example.md`):
```markdown
# Hello World

This is **bold** and *italic* text.

- List item 1
- List item 2
```

Output (`output.txt`):
```
Hello World

This is bold and italic text.

List item 1
List item 2
```

## Requirements

- Python 3.x
