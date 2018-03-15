rm -Rf dirA
rm -Rf dirB
rm -f file1

touch file1
mkdir dirA
cd dirA
mkdir dirC
cd dirC
touch file4
touch file5
mkdir dirD
cd dirD
touch file8
touch file6
touch file7
cd ..
cd ..
mkdir dirE
cd dirE
touch file9
cd ..
touch file2
touch file3
cd ..
mkdir dirB
cd dirB
touch file10
mkdir dirF
cd dirF
touch file11
touch file12
mkdir dirG
cd dirG
touch file13
cd ..
cd ..
cd ..

touch -at 0901011822 ./dirA/dirC/dirD/file6
touch -at 0901011822 ./dirB/file10
