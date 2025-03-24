# API Testing on DummyJSON

This repository contains API tests for [DummyJSON](https://dummyjson.com/), focusing on:
- **Authentication APIs**
- **Products APIs**
- **Users APIs**

## 📌 Tools Used
- **Postman** (for API testing)
- **Newman** (for CLI-based testing)

## 🚀 How to Use
### 1️⃣ Import the Collection
1. Open **Postman**.
2. Click **Import** → Select `dummyjson_collection.json`.
3. (Optional) Import `dummyjson_environment.json`.

### 2️⃣ Run API Tests in Postman
1. Open the **Collection Runner**.
2. Select `dummyjson_collection.json`.
3. Click **Run**.

### 3️⃣ Run Tests Using Newman (CLI)
1. Install **Newman** (if not already installed):
   ```sh
   npm install -g newman
