rfile=open("e:\\readme.txt" , "r")
for i in range(5):
    address=f"e:\\n\\readme_copy{i+1}.txt"
    wfile=open(address, "w")
    b=rfile.read()
    wfile.write(b)
    wfile.close()
rfile.close()
    