# Intellumia Knowledge Graph

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)

A powerful **Knowledge Graph Question-Answering Prototype** that transforms unstructured documents into intelligent, queryable knowledge graphs using cutting-edge RAG (Retrieval-Augmented Generation) technology.

## Features

- **Smart Document Processing**: Convert PDFs to structured text with OCR and table recognition
- **Knowledge Graph Construction**: Automatically extract entities and relationships
- **Multiple Search Methods**: Local, Global, Drift, and Basic search strategies
- **Vector Embeddings**: Semantic search using LanceDB and OpenAI embeddings
- **Natural Language Q&A**: Ask questions in plain English, get intelligent answers
- **Community Detection**: Identify and analyze entity communities
- **High-Performance**: Optimized caching and concurrent processing

## Architecture

```
Document (PDF)
      ↓
[Docling + OCR] → Structured Text
      ↓
[GraphRAG] → Knowledge Graph
      ↓
[Entity & Relationship Extraction]
      ↓
[LanceDB Vector Store]
      ↓
[Query Engine] → Answers
```

## Project Structure

```
intellumia-knowledgegraph/
├── converter.py                    # PDF → Text conversion pipeline
├── query.ipynb                     # Interactive query interface
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
│
├── rag-system/                     # Core RAG system
│   ├── settings.yaml               # Configuration file
│   ├── input/                      # Input documents
│   ├── output/                     # Generated outputs
│   │   ├── context.json            # Extracted context
│   │   ├── graph.graphml           # Knowledge graph
│   │   ├── stats.json              # Processing statistics
│   │   └── lancedb/                # Vector embeddings database
│   ├── cache/                      # Processing cache
│   ├── logs/                       # System logs & reports
│   └── prompts/                    # LLM prompt templates
│       ├── extract_graph.txt
│       ├── extract_claims.txt
│       ├── local_search_system_prompt.txt
│       ├── global_search_map_system_prompt.txt
│       ├── community_report_graph.txt
│       └── [+ more prompts]
│
├── docs/                           # Documentation
└── output/                         # Processing output
```

## Quick Start

### Prerequisites

- **Python**: 3.10 or higher
- **OpenAI API Key**: For GPT-4o-mini and embeddings
- **pip**: Python package manager

### Installation

1. **Clone the repository**
   ```powershell
   git clone https://github.com/theodoreamadeo/intellumia-knowledgegraph.git
   cd intellumia-knowledgegraph
   ```

2. **Create a virtual environment** (recommended)
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure environment**
   - Create `rag-system/.env` file
   - Add your OpenAI API key:
     ```
     GRAPHRAG_API_KEY=sk-your-api-key-here
     ```

### Basic Usage

#### 1. Convert PDF to Text
```powershell
python converter.py
```

**What it does:**
- Reads PDF from `docs/sample_input.pdf`
- Applies OCR for scanned documents
- Extracts table structures
- Exports to `output/sample_input.txt`

#### 2. Process with RAG System
Navigate to `rag-system/` directory and run GraphRAG:
```powershell
cd rag-system
python -m graphrag.index --config settings.yaml
```

**Outputs:**
- `output/graph.graphml` - Knowledge graph structure
- `output/context.json` - Extracted entities and relationships
- `output/lancedb/` - Vector embeddings

#### 3. Query the Knowledge Graph
Use the interactive Jupyter notebook:
```powershell
jupyter notebook query.ipynb
```

Or programmatically:
```python
from graphrag.query_context import QueryContext

qc = QueryContext(config_path="rag-system/settings.yaml")

# Local search (context-aware)
response = qc.query("What are the main topics?", method="local")

# Global search (comprehensive)
response = qc.query("Summarize everything", method="global")
```

## Configuration

### Key Settings (`rag-system/settings.yaml`)

#### LLM Models
```yaml
models:
  default_chat_model:
    model: gpt-4o-mini              # Chat model
    concurrent_requests: 25
    max_retries: 10
  default_embedding_model:
    model: text-embedding-3-small   # Embedding model
```

