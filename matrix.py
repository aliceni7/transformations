"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    matrix = new_matrix(4,4)
    ident(matrix)
    for end in range( len(matrix[0]) - 1):
        matrix[3][end] = x
        x = y
        y = z
    return matrix

def make_scale( x, y, z ):
    matrix = new_matrix(4,4)
    ident(matrix)
    for row in range( len(matrix[0]) - 1 ):
        for col in range( len(matrix) ):
            if row == col:
                matrix[col][row] = x
                x = y
                y = z
    return matrix
            
def make_rot( axis, theta ):
    theta = theta * math.pi / 180.0
    matrix = new_matrix(4,4)
    ident(matrix)
    if axis == 'x':
        for row in range(3):
            for col in range(3):
                if col == 1 and row == 1:
                    matrix[col][row] = math.cos(theta)
                if col == 2 and row == 1:
                    matrix[col][row] = -1 * math.sin(theta)
                    matrix[row][col] = math.sin(theta)
                if col == 2 and row == 2:
                    matrix[col][row] = math.cos(theta)
    if axis == 'y':
        for row in range(3):
            for col in range(3):
                if col == 0 and row == 0:
                    matrix[col][row] = math.cos(theta)
                if col == 2 and row == 0:
                    matrix[col][row] = math.sin(theta)
                    matrix[row][col] = math.sin(theta)
                if col == 2 and row == 2:
                    matrix[col][row] = math.cos(theta)
    if axis == 'z':
        for row in range(2):
            for col in range(2):
                if row == col:
                    matrix[col][row] = math.cos(theta)
                if col == 1 and row == 0:
                    matrix[col][row] = -1 * math.sin(theta)
                    matrix[row][col] = math.sin(theta)
    return matrix

def make_rotY( theta ):
    theta = math.radians(theta)
    matrix = new_matrix(4,4)
    ident(matrix)
    for row in range(3):
        for col in range(3):
            if col == 0 and row == 0:
                matrix[col][row] = math.cos(theta)
            if col == 2 and row == 0:
                matrix[col][row] = math.sin(theta)
                matrix[row][col] = math.sin(theta)
            if col == 2 and row == 2:
                matrix[col][row] = math.cos(theta)
    return matrix

def make_rotZ( theta ):
    theta = math.radians(theta)
    matrix = new_matrix(4,4)
    ident(matrix)
    for row in range(2):
        for col in range(2):
            if row == col:
                matrix[col][row] = math.cos(theta)
            if col == 1 and row == 0:
                matrix[col][row] = -1 * math.sin(theta)
                matrix[row][col] = math.sin(theta)
    return matrix


#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
