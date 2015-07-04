import time

for i in range(10):
    time.sleep((i+1)/10)
    print('Slept for {0} seconds'.format((i+1)/10))

print('Application finished.')
print('Testing new git config...')
