import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2] / "03_pydanticai_structured_output"))

from fastapi import FastAPI
from pydantic_ai import Agent
from model import nvidia_model
from utils import query_duckdb
from data_models import Movie, Prompt

app = FastAPI()

agent = Agent(
    model=nvidia_model("nvidia/nemotron-3.5-lightning-30b-a3b"),
)


@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;")
    return movies.to_dict(orient="records")


@app.post("/movie")
async def create_movie(query: Prompt):
    result = await agent.run(query.prompt, output_type=Movie)
    movie = result.output

    # protect against SQL injection
    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?)",
        parameters=[movie.title, movie.year, movie.genre, movie.rating],
    )

    return movie
