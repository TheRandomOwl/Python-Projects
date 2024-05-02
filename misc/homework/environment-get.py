import os

def environment(filename):
    '''
    Write the current OS environemnt variables to a file
    input: filename (str)
    output: None
    For example, if the environment variables are:
    PATH=/usr/bin

    The file should contain:
    PATH=/usr/bin
    '''
    with open(filename, 'w') as f:
        for key, value in os.environ.items():
            f.write(f"{key}={value}\n")

def main():
    environment('env.txt')

if __name__ == '__main__':
    main()