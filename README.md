# pants-google-app-engine-example

    pants generate-lockfiles

    pants export --py-resolve-format=symlinked_immutable_virtualenv --resolve=python-default

    source dist/export/python/virtualenvs/python-default/3*/bin/activate

    pants package service_a:pex_binary

    gcloud app deploy dist/service_a/pex_binary@environment=linux.pex --appyaml dist/service_a/pex_binary@environment=linux.pex/service_a/app.yaml
