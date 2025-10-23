import logging
import time
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions
)
from docling.document_converter import DocumentConverter, PdfFormatOption

logger = logging.getLogger(__name__)

def main ():
    logging.basicConfig(level=logging.INFO)

    # Define input file as the knowledge source
    source = r"docs\sample_input.pdf"

    # Docling Parse with EasyOCR
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.ocr_options.lang = ["en"]

    document_converter = DocumentConverter(
        format_options= {
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    start_time = time.time()
    conversion_result = document_converter.convert(source)
    end_time = time.time() - start_time

    logger.info(f"Document conversion completed in {end_time:.2f} seconds.")

    # Export results
    output_directory = Path("output")
    output_directory.mkdir(exist_ok=True, parents=True)
    document_filename = conversion_result.input.file.stem

    # Export Docling into txt format
    with (output_directory / f"{document_filename}.txt").open("w", encoding="utf-8") as txt_file:
        txt_file.write(conversion_result.document.export_to_markdown())


if __name__ == "__main__":
    main()
