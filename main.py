from fastapi import FastAPI
app = FastAPI()

#just for frontend
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your HTML file to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from backend.routes import products

app.include_router(products.router,prefix="/api",tags=["Products"])
# books_data={
#     1:{
      
#        "name":"shadow slave",
#         "author":"guilty three",
#         "status":"available"
#     },
#     2:{
#         "name":"operating system",
#         "author":"a.k.chandrashekar",
#         "status":"out of stock"

#     },
#     3:{
#         "name":"ww",
#         "author":"ws",
#         "status":"yy"

#     }
# }
# @app.get("/user_pathparam/{id}") #path param where we type id and it shows your id
# def pathparam(id:int):
#     return{"userid :":id}

# @app.get("/personal_queryparam") #query param same as pp butis more for like filtering .all name ,str, are qp
# def queryparam(name:str,age:int,address:str|None=None):
#     return{"name":name,"age":age,"address":address}

# @app.get("/test_combime_path_and_query/{phonenum}/details")#phone num as path param and email as query param
# def very_personal(phonenum:int,include_email:bool):
#     if include_email :
#         return{"phonenum:":phonenum,"email":include_email}
#     else:
#         return{"phonenum:":phonenum,"email":"email not givem"}


# @app.get("/my_name")
# def name()->dict: 
#     return {"john":"doe"}

# @app.get("/books/{id}")
# def search_book(id:int):

#     if id in books_data:
#             return books_data[id]
#     else:

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"book with id {id} not found")
   
# @app.post("/books")
# def create_book(name,author,status):
#     new_id=max(books_data.keys())+1
#     books_data[new_id]={
#         "name":name,
#         "author":author,
#         "status":status
#     }

# @app.put("/update/{id}")
# def update_book(name,author,status):
#     if id in books_data:
#         books_data[id]={
#         "name":name,
#         "author":author,
#         "status":status

#         }
# @app.patch("/update_with_selection")
# def update_book_patch(id:int,name:str|None=None,author:str|None=None,status:str|None=None):
#     book =books_data[id]
#     if name:
#         book["name"]=name
#     if author:
#         book["author"]=author
#     if status:
#         book["status"]=status
#     books_data[id]=book
#     return book

# @app.delete("/delete")
# def delete(id:int):
#     books_data.pop(id)
#     return {f"book data of id {id} is deleted successfully"} 

# @app.get("/scalar",include_in_schema=False)
# def get_scalar_docs():
#     return get_scalar_api_reference(
#         openapi_url=app.openapi_url,
#         title="Scalar API",

#     )
#
             

