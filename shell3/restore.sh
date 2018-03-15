rm -Rf prova1
rm -Rf prova2

mkdir prova1
mkdir prova2
mkdir prova3
cd prova1
touch file1
cd ../prova2
touch file2
cd ../prova3
touch file3
cd ..

# touch -at 0901011822 ./prova1/file1
# touch -at 0901011822 ./prova2/file2
touch -at 0901011822 ./prova3/file3
