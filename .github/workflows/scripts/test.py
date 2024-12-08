import os

def main():
    with open(os.environ['GITHUB_OUTPUT'], 'w') as f:
        l = '\n'.join(['123', '456', '789'])
    
        f.write('test1<<EOF\n')
        f.write(f'{l}\n')
        f.write('EOF\n')


if __name__ == '__main__':
    main()