import os
import json
from analyzer.analyze_code import analyze_codebase
from refactor.refactor_engine import refactor_code

REPO_PATH = "sample_project/"  # Local path to code repo
LANGUAGE = "python"  # Can be "java" or "python"

def main():
    print("[+] Starting IntelliRefactor Analyzer...")
    issues = analyze_codebase(REPO_PATH, LANGUAGE)
    print(f"[+] Found {len(issues)} DSA inefficiencies.")
    suggestions = []
    for issue in issues:
        suggestion = refactor_code(issue)
        suggestions.append(suggestion)
    with open("refactor_report.json", "w") as f:
        json.dump(suggestions, f, indent=4)
    print("[+] Refactor report saved to refactor_report.json")

if __name__ == "__main__":
    main()
