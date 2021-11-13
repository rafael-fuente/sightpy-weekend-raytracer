
from sightpy import *

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




scene.add_Camera(lookfrom = point3(13,3.3,4),
			  lookat = point3(0,0.3,0),
			  screen_width = int(200*16/9), 
			  screen_height = 200,
			  field_of_view = 20,
			  focal_distance  = (point3(13,2,4)).length(),
			  aperture  = 0.1)


img = scene.render(samples_per_pixel = 300, max_depth = 4)

img.save("example1.png")

img.show()

