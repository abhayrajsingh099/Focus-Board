

def has_ASCII(title="") -> bool:
    
    for char in title:
        if ord(char)>=0 and ord(char)<127 and char!=' ':
            return True

    return False