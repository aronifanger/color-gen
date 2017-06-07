from random import randint as rnd
from numpy.linalg import inv
from numpy.linalg import norm
import numpy as np

def color_dec(color):
	v = [color[1:3],color[3:5],color[5:7]]
	return(np.array([int(v[0],16),int(v[1],16),int(v[2],16)]))

def dec_color(v):
	return("#%02X%02X%02X"%(v[0],v[1],v[2]))


#	    |a  b  c | -> v1
#	M = |d* e  f | -> v2
#	    |g  h* i*| -> v3

# We need to find d*, h*, i* where <v1,v2>=0 (1), 
# <v3,v2>=0 (2) and <v1,v3>=0 (3)
# From (1): d = (be+cf)/a
# From (2) and (3): ...

def gen_color(color):
  dist = 20
  v = color_dec(color)
	# a != 0
  a = v[0]
  b = v[1]
  c = v[2]

	# Test values to e, f and g
  e = rnd(0,255)
  f = rnd(0,255)
  g = rnd(0,255)
  while(e*c == f*b):
    e = rnd(0,255)
    f = rnd(0,255)

	# From (1)
  d = (b*e+c*f)/a

  submatrix = np.array([[e,f],[b,c]])
  inv_submatrix = inv(submatrix)
  eq = np.array([-(b*e+c*f)*g/a, a*g])

  resp = inv_submatrix.dot(eq)
  h = resp[0]
  i = resp[1]
	
  v1 = np.array([a,b,c])
  v2 = np.array([d,e,f])
  v3 = np.array([g,h,i])
	
  v2_norm = dist*v2/norm(v2)
  v3_norm = dist*v3/norm(v3)
  
  c3 = dec_color(v1)
  c1 = dec_color(np.clip(v1+v2_norm,0,255))
  c2 = dec_color(np.clip(v1-v2_norm,0,255))
  c4 = dec_color(np.clip(v1+v3_norm,0,255))
  c5 = dec_color(np.clip(v1-v3_norm,0,255))
  
  return(np.array([c1,c2,c3,c4,c5]))


def gen_color_map(v):
  inc = 1
  maxi = max(v)
  mini = min(v)
  vnorm = (v-mini)/(maxi-mini)
  index = vnorm.argsort()

  if(vnorm[index[1]] + inc > 1 ):
    vnorm_output2 = np.array([vnorm[index[0]], 1, vnorm[index[2]] - ((vnorm[index[1]] + inc) % 1)])
  else:
    vnorm_output2 = np.array([vnorm[index[0]], vnorm[index[1]] + inc, vnorm[index[2]]])
    
  if(vnorm[index[1]] - inc < 0 ):
    vnorm_output3 = np.array([vnorm[index[0]] + inc - vnorm[index[1]], vnorm[index[1]], vnorm[index[2]]])
  else:
    vnorm_output3 = np.array([vnorm[index[0]], vnorm[index[1]] - inc, vnorm[index[2]]])
    
  v_output2 = vnorm_output2*(maxi-mini)+mini
  v_output3 = vnorm_output3*(maxi-mini)+mini
  
  c2 = dec_color(v)
  c1 = dec_color(v_output2[index])
  c3 = dec_color(v_output3[index])
  
  return(np.array([c1,c2,c3]))
    

def gen_color_gradient(color):
  v = color_dec(color)
  white = np.array([255,255,255])
  l = 5
  colors = [gen_color_map((v*i/l)+(white*(l-i)/l)) for i in np.arange(l+1)]
  return(np.array(colors))
    
def format_html(colors):
  print "<html>"
  for i in colors:
    for j in i:
      print "<div style='float:left; width:500px; height:60px;background-color:"+j+"'>&nbsp;</div>"
  print "</html>"
  
color = "#00680f"
format_html(gen_color_gradient(color))