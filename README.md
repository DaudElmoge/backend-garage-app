# 🚗 Garage App Backend

This is the backend for my Garage App project. I built it using **FastAPI** and **SQLAlchemy**. The goal of this backend is to help garages track customer visits by recording both service and repair details for every vehicle. It also allows quick customer lookups using phone numbers.

## 📌 Project Goal

This backend supports the following main features:

1. Logging **service** and **repair** records for customers
2. Viewing a customer's full history (service + repairs)
3. Searching customers by **phone number**

## 🧍 Models & Relationships

### 🧑‍🔧 Customer
- `id`: Integer (Primary key)
- `name`: String
- `phone`: String (used for search)

### 🛠️ ServiceRecord
- `id`: Integer
- `vehicle_number`: String
- `car_make`: String
- `car_model`: String
- `mechanic_name`: String
- `service_type`: String
- `service_date`: Date
- `service_time`: Time
- `comments`: String
- `customer_id`: ForeignKey → Customer

### 🔧 RepairRecord
- `id`: Integer
- `vehicle_number`: String
- `car_make`: String
- `car_model`: String
- `mechanic_name`: String
- `repair_type`: String
- `repair_date`: Date
- `repair_time`: Time
- `comments`: String
- `customer_id`: ForeignKey → Customer

### 🔗 Relationships
- One **Customer** ➝ many **ServiceRecords**
- One **Customer** ➝ many **RepairRecords**

## 🧠 User Stories (Backend Support)

- ✅ I can log service and repair details (POST endpoints)
- ✅ I can get full service/repair history by customer ID
- ✅ I can search for a customer using their phone number

