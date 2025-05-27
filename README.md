# BiblioScope 📚

A clean, user-friendly command-line tool for searching academic papers via Elsevier APIs.

## Features

- 🔍 **Scopus Search**: Search millions of academic papers, abstracts, and citations
- 🚀 **Fast & Clean**: Simple command-line interface with beautiful output
- 🔑 **Environment Variables**: Secure API key management
- 📊 **Detailed Results**: Shows titles, authors, journals, years, and DOIs

## Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key**:
   ```bash
   cp .env.example .env
   # Edit .env and add your Elsevier API key
   ```

## Getting Your API Key

1. Visit [Elsevier Developer Portal](https://dev.elsevier.com/)
2. Create an account and request an API key
3. Add the key to your `.env` file:
   ```
   ELSEVIER_API_KEY=your_actual_api_key_here
   ```

## Usage

### Basic Search
```bash
python biblioscope.py "machine learning"
```

### Specify Number of Results
```bash
python biblioscope.py "artificial intelligence" --count 20
```

### Make it Executable (Optional)
```bash
chmod +x biblioscope.py
./biblioscope.py "deep learning"
```
## Command Line Options

- `query`: Your search query (required)
- `--count, -c`: Number of results to return (default: 10, max: 200)

## Example Output

```
🔍 Searching for: machine learning
📊 Requesting 10 results...

📚 Found 230882 total results

[1] Machine Learning-Based Surface Roughness Prediction
    Author: Ginting A.
    Journal: Journal of Applied Science and Engineering (2024)
    DOI: 10.6180/jase.202501_28(1).0001

[2] Research on Efficiency Coupling Coordination Feature Model
    Author: Cui X.
    Journal: Tehnicki Vjesnik (2024)
    DOI: 10.17559/TV-20240215001122
```

## Supported Databases

Currently supports:
- ✅ **Scopus**: Comprehensive academic database with 25,000+ journals
- 🚧 **ScienceDirect**: Coming soon (requires different subscription level)

## Requirements

- Python 3.7+
- Valid Elsevier API key
- Internet connection

## Contributing

Contributions welcome! Please feel free to submit issues and pull requests.

## License

MIT License - see LICENSE file for details.
