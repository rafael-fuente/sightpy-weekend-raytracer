
from sightpy import *
from sightpy.animation import create_animation

point3 = vec3
color = vec3

light = Diffuse_light(solid_color(15, 15, 15))


scene = Scene(ambient_color = color(0.5,0.5,1.0))

#floor
scene.add(Sphere(point3(0,-1000,0), 1000, Diffuse(solid_color(0.5, 0.5, 0.5))))

scene.add(Sphere(point3(-5, 1, 0), 1.0, Diffuse(checker_texture(solid_color(0.1, 0.4, 0.1) , solid_color(0.5, 0.5, 0.5)))))
scene.add(Sphere(point3(0, 1, 0), 1.0, Diffuse(checker_texture(solid_color(0.4, 0.2, 0.1) , solid_color(0.5, 0.5, 0.5)))))
scene.add(Sphere(point3(4, 1, 0), 1.0, Diffuse(checker_texture(solid_color(0.1, 0.2, 0.4) , solid_color(0.5, 0.5, 0.5)))))


scene.add(Sphere(point3(2.5, 0.49, 1.5), 0.5, Refractive(1.5)))
scene.add(Box(point3(-0.5, 0, 2), point3(1.5, 1, 3), Diffuse(checker_texture(solid_color(0.6, 0.0, 0.0) , solid_color(0.5, 0.5, 0.5)))))

#lights
scene.add(Sphere(point3(3.5, 6, 2), 1.0, light), importance_sampled = True)
scene.add(Sphere(point3(-3.5, 5, 2), 1.0, light), importance_sampled = True)




samples_per_pixel = 500
max_depth = 4
fps = 1 
start_time = 0
final_time = 5

def update_scene(scene, t):
	final_time = 5

	aperture = 1.5 - 1.5/final_time*t
	phi0 = 1.2722973952087173
	w = (np.pi/20)/final_time


	print( aperture)
	scene.add_Camera(lookfrom = point3(14*np.sin(-w*t + phi0),3.3,14*np.cos(-w*t + phi0)),
				  lookat = point3(0,0.3,0),
				  screen_width = int(200*16/9), 
				  screen_height = 200,
				  field_of_view = 20,
				  focus_distance  = (point3(13,2,4)).length(),
				  aperture  = aperture)




create_animation(scene,samples_per_pixel,max_depth, fps, start_time, final_time, update_scene, "example1_")