#### Processing Parameters
```yaml
chunks:
  size: 1200              # Chunk size in tokens
  overlap: 100            # Overlap between chunks

extract_graph:
  entity_types: [organization, person, geo, event]
  max_gleanings: 1

summarize_descriptions:
  max_length: 500         # Max description length
```

#### Search Methods
```yaml
local_search:           # Context-aware search
  prompt: "prompts/local_search_system_prompt.txt"

global_search:          # Comprehensive search (map-reduce)
  prompt: "prompts/global_search_map_system_prompt.txt"

drift_search:           # Semantic drift detection
  prompt: "prompts/drift_search_system_prompt.txt"

basic_search:           # Simple semantic search
  prompt: "prompts/basic_search_system_prompt.txt"
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `graphrag` | Microsoft GraphRAG framework for knowledge graph construction |
| `docling` | Advanced document parsing with OCR and table recognition |
| `lancedb` | Vector database for efficient embeddings |
| `openai` | LLM API access (GPT-4o-mini) |
| `pyyaml` | YAML configuration parsing |
| `networkx` | Graph analysis utilities |

See `requirements.txt` for complete list.

## Workflow Example

```
1. Input
   └─ Place PDF in docs/ folder

2. Convert
   └─ python converter.py
      └─ Output: output/sample_input.txt

3. Build Graph
   └─ python -m graphrag.index --config settings.yaml
      ├─ Extract entities & relationships
      ├─ Detect communities
      ├─ Generate embeddings
      └─ Output: output/graph.graphml, output/lancedb/

4. Query
   └─ Use query.ipynb or API
      └─ Input: Natural language question
      └─ Output: Answer with source citations
```

## Output Artifacts

After processing, you'll find:

- **`context.json`** - Extracted entities, relationships, and communities
- **`graph.graphml`** - Knowledge graph in GraphML format (viewable in Gephi)
- **`stats.json`** - Processing statistics and metrics
- **`lancedb/`** - Vector embeddings for semantic search

## Search Methods Explained

### Local Search
- **Best for**: Specific questions about entities
- **How it works**: Finds related entities and their context
- **Speed**: Fast

### Global Search
- **Best for**: Summary and overview questions
- **How it works**: Map-reduce approach over all data
- **Speed**: Slower but comprehensive

### Drift Search
- **Best for**: Exploring related topics
- **How it works**: Detects semantic drift patterns
- **Speed**: Medium

### Basic Search
- **Best for**: Simple keyword searches
- **How it works**: Direct semantic similarity
- **Speed**: Very fast

## Development

### Project Setup

1. Install development dependencies
2. Configure `.env` with your API keys
3. Test with sample input: `docs/sample_input.pdf`

### Modifying Prompts

Edit templates in `rag-system/prompts/`:
- `extract_graph.txt` - Entity/relationship extraction
- `local_search_system_prompt.txt` - Local search behavior
- `global_search_*.txt` - Global search behavior

### Debugging

Check logs in `rag-system/logs/` for detailed processing information.

## Requirements

- Python 3.10+
- 4GB+ RAM (8GB+ recommended)
- OpenAI API account with credits
- Internet connection

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues or questions:
1. Check existing GitHub issues
2. Review the documentation in `docs/`
3. Open a new issue with detailed information

## Resources

- [GraphRAG Documentation](https://microsoft.github.io/graphrag/)
- [Docling Documentation](https://ds4sd.github.io/docling/)
- [LanceDB Documentation](https://docs.lancedb.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

**Project Status**: Active Development  
**Last Updated**: October 2025  
**Repository**: [theodoreamadeo/intellumia-knowledgegraph](https://github.com/theodoreamadeo/intellumia-knowledgegraph)

---

<div align="center">

Made with love by [Theodore Amadeo](https://github.com/theodoreamadeo)

</div>
