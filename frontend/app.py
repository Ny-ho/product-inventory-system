# import streamlit as st
# import requests
# import pandas as pd

# # 🎨 Apply Custom CSS for Styling
# st.markdown("""
#     <style>
#         html {
#             background-color: #71797E;
#         }
#         div.stButton > button {
#             background-color: steelblue;
#             color: white;
#             border-radius: 10px;
#             padding: 8px;
#             font-size: 16px;
#         }
#         div.stAlert {
#             border-radius: 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Update this if your live Render API URL changes later!
# BASE_URL = "http://127.0.0.1:8000/api"

# st.markdown("<h3>📦 Inventory Management - Products</h3>", unsafe_allow_html=True)

# # =====================================================================
# # API COMMUNICATION FUNCTIONS
# # =====================================================================

# def get_products():
#     """Fetches all inventory records from the backend."""
#     try:
#         response = requests.get(f"{BASE_URL}/products")  # Matches @router.get("/products")
#         return response.json() if response.status_code == 200 else []
#     except requests.exceptions.RequestException as e:
#         st.error(f"⚠️ Error fetching products: {e}")
#         return []


# def add_product(name, category, price, stock):
#     """Sends a payload to create a new product inventory record."""
#     data = {"name": name, "category": category, "price": price, "stock": stock}
#     response = requests.post(f"{BASE_URL}/products", json=data)  # Matches @router.post("/products")
#     return response.json()


# def update_product(product_id, price, stock):
#     """Sends patch data to dynamically update an item."""
#     data = {}
#     if price is not None and price > 0.01:  # Ensure price is valid
#         data["price"] = price
#     if stock is not None:  # Always allow stock updates
#         data["stock"] = stock

#     if not data:
#         return {"message": "⚠️ No valid fields to update!"}

#     response = requests.put(f"{BASE_URL}/products/{product_id}", json=data)  # Matches @router.put("/products/{id}")
#     return response.json()


# def delete_product(product_id):
#     """Instructs the backend database to drop an item entry by ID."""
#     response = requests.delete(f"{BASE_URL}/product/{product_id}")  # Matches @router.delete("/product/{product_id}")
#     return response.json()


# # =====================================================================
# # STREAMLIT USER INTERFACE TABS
# # =====================================================================

# tab1, tab2, tab3, tab4 = st.tabs(["📋 View Products", "➕ Add Product", "✏️ Update Product", "🗑️ Delete Product"])

# # 🟢 Tab 1: View Products
# with tab1:
#     st.subheader("📋 Products List")

#     if st.button("🔄 Refresh", key="refresh_button"):
#         st.rerun()

#     products = get_products()  # Fetch products from API

#     if products:
#         df = pd.DataFrame(products)
#         st.dataframe(df, hide_index=True)  # Clean dataframe layout display
#     else:
#         st.warning("⚠️ No products found or API response is empty.")


# # 🔵 Tab 2: Add Product
# with tab2:
#     st.subheader("➕ Add New Product")
#     name = st.text_input("Product Name")
#     category = st.text_input("Category")
#     price = st.number_input("Price", min_value=0.01, format="%.2f")
#     stock = st.number_input("Stock", min_value=0, step=1)

#     if st.button("Add Product", key="add_product_button"):
#         if name:
#             result = add_product(name, category, price, stock)
#             st.success(result.get("message", "✅ Product processed successfully!"))
#             st.rerun()
#         else:
#             st.warning("⚠️ Product name cannot be blank.")


# # 🟡 Tab 3: Update Product
# with tab3:
#     st.subheader("✏️ Update Product Details")
#     product_id = st.number_input("Product ID", min_value=1, step=1)
#     new_price = st.number_input("New Price", min_value=0.00, format="%.2f")
#     new_stock = st.number_input("New Stock", min_value=0, step=1)

#     if st.button("Update Product", key="update_product_button"):
#         # Setup clean conditional fallbacks to check if fields were altered
#         passed_price = new_price if new_price > 0.01 else None
#         result = update_product(product_id, passed_price, new_stock)
#         st.success(result.get("message", "✅ Product handled!"))
#         st.rerun()


# # 🔴 Tab 4: Delete Product (With Session Confirmation safety steps)
# with tab4:  
#     st.subheader("🗑️ Delete Product")

#     delete_id = st.number_input("🔢 Enter Product ID to Delete", min_value=1, step=1)

#     if "confirm_delete" not in st.session_state:
#         st.session_state.confirm_delete = False  # Initialize layout verification tracker

#     # Click Initial Button -> Prompt Safety Interstitial
#     if st.button("🗑️ Delete Product", key="delete_product_button"):
#         if delete_id:
#             st.session_state.confirm_delete = True
#         else:
#             st.warning("⚠️ Please enter a valid Product ID.")

#     # Interstitial execution loop block
#     if st.session_state.confirm_delete:
#         st.warning(f"⚠️ Are you sure you want to completely erase Product ID {delete_id}?")

#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button("✅ Yes, Delete", key="confirm_delete_button"):
#                 if delete_id:
#                     result = delete_product(delete_id)
#                     st.success(result.get("message", "✅ Product dropped."))
#                 else:
#                     st.error("❌ Invalid Product ID reference")

#                 st.session_state.confirm_delete = False  # Clean out session tracker state
#                 st.rerun()

#         with col2:
#             if st.button("❌ Cancel", key="cancel_delete_button"):
#                 st.session_state.confirm_delete = False  # Abort run safely
#                 st.rerun()