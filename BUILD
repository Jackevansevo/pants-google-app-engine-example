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
    image="python:3.11-slim",
    python_bootstrap_search_path=["<PATH>"],
)
