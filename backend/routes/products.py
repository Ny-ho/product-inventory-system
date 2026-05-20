from fastapi import APIRouter,HTTPException
from backend.database import get_db_cursor
from backend.schemas import Product,ProductUpdate

router=APIRouter()

@router.post("/products")
def add_product(product:Product):
    with get_db_cursor(commit=True) as cursor:
        sql="INSERT INTO products(name,category,price,stock) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,(product.name,product.category,product.price,product.stock))
    return {"message":"product added successfully"}
    
@router.get("/products")
def list_products():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

@router.get("/products/{product_id}")
def get_product(product_id:int):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE id=%s",(product_id,))
        product=cursor.fetchone()
        if not product:
            raise HTTPException(status_code=404,detail="product not found")
        return product

@router.put("/products/{id}")
def update_product(id:int,product:ProductUpdate):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("SELECT * FROM products where id=%s",(id,))
        existing_product=cursor.fetchone()
        if not existing_product:
            raise HTTPException(status_code=404,detail="item doesnot exist to update")
        
        update_fields=[]
        update_values=[]
        if product.price is not None:
            update_fields.append("price=%s")
            update_values.append(product.price)
        if product.stock is not None:
            update_fields.append("stock=%s")
            update_values.append(product.stock)
        if update_fields:
            sql=f"UPDATE products SET {','.join(update_fields)} WHERE id=%s"
            update_values.append(id)
            cursor.execute(sql,update_values)
    return {"message":"product updated successfully"}

@router.delete("/product/{product_id}")
def remove_product(product_id:int):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("SELECT * FROM products WHERE id=%s",(product_id,))
        product=cursor.fetchone()
        if not product:
            raise HTTPException(status_code=404,detail="product not found")

        cursor.execute("DELETE FROM products WHERE id=%s",(product_id,))
    return{"message":"item deleted successfully"}
        
