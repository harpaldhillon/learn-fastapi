from fastapi import FastAPI, Body

IMAGES = [
        {'name':'ubi8', 'current_tag':'1.0', 'previous_tag':'0.4', 'org':'redhat plc'},
        {'name':'ubi9', 'current_tag':'2.0', 'previous_tag':'1.0', 'org':'redhat plc'},
        {'name':'ubuntu', 'current_tag':'9', 'previous_tag':'8', 'org':'canonical'},
        {'name':'kali', 'current_tag':'11.0', 'previous_tag':'10.4', 'org':'kali org'},
        {'name':'mongodb', 'current_tag':'0.8', 'previous_tag':'0.8', 'org':'mongo'},
        ]

app = FastAPI()

@app.get("/images")
async def get_images():
    return IMAGES

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    for image in IMAGES:
        if image.get('name').casefold() == image_name.casefold():
            return image

@app.get("/images/")
async def read_images_by_org(org: str):
    image_list = []
    for image in IMAGES:
        if image.get('org').casefold() == org.casefold():
            image_list.append(image)

    return image_list

@app.post("/images/create_image")
async def add_new_image(new_image=Body()):
    IMAGES.append(new_image)

@app.put("/images/update_image")
async def update_image(updated_image=Body()):
    for i in range(len(IMAGES)):
        if IMAGES[i].get('name').casefold() == updated_image.get('name').casefold():
            IMAGES[i] = updated_image

@app.delete("/images/delete_image/{image_name}")
async def delete_image(image_name: str):
    for i in range(len(IMAGES)):
        if IMAGES[i].get('name').casefold() == image_name.casefold():
            IMAGES.pop(i)
            break
