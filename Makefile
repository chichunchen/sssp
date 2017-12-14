all:
	javac *.java

test:
	python3 test.py 20 10 40 4

clean:
	rm *.class
