import sys, os


with open(sys.argv[1], "r", encoding="utf-8") as doc:
  data = [list(item) for item in [ item for item in doc.readlines() ]]

  for item in data:
    for letter in item:
      testFile = open("README.md", "a", encoding="utf=8")
      testFile.write(letter)
      testFile.close()
      os.system("git add .")
      os.system(f'git commit -m "A Letra {letter} foi adicionada"')
      os.system("git push")
