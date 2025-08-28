from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load JSON file once at startup
json_file = os.path.join(os.path.dirname(__file__), "food_delivery_reviews.json")
with open(json_file, "r") as f:
    reviews = json.load(f)

@app.get("/")
def home():
    return {"message": "Food Delivery Reviews API is running. Use /reviews endpoint."}

@app.get("/reviews")
def get_reviews(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
    start = (page - 1) * limit
    end = start + limit
    paginated_reviews = reviews[start:end]
    
    return {
        "page": page,
        "limit": limit,
        "total_reviews": len(reviews),
        "reviews": paginated_reviews
    }
