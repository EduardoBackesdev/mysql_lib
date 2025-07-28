def select(table: str, columns: list[str]):
    
    c = ""
    
    for i in range(len(columns)):
        if i == len(columns) - 1:
            c += columns[i]
        else:        
            c += columns[i] + ', '
        
    query = f"SELECT {c} FROM {table};"
        
    
    