from app.services.file_extractors.pdf_extractor import PDFExtractor


def get_extractor(file_type: str):
    if file_type.lower() == "pdf":
        return PDFExtractor()
    else:
        raise ValueError("Unsupported file type")
