
import re
from pathlib import Path

import fitz  # PyMuPDF


def clean_text(text: str) -> str:
    """Normalize whitespace in extracted PDF text."""

    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def extract_text_from_pdf(source: bytes | str | Path) -> str:
    """
    Extract readable text from a PDF.

    Args:
        source: PDF file path or PDF contents as bytes.

    Returns:
        Cleaned text extracted from all pages.

    Raises:
        ValueError: If the PDF is invalid, encrypted,
                    or contains no extractable text.
        FileNotFoundError: If a supplied path doesn't exist.
    """

    try:
        if isinstance(source, bytes):
            document = fitz.open(stream=source, filetype="pdf")
        else:
            document = fitz.open(str(source))

        with document as pdf:
            if pdf.needs_pass:
                raise ValueError(
                    "This PDF is password-protected. "
                    "Please provide an unlocked PDF."
                )

            page_texts = []

            for page in pdf:
                page_texts.append(page.get_text("text"))

            extracted_text = clean_text("\n".join(page_texts))

    except ValueError:
        raise
    except (fitz.FileDataError, RuntimeError, OSError) as exc:
        raise ValueError(
            "Could not read this PDF. Please upload a valid PDF file."
        ) from exc

    if not extracted_text:
        raise ValueError(
            "No readable text was found. This may be a scanned PDF. "
            "OCR support can be added in a later step."
        )

    return extracted_text
