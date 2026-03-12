def clean_names(name_list):
    cleaned = []
    for name in name_list:
        cleaned.append(name.strip().lower())
    return cleaned    
