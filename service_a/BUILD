python_sources(
    dependencies=[':gcloud_config'],
)

resource(name="gcloud_config", source='app.yaml')

pex_binary(
    name="pex_binary",
    script="gunicorn",
    args=["service_a.main:app"],
    dependencies=[":reqs", ":gcloud_config", ":service_a"],
    layout="loose",
    environment=parametrize("linux", "macos"),
)

python_requirements(
    name="reqs",
)
