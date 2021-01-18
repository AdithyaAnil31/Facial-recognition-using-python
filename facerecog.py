# Importing modules
import PIL.Image
import PIL.ImageDraw
import face_recognition #must pip install, link in readme 

# Reading the image for which the faces has to be detected
file = face_recognition.load_image_file('face.jpg')
faces = face_recognition.face_locations(file)
print(faces)

# Now we find the number of faces
faces_count = len(faces)
print("There are {} face(s) in this image".format(how_many_faces))

# This here draws rectangles around the face
picture = PIL.Image.fromarray(file)
rect_draw = PIL.ImageDraw.Draw(picture)

for i in faces:
    top, right, bottom, left = i
    rect_draw.rectangle([right, bottom, left, top],
                           outline="green", width=8)
pil_picture.show()
