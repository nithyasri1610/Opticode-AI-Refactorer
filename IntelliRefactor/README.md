# IntelliRefactor – Intelligent Static Analyzer for DSA Optimization

A lightweight static analyzer that identifies inefficient DSA usage in Python codebases and provides clear, rule-based refactoring suggestions.

## 🚀 Features
- Analyzes Python code using AST parsing
- Detects inefficient DSA patterns
- Provides refactor suggestions in structured JSON
- Modular architecture for easy extension

## 🛠 How It Works
1. Parses Python codebase using AST
2. Finds patterns like inefficient for-loops with range
3. Outputs suggestions to optimize time complexity

## 📦 Usage
```bash
python main.py
```

## 📂 Output
- `refactor_report.json`: Contains file name, line number, and DSA improvement suggestions

## 🧠 Future Work
- Java support
- Advanced pattern detection (recursion, graph traversal)
- GitHub PR comment bot
