# Use the official Ubuntu 20.04 image as the base image
FROM ubuntu:20.04

# Set the Go version to be installed
ENV GO_VERSION=1.21.3

# Download and install Go
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz && \
    rm go${GO_VERSION}.linux-amd64.tar.gz && \
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Go environment variables
ENV PATH="/usr/local/go/bin:${PATH}"
ENV GOPATH="/go"
ENV GOBIN="/go/bin"

# Create a directory for the Go workspace
RUN mkdir -p /go/src /go/bin

# Set the working directory to the Go workspace
WORKDIR /go/src

# Print Go version and run your application
# CMD ["go", "version"]

# Run an interactive shell when the container starts
CMD ["/bin/bash"]
