import numpy as np
import time

def make_bg(phase):
	# Triangle size
	v_size = 46
	h_size = 80

	# Gradiente parameters
	max_grad = 10
	sd_op = 0.1

	# Wave parameters
	length = 16
	phase = phase +0 % length
	freq = 8
	amp = 0.5
	height = 0.3
	wave = amp*(np.sin(phase+np.arange(0,16)*np.pi/freq)+1)-height
	wave_op = wave*0.1
	wave_cl = length*wave*0.3

	color_map_default = np.array(['216171','367A99','41A3CD','67C2D6','FFFFFF'])
	#np.array(['0F128F','0F1F81','0F1281','0F1ADC','364ADC','3647F5','93C7F5','93CCF9','D0ECF9','D0E1FE','E0F1FE','E0FFFF','FFFFFF'])
	color_map = color_map_default#[np.array([0,2,1,4,3,6,5,8,7,10,9,12,11])]
	opacity_range = np.arange(1,0,-0.1)

	def format_line(p1,p2,p3,color,opacity):
		p1_str = "M"+str(int(p1[0]))+","+str(int(p1[1]))+" "
		p2_str = "L"+str(int(p2[0]))+","+str(int(p2[1]))+" "
		p3_str = "L"+str(int(p3[0]))+","+str(int(p3[1]))+" "

		return("<path d='"+p1_str+p2_str+p3_str+"Z"+"' style='fill:#"+color+";stroke-width:0;opacity:"+str(opacity)+"'/>")

	def line_type_one(v_plus,color,opacity):
		script = ""
		for i in np.arange(16):
			h_plus = h_size*i
			p1 = [h_plus,v_plus]
			p2 = [h_plus,v_plus+v_size]
			p3 = [h_plus+h_size/2,v_plus+v_size/2]
			op = np.clip(opacity-np.random.rand()*sd_op-wave_op[i],0,1)
			cl = color_map[np.clip(color+int(-1*np.random.rand()*2-wave_cl[i]),0,color_map.size-1)]
			script = script + format_line(p1,p2,p3,cl,op)
			p1 = [h_plus+h_size/2,v_plus+v_size/2]
			p2 = [h_plus+h_size,v_plus+v_size]
			p3 = [h_plus+h_size,v_plus]
			op = np.clip(opacity-np.random.rand()*sd_op-wave_op[i],0,1)
			cl = color_map[np.clip(color+int(-1*np.random.rand()*2-wave_cl[i]),0,color_map.size-1)]
			script = script + format_line(p1,p2,p3,cl,op)
		return(script)

	def line_type_two(v_plus,color,opacity):
		script = ""
		for i in np.arange(16):
			h_plus = h_size*i - h_size/2
			p1 = [h_plus+h_size/2,v_plus+v_size/2]
			p2 = [h_plus+h_size,v_plus+v_size]
			p3 = [h_plus+h_size,v_plus]
			op = np.clip(opacity-np.random.rand()*sd_op-wave_op[i],0,1)
			cl = color_map[np.clip(color+int(-1*np.random.rand()*2-wave_cl[i]),0,color_map.size-1)]
			script = script + format_line(p1,p2,p3,cl,op)
			h_plus = h_size*i + h_size/2
			p1 = [h_plus,v_plus]
			p2 = [h_plus,v_plus+v_size]
			p3 = [h_plus+h_size/2,v_plus+v_size/2]
			op = np.clip(opacity-np.random.rand()*sd_op-wave_op[i],0,1)
			cl = color_map[np.clip(color+int(-1*np.random.rand()*2-wave_cl[i]),0,color_map.size-1)]
			script = script + format_line(p1,p2,p3,cl,op)
		return(script)

	script = ""
	for i in np.arange(0,max_grad):
		pos_y = (i-1)*v_size
		script = script + line_type_two(pos_y - v_size/2,i,1)#(max_grad-i)/max_grad)
		script = script + line_type_one(pos_y,i,1)#(max_grad-i)/max_grad)

	header = "<!DOCTYPE html><html><body><svg width='1280' height='480'>"

	bottom = "</svg></body></html>"

	file = open("bg.html","w")
	file.write(header+script+bottom)
	file.close()

for i in np.arange(1):
	#time.sleep(1)
	make_bg(i)
	i = i+1
