import myservice

if __name__ == '__main__':
    myservice.app.run(port=1337, host='::', passthrough_errors=True)
