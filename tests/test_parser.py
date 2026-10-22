
import fitz
import pytest

from src.resume_parser import extract_text_from_pdf


def create_sample_pdf():
    """Generate a small PDF for testing."""

    pdf = fitz.open()
    page = pdf.new_page()

    page.insert_text(
        (72, 72),
        "Python Developer\n"
        "Skills: Python, SQL, Machine Learning\n"
        "Education: B.E. Computer Engineering"
    )

    pdf_bytes = pdf.tobytes()
    pdf.close()

    return pdf_bytes


def test_extract_text_from_pdf_bytes():
    pdf_bytes = create_sample_pdf()

    text = extract_text_from_pdf(pdf_bytes)

    assert "Python Developer" in text
    assert "Machine Learning" in text
    assert "SQL" in text


def test_extract_text_from_pdf_path(tmp_path):
    pdf_path = tmp_path / "sample_resume.pdf"
    pdf_path.write_bytes(create_sample_pdf())

    text = extract_text_from_pdf(pdf_path)

    assert "Python Developer" in text


def test_invalid_pdf():
    with pytest.raises(ValueError, match="Could not read"):
        extract_text_from_pdf(b"this is not a PDF")


def test_pdf_without_readable_text():
    pdf = fitz.open()
    pdf.new_page()
    pdf_bytes = pdf.tobytes()
    pdf.close()

    with pytest.raises(ValueError, match="No readable text"):
        extract_text_from_pdf(pdf_bytes)
