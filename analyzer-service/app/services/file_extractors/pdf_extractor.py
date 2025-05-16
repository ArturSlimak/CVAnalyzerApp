import fitz
from app.services.file_extractors.base_extractor import BaseExtractor
from app.utils.logging_config import setup_logger


class PDFExtractor(BaseExtractor):

    def extract_text(self, data: bytes) -> str:
        try:
            doc = fitz.open(stream=data, filetype="pdf")
            return "\n".join([page.get_text() for page in doc])
        except Exception as e:
            raise ValueError(f"Failed to extract PDF text: {e}")
