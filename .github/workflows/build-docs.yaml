name: Build Docs

on: push

jobs:

  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Build the Docker image
      run: docker build --file Dockerfile --tag build-docs:$(date +%s)
    - name: Run the Docker image
      run: docker run -w /src -v ./Specification:/src/Specification -v ./build:/src/build build-docs:$(date +%s) ./Scripts/buildDocs.sh