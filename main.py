def EditDistance(x, y):
    m = len(x)
    n = len(y)
    
    # Create a table to store the edit distances
    arr = [[0] * (n + 1) for i in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        arr[i][0] = i
    for j in range(n + 1):
        arr[0][j] = j
    
    # Compute the edit distance and operations
    for i in range(1, m + 1):
        for j in range(1, n + 1): 
            # If characters match
            if x[i - 1] == y[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else: # Choose the minimum cost operation
                substitute = arr[i - 1][j - 1] + 1
                delete = arr[i - 1][j] + 1
                insert = arr[i][j - 1] + 1
                arr[i][j] = min(substitute, delete, insert)
    
    # Trace back the operations
    operations = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]: # Characters match
            i -= 1
            j -= 1
        else:
            current_cost = arr[i][j]
            substitute = arr[i - 1][j - 1]
            delete = arr[i - 1][j]
            insert = arr[i][j - 1]
            
            if current_cost == substitute + 1:
                operations.insert(0, f"Substitute \"{x[i - 1]}\" into \"{y[j - 1]}\"")
                i -= 1
                j -= 1
            elif current_cost == delete + 1:
                operations.insert(0, f"Delete \"{x[i - 1]}\"")
                i -= 1
            elif current_cost == insert + 1:
                operations.insert(0, f"Insert \"{y[j - 1]}\"")
                j -= 1
    
    # Handle remaining characters if any
    while i > 0:
        operations.insert(0, f"Delete \"{x[i - 1]}\"")
        i -= 1
    while j > 0:
        operations.insert(0, f"Insert \"{y[j - 1]}\"")
        j -= 1
    
    for operation in operations:
        print(operation)
    
    return arr[m][n]

 

def main():
    x = input("Enter first word: ")
    y = input("Enter second word: ")
    distance = EditDistance(x, y)
    print("Edit Distance:", distance)
    
if __name__ == "__main__":
    main()