import os
import ast

class DSAASTVisitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.issues = []

    def visit_For(self, node):
        if isinstance(node.iter, ast.Call) and getattr(node.iter.func, 'id', '') == 'range':
            with open(self.filename, "r") as f:
                source = f.read()
            code_snippet = ast.get_source_segment(source, node)
            self.issues.append({
                "file": self.filename,
                "line": node.lineno,
                "code": code_snippet,
                "reason": "Loop uses range, consider data structures like sets or dicts for optimization."
            })
        self.generic_visit(node)

def analyze_codebase(repo_path, language):
    issues = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py") and language == "python":
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r") as f:
                        content = f.read()
                        tree = ast.parse(content)
                        visitor = DSAASTVisitor(full_path)
                        visitor.visit(tree)
                        issues.extend(visitor.issues)
                except Exception as e:
                    print(f"Error analyzing {full_path}: {e}")
    return issues
