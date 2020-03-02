from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    g = open(fname, "r")
    x = len(g.readlines())
    g.close()
    f = open(fname, "r")
    print x
    while x > 0:
        line = f.readline()
        if line == 'line\n':
            coords = f.readline()
            point = coords.split()
            add_edge(points, int(point[0]), int(point[1]), int(point[2]), int(point[3]), int(point[4]), int(point[5]))
        elif line == 'display\n':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif line == 'ident\n':
            ident(transform)
        elif line == 'scale\n':
            coords = f.readline()
            point = coords.split()
            matrix_mult(make_scale(int(point[0]),int(point[1]),int(point[2])), transform)
        elif line == 'apply\n':
            matrix_mult(transform,points)
        elif line == 'rotate\n':
            info = f.readline()
            infoz = info.split()
            matrix_mult(make_rot(infoz[0], int(infoz[1])), transform)
        elif line == 'move\n':
            info = f.readline()
            infoz = info.split()
            matrix_mult(make_translate(int(infoz[0]),int(infoz[1]),int(infoz[2])),transform)
        elif line == 'save\n':
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen, str(f.readline()))
        x = x - 1
    f.close()
    
            
            
            
            
    
