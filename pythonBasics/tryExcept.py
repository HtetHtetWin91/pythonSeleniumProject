try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('File not found')



try:
    with open('file.log') as file:
        read_data = file.read()

except Exception as e:
    print(e)

finally:
    print("Cleanup resources")

