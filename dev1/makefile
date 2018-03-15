MONTH=$(shell date +%B | awk 'BEGIN{FS=" "} {print $3}')
MONTHC=$(MONTH).c
MONTHO=$(MONTH).o

all: $(MONTHO) strange_app

$(MONTHO): $(MONTHC)
	gcc -c $< -o $@
strange_app: strange_app.c $(MONTHO)
	gcc $^ -o $@
clean:
	rm -f *.o
	rm -f strange_app
