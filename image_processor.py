#
#Convert the units from coordinates to Decimal Degrees and consider the longitude reference of the image
def decimal_coords(coords,ref):
    decimal_deg= coords[0]+ coords[1]/60 + coords[2]/3600
    if ref =="S" or ref== "E":
        decimal_deg= decimal_deg
    return decimal_deg
#
#Read exif data from an image before processing it to the final output
from exif import Image
img_path= '../../carpark_images/IMG_20221019_174100.jpg'
with open(img_path,'rb')as src:
    img=Image(src)
#
#Check all exif metadata from the application
if img.has_exif:
    #
    #Enclose the program's execution in a try catch block
    try:
        img.gps_longitude
        coordinates= (decimal_coords(
                img.gps_latitude,img.gps_latitude_ref),
                decimal_coords(
                img.gps_longitude, img.gps_longitude_ref
           )
        )
    #Handle the thrown exception
    except AttributeError: 
        print("No coordinates are available for this image")
else: 
    print("The image does not have exif information")
print(f"Image is located at {src.name}")
print(f"Was taken: {img.datetime_original}, and has coordinates:{coordinates}")


