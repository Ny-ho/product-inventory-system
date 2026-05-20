from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.routes import products

app = FastAPI()

FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api", tags=["Products"])


@app.get("/", include_in_schema=False)
async def serve_frontend():
    """Serve the inventory UI from the same deployment as the API."""
    return FileResponse(FRONTEND_DIR / "index.html")
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
             

