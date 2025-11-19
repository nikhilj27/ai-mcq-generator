# AI MCQ Generator

A small utility that generates multiple-choice questions (MCQs) from researched notes using a HuggingFace LLM via LangChain.

**Overview:**
- The project runs a simple pipeline: it first collects research notes for a user-provided topic, then uses those notes to generate MCQs with four options and a correct answer flag.
- The LLM integration is implemented with the `langchain_huggingface` connector.

**Features:**
- `research_agent(topic)`: calls an LLM to produce research notes for the given topic.
- `mcq_generator_agent(research_data)`: calls an LLM to produce MCQs from research notes in a structured JSON-like format.
- `run_pipeline()`: interactive runner that prompts for a topic and prints generated MCQs.

**Requirements:**
- Python 3.8+
- See `requirements.txt` for exact packages (project expects `langchain_huggingface`, `python-dotenv`, and their dependencies).

**Environment variables (.env)**
- `LLM`: Hugging Face model repository id (e.g. `gpt-xyz` or other model id used by your HF endpoint).
- `HUGGINGFACEHUB_API_TOKEN`: Hugging Face API token with access to the model.

Example `.env`:

```
LLM=your-hf-model-id
HUGGINGFACEHUB_API_TOKEN=hf_xxx...yourtoken...
```

**Installation & Setup**

1. Create and activate a virtual environment:

```powershell
python -m venv venv
& "venv\Scripts\Activate.ps1"
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Add a `.env` file in the project root with the variables described above.

**Usage**

Run the pipeline interactively:

```powershell
python main.py
```

The program will prompt for a research topic, fetch research notes using the configured LLM, then generate and print MCQs.

**Output format**

The `mcq_generator_agent` expects to return MCQs in a structured JSON-like format. Example expected structure:

```json
{
	"1": {
		"mcq": "What is the capital of France?",
		"options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
		"correct_answer": "C"
	}
}
```

**Files of interest**
- `main.py` — entry point that calls `run_pipeline()`.
- `src/agents/research.py` — research agent implementation.
- `src/agents/mcqgenerator.py` — MCQ generator agent implementation.
- `src/workflows/pipeline.py` — pipeline orchestration and CLI prompt.

**Next steps / Improvements**
- Add argument flags to skip interactive prompts and use CLI args.
- Add unit tests and integration tests for agents (mock LLM responses).
- Add example outputs and sample `.env` template (without secrets).

If you want, I can also add a small example run or add a `.env.example` file.
