from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix(0,0)

#move = make_translate(1,2,3)
#print_matrix(move)

#scale = make_scale(1,2,3)
#print_matrix(scale)

#rotZ = make_rotZ(90)
#print_matrix(rotZ)

#rotX = make_rotX(90)
#print_matrix(rotX)

#rotY = make_rotY(90)
#print_matrix(rotY)


parse_file( 'script', edges, transform, screen, color )
