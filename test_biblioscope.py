#!/usr/bin/env python3
"""
Test script for BiblioScope functionality
"""

import subprocess
import sys
import os

def run_test(description: str, command: list) -> bool:
    """Run a test command and return success status"""
    print(f"\n🧪 Testing: {description}")
    print(f"Command: {' '.join(command)}")
    
    try:
        result = subprocess.run(command, cwd=os.path.dirname(__file__), 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ PASSED")
            # Show first few lines of output
            lines = result.stdout.split('\n')[:6]
            for line in lines:
                if line.strip():
                    print(f"   {line}")
            return True
        else:
            print("❌ FAILED")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    """Run all tests"""
    print("BiblioScope Test Suite")
    print("=" * 50)
    
    tests = [
        ("General search", ["python", "biblioscope.py", "machine learning", "--count", "2"]),
        ("Title search", ["python", "biblioscope.py", "deep learning", "--title", "--count", "2"]),
        ("DOI search", ["python", "biblioscope.py", "10.1007/s00256-024-04692-6", "--doi"]),
        ("Author search", ["python", "biblioscope.py", "Smith", "--author", "--count", "2"]),
        ("Help command", ["python", "biblioscope.py", "--help"])
    ]    
    passed = 0
    total = len(tests)
    
    for description, command in tests:
        if run_test(description, command):
            passed += 1
    
    print(f"\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
