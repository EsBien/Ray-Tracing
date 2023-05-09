from sightpy import *

# define materials to use
#gold_metal = Glossy(diff_color = rgb(1., .572, .184), n = vec3(0.15+3.58j, 0.4+2.37j, 1.54+1.91j), roughness = 0.0, spec_coeff = 0.2, diff_coeff= 0.8) # n = index of refraction
#bluish_metal = Glossy(diff_color = rgb(0.0, 0, 0.1), n = vec3(1.3+1.91j, 1.3+1.91j, 1.4+2.91j), roughness = 0.2,spec_coeff = 0.5, diff_coeff= 0.3)

gold_metal = Glossy(diff_color = rgb(1., .572, .184), n = vec3(0.15+3.58j, 0.4+2.37j, 1.54+1.91j), roughness = 0.0, spec_coeff = 0.2, diff_coeff= 0.8) # n = index of refraction
bluish_metal = Glossy(diff_color = rgb(0.0, 0, 0.1), n = vec3(1.3+1.91j, 1.3+1.91j, 1.4+2.91j), roughness = 0.2,spec_coeff = 0.5, diff_coeff= 0.3)

floor =  Glossy(diff_color = image("checkered_floor.png", repeat = 80.),   
	            n = vec3(1.2+ 0.3j, 1.2+ 0.3j, 1.1+ 0.3j), roughness = 0.2, spec_coeff = 0.3, diff_coeff= 0.9 )
floor =  Glossy(diff_color = image("checkered_floor.png", repeat = 80.),
				n=vec3(1.2 + 0.3j, 1.2 + 0.3j, 1.1 + 0.3j), roughness=0.2, spec_coeff=0.3, diff_coeff=0.9)
#floor =  Glossy(diff_color = image("checkered_floor.png", repeat = 80.),
	 #           n = vec3(1.2+ 0.3j, 1.2+ 0.3j, 1.1+ 0.3j), roughness = 0.2, spec_coeff = 0.3, diff_coeff= 0.9 )






# Set Scene
current_location=3.0
for i in range(3):
	Sc = Scene(ambient_color = rgb(0.05, 0.05, 0.05))



Current_Location_0=10.0
Current_Location_1=9.0
x=0.0
for i in range (20):
 	# Set Scene
 	Sc = Scene(ambient_color = rgb(0.05, 0.05, 0.05))

# Set Scene 
Sc = Scene(ambient_color = rgb(0.05, 0.05, 0.05))

Sc.add(Sphere(material = gold_metal, center = vec3(-.75, current_location, -2.),radius =  .5, max_ray_depth = 3))
	Sc.add(Sphere(material = bluish_metal, center = vec3(1.25, current_location, -2.), radius = .5, max_ray_depth = 3))
angle = -np.pi/2 * 0.3
Sc.add_Camera(look_from = vec3(2.5*np.sin(angle), 0.25, 2.5*np.cos(angle)  -1.5 ), 
			  look_at = vec3(0., 0.25, -3.), 
	          screen_width = 400 ,
	          screen_height = 300)
 	angle = -np.pi/2 * 0.3
 	Sc.add_Camera(look_from = vec3(2.5*np.sin(angle), 1.25, 2.5*np.cos(angle)  -11.5 ),
			  look_at = vec3(0., 0.25, -3.),
	          screen_width = 400 ,
	          screen_height = 300)

 	#angle = -np.pi/2 * 0.3
 	#Sc.add_Camera(look_from = vec3(2.5*np.sin(angle), 0.25, 2.5*np.cos(angle)  -1.5 ),
 	#			  look_at = vec3(0., 0.25, -3.),
 	#	          screen_width = 400 ,
 	#	          screen_height = 300)



Sc.add_DirectionalLight(Ldir = vec3(0.52,0.45, -0.5),  color = rgb(0.15, 0.15, 0.15))
 	Sc.add_DirectionalLight(Ldir = vec3(0.52,0.45, -0.5),  color = rgb(0.15, 0.15, 0.15))


<<<<<<< .mine


=======
	img.save(".\images2"+str(i)+".png")
	current_location=current_location-0.2
>>>>>>> .theirs

#Sc.add(Sphere(material = gold_metal, center = vec3(-.75, .1, -3.),radius =  .6, max_ray_depth = 3))
 	#Sc.add(Sphere(material = bluish_metal, center = vec3(1.25, .1, -3.), radius = .6, max_ray_depth = 3))

Sc.add(Sphere(material = gold_metal, center = vec3(-.75, .1, -3.),radius =  .6, max_ray_depth = 3))
Sc.add(Sphere(material = bluish_metal, center = vec3(1.25, .1, -3.), radius = .6, max_ray_depth = 3))





Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 120.0,height = 120.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0),  max_ray_depth = 3))
# to see
#see sightpy/backgrounds
Sc.add_Background("stormydays.png")
 	#Sc.add(Sphere(material = gold_metal, center = vec3(-.75, 4, 3.),radius =  3, max_ray_depth = 3))
 	#Sc.add(Sphere(material = bluish_metal, center = vec3(-2, 3, -3.), radius = .6, max_ray_depth = 3))

	 #Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 120.0,height = 120.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0),  max_ray_depth = 3))

	 #Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 0.0,height = 120.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0),  max_ray_depth = 3))
	 # to see
	 #see sightpy/backgrounds
	 #Sc.add_Background("stormydays.png")


# Render 
img = Sc.render(samples_per_pixel = 6)


# Render 
#img = Sc.render(samples_per_pixel = 6)

img.save(".\images2\EXAMPLE1.png")

img.show()
#img.save(".\images2\EXAMPLE1.png")

#img.show()

 	Sc.add(Sphere(material = gold_metal, center = vec3(-.75, Current_Location_0, 3.),radius =  0.6, max_ray_depth = 3))
 	Sc.add(Sphere(material = bluish_metal, center = vec3(-2,Current_Location_0, -3.), radius = .6, max_ray_depth = 3))
 	x=x+0.1*1.1
 	Current_Location_0=Current_Location_0-x
 	Current_Location_1=Current_Location_1-0.2
 	#Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 120.0,height = 120.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0),  max_ray_depth = 3))
 	Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 0.0,height = 120.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0),  max_ray_depth = 3))
 	# to see
 	#see sightpy/backgrounds
 	Sc.add_Background("stormydays.png")




# Render
 	img = Sc.render(samples_per_pixel = 6)

 	img.save(".\images\SequencePhotographs\example_BallDrop"+str(i)+".png")<<<<<<< .mine
 	img.save(".\images\SequencePhotographs\example_BallDrop"+str(i)+".png")
=======

>>>>>>> .theirs
