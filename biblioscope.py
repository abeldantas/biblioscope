#!/usr/bin/env python3
"""
BiblioScope - Elsevier API Research Tool
A clean, user-friendly interface for searching academic papers via Elsevier APIs
"""

import os
import sys
import requests
import json
import argparse
from typing import Dict, List, Optional
from dotenv import load_dotenv

class BiblioScope:
    """Main class for interacting with Elsevier APIs"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_urls = {
            'scopus': 'https://api.elsevier.com/content/search/scopus',
            'sciencedirect': 'https://api.elsevier.com/content/search/sciencedirect',
            'author': 'https://api.elsevier.com/content/search/author'
        }
        self.headers = {
            'X-ELS-APIKey': api_key,
            'Accept': 'application/json'
        }
    
    def search_scopus(self, query: str, count: int = 10, search_type: str = "general") -> Dict:
        """Search Scopus database with different search types"""
        # Format query based on search type
        if search_type == "doi":
            # Clean DOI format
            query = query.replace('https://doi.org/', '').replace('http://dx.doi.org/', '')
            query = query.replace('doi:', '').strip()
            query = f'DOI({query})'
        elif search_type == "title":
            query = f'TITLE({query})'
        elif search_type == "author":
            query = f'AUTHOR-NAME({query})'
        # general search uses query as-is
        
        params = {
            'query': query,
            'count': min(count, 200)
        }
        
        try:
            response = requests.get(
                self.base_urls['scopus'], 
                headers=self.headers, 
                params=params, 
                timeout=30
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error searching Scopus: {e}")
            return {}    
    def format_scopus_results(self, data: Dict) -> None:
        """Format and display Scopus search results"""
        if not data or 'search-results' not in data:
            print("No results found or invalid response")
            return
            
        results = data['search-results']
        total_results = results.get('opensearch:totalResults', '0')
        
        print(f"\n📚 Found {total_results} total results\n")
        
        if 'entry' not in results or not results['entry']:
            print("No articles to display")
            return
            
        for i, entry in enumerate(results['entry'], 1):
            title = entry.get('dc:title', 'No title available')
            author = entry.get('dc:creator', 'No author available')
            journal = entry.get('prism:publicationName', 'No journal available')
            year = entry.get('prism:coverDate', 'No date')[:4] if entry.get('prism:coverDate') else 'Unknown'
            doi = entry.get('prism:doi', 'No DOI')
            
            print(f"[{i}] {title}")
            print(f"    Author: {author}")
            print(f"    Journal: {journal} ({year})")
            print(f"    DOI: {doi}")
            print()

def load_api_key() -> str:
    """Load API key from environment variables"""
    load_dotenv()
    
    api_key = os.getenv('ELSEVIER_API_KEY')
    if not api_key:
        print("❌ Error: ELSEVIER_API_KEY not found in environment variables")
        print("Please set it in your .env file or environment")
        sys.exit(1)
    
    return api_key

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description='BiblioScope - Search academic papers via Elsevier APIs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  biblioscope.py "machine learning"
  biblioscope.py "artificial intelligence" --count 20
        """
    )
    
    parser.add_argument('query', help='Search query')
    parser.add_argument('--count', '-c', type=int, default=10, 
                       help='Number of results to return (default: 10, max: 200)')
    
    args = parser.parse_args()    
    def format_scopus_results(self, data: Dict) -> None:
        """Format and display Scopus search results"""
        if not data or 'search-results' not in data:
            print("No results found or invalid response")
            return
            
        results = data['search-results']
        total_results = results.get('opensearch:totalResults', '0')
        
        print(f"\n📚 Found {total_results} total results\n")
        
        if 'entry' not in results or not results['entry']:
            print("No articles to display")
            return
            
        for i, entry in enumerate(results['entry'], 1):
            title = entry.get('dc:title', 'No title available')
            author = entry.get('dc:creator', 'No author available')
            journal = entry.get('prism:publicationName', 'No journal available')
            year = entry.get('prism:coverDate', 'No date')[:4] if entry.get('prism:coverDate') else 'Unknown'
            doi = entry.get('prism:doi', 'No DOI')
            
            print(f"[{i}] {title}")
            print(f"    Author: {author}")
            print(f"    Journal: {journal} ({year})")
            print(f"    DOI: {doi}")
            print()

def load_api_key() -> str:
    """Load API key from environment variables"""
    load_dotenv()
    
    api_key = os.getenv('ELSEVIER_API_KEY')
    if not api_key:
        print("❌ Error: ELSEVIER_API_KEY not found in environment variables")
        print("Please set it in your .env file or environment")
        sys.exit(1)
    
    return api_key
def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description='BiblioScope - Search academic papers via Elsevier APIs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  biblioscope.py "machine learning"
  biblioscope.py "artificial intelligence" --count 20
  biblioscope.py "10.1016/j.example.2023.123456" --doi
  biblioscope.py "deep learning applications" --title
  biblioscope.py "Smith, J." --author
        """
    )
    
    parser.add_argument('query', help='Search query')
    parser.add_argument('--count', '-c', type=int, default=10, 
                       help='Number of results to return (default: 10, max: 200)')
    parser.add_argument('--doi', action='store_true',
                       help='Search by DOI')
    parser.add_argument('--title', action='store_true',
                       help='Search in titles only')
    parser.add_argument('--author', action='store_true',
                       help='Search by author name')
    
    args = parser.parse_args()
    
    # Determine search type
    search_type = "general"
    if args.doi:
        search_type = "doi"
    elif args.title:
        search_type = "title"
    elif args.author:
        search_type = "author"
    
    # Load API key
    api_key = load_api_key()
    
    # Initialize BiblioScope
    biblio = BiblioScope(api_key)
    
    print(f"🔍 Searching for: {args.query}")
    print(f"📊 Search type: {search_type}")
    print(f"📊 Requesting {args.count} results...")
    
    # Search Scopus
    results = biblio.search_scopus(args.query, args.count, search_type)
    biblio.format_scopus_results(results)

if __name__ == "__main__":
    main()
