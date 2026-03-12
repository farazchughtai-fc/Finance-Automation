import pandas as pd

def check_audit_compliance(file_path):
    """
    Sample script to flag transactions above a specific threshold 
    for manual review during USAID/WHO audit prep.
    """
    # Load financial data
    df = pd.read_excel(file_path)
    
    # Threshold for mandatory documentation
    threshold = 5000
    
    # Identify transactions needing review
    flagged = df[df['Amount'] > threshold]
    
    print(f"Total transactions flagged: {len(flagged)}")
    return flagged

# Note: In a real scenario, API keys or sensitive paths 
# would be managed via environment variables.
