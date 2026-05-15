# Bookly - RESTful Book Management API

A comprehensive FastAPI project built alongside the FastAPI course to master backend development.

## 🎯 Project Goal
Build a robust book management system where users can catalog books, manage authors, and handle reviews, progressing from simple in-memory storage to a production-ready database with authentication.

## 🚀 Current Progress: Session 22 (Pydantic)
The project currently mirrors the knowledge gained up to Session 21.

### Completed Milestones
- [x] **Project Setup**: FastAPI installation and basic server setup.
- [x] **Basic CRUD**: Implemented GET, POST, PUT, PATCH, and DELETE endpoints.
- [x] **Path & Query Params**: Handling dynamic data via URLs and query strings.
- [x] **Simple Database**: Using an in-memory list to store book data.
- [x] **Error Handling**: Using `HTTPException` for missing resources or invalid inputs.

---

## 🗺️ Roadmap & Task List

### Phase 1: Data Validation & Schemas (Current)
*Focus: Sessions 22-28 (Pydantic & JSON)*
- [ ] **Define Pydantic Models**: Create schemas for Book creation and updates.
- [ ] **Field Validation**: Add constraints (e.g., min length for titles, range for ratings).
- [ ] **Response Models**: Control what data is returned to the user.
- [ ] **Enums**: Use Enums for book genres or categories.

### Phase 2: Database Integration
*Focus: Sessions 29-46 (SQL, SQLite, SQLModel)*
- [ ] **Setup SQLite**: Connect the app to a persistent database.
- [ ] **SQLModel Integration**: Map Python classes to database tables.
- [ ] **Database Migrations**: (Later) Handle schema changes.

### Phase 3: Advanced Logic & Services
*Focus: Sessions 51-58 (Dependency Injection & Service Layer)*
- [ ] **Environment Variables**: Manage sensitive config with `.env`.
- [ ] **Service Layer**: Move business logic out of routes into separate services.
- [ ] **Dependency Injection**: Use `Depends` for database sessions.

### Phase 4: Authentication & Security
*Focus: Sessions 59-79 (JWT & OAuth2)*
- [ ] **User Model**: Create a Seller/User model with hashed passwords.
- [ ] **JWT Implementation**: Generate and verify tokens.
- [ ] **Protected Routes**: Restrict book management to authenticated users.

### Phase 5: Relationships & Features
*Focus: Sessions 80-139 (Foreign Keys, Mail, Background Tasks)*
- [ ] **Author Relationships**: Link books to authors.
- [ ] **Email Notifications**: Send emails on signup or key events.
- [ ] **Background Tasks**: Process heavy tasks without blocking the API.
- [ ] **CORS & Metadata**: Finalize API documentation and cross-origin settings.

### Phase 6: Testing & Deployment
*Focus: Sessions 140-185 (Pytest, Docker, AWS)*
- [ ] **Unit Tests**: Write tests for all endpoints using `pytest`.
- [ ] **Dockerization**: Create a Dockerfile and Compose setup.
- [ ] **Cloud Deployment**: Prepare for AWS App Runner/Render.

---

## 📚 Course Reference Mapping
| Session | Topic | Feature Integration |
| :--- | :--- | :--- |
| 1-13 | Basics | Initial endpoints and list-based storage |
| 14-21 | Methods | Full CRUD implementation |
| 22-27 | Pydantic | **[NEXT]** Add request validation schemas |
| 28-36 | SQL | Switch from lists to SQLite |
| 40-46 | SQLModel | Refactor to use SQLModel |
