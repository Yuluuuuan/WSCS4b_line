requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f line
	brane remove -f line
	brane build container.yml
	brane push line