all:
	javac *.java

test:
	python3 test.py

clean:
	rm *.class
