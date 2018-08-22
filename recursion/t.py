SERVER_IMAGE = "hello, I'M default"

if __name__ == "__main__":
    server_image = "aa"
    deployment_server_image = server_image if server_image else SERVER_IMAGE
    print(deployment_server_image)
