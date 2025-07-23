def refactor_code(issue):
    code = issue["code"].strip()
    suggestion = "Review loop structure — consider using set/dictionary to reduce time complexity."
    if "for" in code and "range" in code:
        suggestion = "This loop uses 'range'. If nested or scanning lists, consider a dictionary or set lookup to optimize."
    return {
        "file": issue["file"],
        "line": issue["line"],
        "original_code": code,
        "suggestion": suggestion
    }
