from pathlib import Path

from fastapi import FastAPI, Request, HTTPException, status
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


posts: list[dict] = [
    {
        "id": "1",
        "author": "Krishna",
        "title": "Krishna_123",
        "content": "Jai Krishna",
        "date_posted": "April 20, 2025",
    },
    {
        "id": "2",
        "author": "Rama",
        "title": "Rama_1",
        "content": "Jai Rama",
        "date_posted": "April 20, 2025"
    },
]   

@app.get("/", name="home")
@app.get("/posts",  name="posts")
def home(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts, "title":"Home"})

@app.get("/posts")
def get_posts():
    return posts

@app.get("/posts/{post_id}")
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == str(post_id):
            return templates.TemplateResponse(request,"post.html",{"post": post, "title": post.get("title")[:50]})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/api/posts/{post_id}")
def get_post_api(post_id: int):
    for post in posts:
        if post.get("id") == str(post_id):
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


def hoome():
    return { "message":"home"}