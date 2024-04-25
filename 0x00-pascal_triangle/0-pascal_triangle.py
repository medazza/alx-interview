def pascal_triangle(n):
    """ Pascal triangle"""
    if n <= 0:
        return []
    
    triangle = []
    for row in range(n):
        # Create a new row
        current_row = []
        
        for col in range(row + 1):
            # Calculate the value for each element in the row
            if col == 0 or col == row:
                current_row.append(1)  # The first and last elements in each row are always 1
            else:
                # The value of an element is the sum of the two elements above it
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(value)
        
        triangle.append(current_row)
    
    return triangle