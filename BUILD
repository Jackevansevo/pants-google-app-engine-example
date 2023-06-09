local_environment(
  name="macos",
  compatible_platforms=["macos_arm64"],
)

local_environment(
  name="linux",
  compatible_platforms=["linux_x86_64"],
  fallback_environment="docker",
)

docker_environment(
    name="docker",
    platform="linux_x86_64",
    image="python_postgres",
    python_bootstrap_search_path=["<PATH>"],
)

docker_image(
  name="python_postgres",
  instructions=[
    "FROM --platform=linux/x86_64 python:3.11-slim",
    "RUN apt update && apt install -y gcc libpq-dev",
  ]
)
