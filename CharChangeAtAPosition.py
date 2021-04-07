def mutate_string(string, position, character):
    s=string[:position]
    s=s+character
    s=s+string[position+1:]
    return s

if __name__ == '__main__':
