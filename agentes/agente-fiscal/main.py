import mimetypes
from pathlib import Path


class MIMETypeDetector:
    @staticmethod
    def detect(file_path: str) -> str:
        """
        Detecta o tipo MIME de um arquivo com base na extensão.
        """
        mime_type, _ = mimetypes.guess_type(file_path)
        return mime_type or "application/octet-stream"

    @staticmethod
    def register_custom_types(custom_types: dict) -> None:
        """
        Registra tipos MIME personalizados.
        Exemplo de uso:
            {
                '.md': 'text/markdown',
                '.log': 'text/plain'
            }
        """
        for ext, mime in custom_types.items():
            mimetypes.add_type(mime, ext, strict=True)

    @staticmethod
    def detect_from_path(path: Path) -> str:
        """
        Detecta o tipo MIME usando um objeto Path.
        """
        return MIMETypeDetector.detect(str(path))
